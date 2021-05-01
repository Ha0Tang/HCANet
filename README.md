# XingVTON (PAMI)
Official implementation of XingVTON for "Cross-Attention Is What You Need for Person Image Generation and Virtual Try-On" .
<br/>Project page: [TODO](-----). 
<br/>Saved/Pre-trained models: [TODO](--------)
<br/>Dataset: [XingVTON](https://1drv.ms/u/s!Ai8t8GAHdzVUiQQYX0azYhqIDPP6?e=4cpFTI)
<br/>The code and pre-trained models are tested with pytorch 0.4.1, torchvision 0.2.1, opencv-python 4.1 and pillow 5.4 (Python 3 env).
<br/><br/>
[Project page]() | [Paper]() | [Dataset]() | [Model]() | [Video]()
<br/><br/>
![Teaser](./teaser.png)
	
## Usage
This pipeline is a combination of consecutive training and testing of person-cloth crossing (PCC) block based GMM and TOM. GMM generates the warped clothes according to the target human. Then, TOM blends the warped clothes outputs from GMM into the target human properties, to generate the final try-on output.

1) Install the requirements
2) Download/Prepare the dataset
3) Train the Person-Cloth Crossing (PCC) block based GMM network
4) Get warped clothes for training set with trained GMM network, and copy warped clothes & masks inside `data/train` directory
5) Train the Person-Cloth Crossing (PCC) block based TOM network
6) Test PCC block based GMM for testing set
7) Get warped clothes for testing set, copy warped clothes & masks inside `data/test` directory
8) Test PCC block based TOM testing set

## Installation
This implementation is built and tested in PyTorch 0.4.1.
Pytorch and torchvision are recommended to install with conda: `conda install pytorch=0.4.1 torchvision=0.2.1 -c pytorch`
<br/>For all packages, run `pip install -r requirements.txt`

## Data preparation
For training/testing VITON dataset, our full and processed dataset is available here: https://1drv.ms/u/s!Ai8t8GAHdzVUiQQYX0azYhqIDPP6?e=4cpFTI. After downloading, unzip to your own data directory.

## Training
Run `python train.py` with your specific usage options for GMM and TOM stage.
<br/>For example, GMM: ```python train.py --name GMM --stage GMM --workers 4 --save_count 5000 --shuffle```
<br/> Then run test.py for GMM network with the training dataset, which will generate the warped clothes and masks in "warp-cloth" and "warp-mask" folders inside the "result/GMM/train/" directory. Copy the "warp-cloth" and "warp-mask" folders into your data directory, for example inside "data/train" folder.
<br/>Run TOM stage, ```python train.py --name TOM --stage TOM --workers 4 --save_count 5000 --shuffle```



## Evaluation
We adopt four evaluation metrics in our work for evaluating the performance of the proposed XingVTON. There are Jaccard score (JS), structral similarity index measure (SSIM), learned perceptual image patch similarity (LPIPS), and Inception score (IS).

Note that JS is used for the same clothing retry-on cases (with ground truth cases) in the first geometric matching stage, while SSIM and LPIPS are used for the same clothing retry-on cases (with ground truth cases) in the second try-ob stage. In addition, IS is used to for different clothing try-on (where no ground truth is available). 
### For JS 
- Step1: Run```python test.py --name GMM --stage GMM --workers 4 --datamode test --data_list test_pairs_same.txt --checkpoint checkpoints/GMM/gmm_final.pth```
then the parsed segmentation area for current upper clothing is used as the reference image, accompanied with generated warped clothing mask then:

- Step2: Run```python metrics/getJS.py```


### For SSIM
After we run test.py for GMM network with the testibng dataset, the warped clothes and masks will be generated in "warp-cloth" and "warp-mask" folders inside the "result/GMM/test/" directory. Copy the "warp-cloth" and "warp-mask" folders into your data directory, for example inside "data/test" folder. Then:
- Step1: Run TOM stage test ```python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs_same.txt --checkpoint checkpoints/TOM/tom_final.pth```
Then the original target human image is used as the reference image, accompanied with the generated retry-on image then:
- Step2: Run ```python metrics/getSSIM.py```

### For LPIPS
- Step1: You need to creat a new virtual enviriment, then install PyTorch 1.0+ and torchvision;
- Step1: Run ```sh metrics/PerceptualSimilarity/testLPIPS.sh```;

### For IS
- Step1: Run TOM stage test ```python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/TOM/tom_final.pth```
- Step2: Run ```python metrics/getIS.py```


## Inference/Demo
Download the pre-trained models from here: TODO.
Then run the same step as Testing to test/inference our model.
The code and pre-trained models are tested with pytorch 0.4.1, torchvision 0.2.1, opencv 4.1 and pillow 5.4.


## Citation
Please cite our paper in your publications if it helps your research:
```
TODO
```

### Acknowledgements
This implementation is largely based on the PyTorch implementation of [CP-VTON](https://github.com/sergeywong/cp-vton) and [CP-VTON+](https://github.com/minar09/cp-vton-plus). We are extremely grateful for their public implementation.
