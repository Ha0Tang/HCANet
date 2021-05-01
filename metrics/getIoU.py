import numpy as np
import os
from skimage.io import imread, imsave


def iou(img1, img2):
	lable_area = 0
	res_area = 0
	intersection_area = 0

	rows, cols = img1.shape[:2]

	for row in range(rows):
		for col in range(cols):
			if img1[row][col] == 255 and img2[row][col] == 255:
				intersection_area += 1
				lable_area +=  1
				res_area += 1
			elif img1[row][col] == 255  and img2[row][col] != 255:
				lable_area += 1
			elif img1 [row][col] != 255 and img2[row][col] == 255:
				res_area += 1
 			
	
	combine_area = lable_area + res_area - intersection_area

	iou = intersection_area / combine_area
	return iou 


def iou_score(warpedMask_imgs, mask_onPerson_imgs):
	iou_score_list = []
	for warpedMask_img, mask_onPerson_img in zip(warpedMask_imgs, mask_onPerson_imgs):
		# print(type(warpedMask_img))
		# print(type(mask_onPerson_img))
		iou_score = iou(warpedMask_img, mask_onPerson_img)
		iou_score_list.append(iou_score)

	return np.mean(iou_score_list)


def test(warpedMask_dir, mask_onPerson_dir):
	print("Loading Images...")

	warpedMask_imgs = []
	for img_nameWM in os.listdir(warpedMask_dir):
		imgWM = imread(os.path.join(warpedMask_dir, img_nameWM))
		warpedMask_imgs.append(imgWM)

	mask_onPerson_imgs = []
	for img_nameOP in os.listdir(mask_onPerson_dir):
		imgOP = imread(os.path.join(mask_onPerson_dir, img_nameOP))
		mask_onPerson_imgs.append(imgOP)

	print("######IOU######")
	Final_iou_score = iou_score(warpedMask_imgs, mask_onPerson_imgs)
	print("IOU: %s " % Final_iou_score)


if __name__ == "__main__":
	warpedMask_dir = '/home/data/try-on/cp-vton_Plus/result/GMM/test/warp-mask'
	mask_onPerson_dir = '/home/data/try-on/cp-vton_Plus/result/GMM/test/pcm'
	# img1_path = '/home/data/try-on/cp-vton-plus/result/GMM/test/warp-mask/000028_0.jpg'
	# img2_path = '/home/data/try-on/cp-vton-plus/result/GMM/test/pcm/000028_0.jpg'



	# print(iou(imread(img1_path), imread(img2_path)))
	test(warpedMask_dir, mask_onPerson_dir)


