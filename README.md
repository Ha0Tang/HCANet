[![License CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC4.0-blue.svg)](https://github.com/Ha0Tang/XingVTON/blob/master/LICENSE.md)
![Python 3.6](https://img.shields.io/badge/python-3.6.9-green.svg)
![Packagist](https://img.shields.io/badge/Pytorch-0.4.1-red.svg)
![Last Commit](https://img.shields.io/github/last-commit/Ha0Tang/XingVTON)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-blue.svg)]((https://github.com/Ha0Tang/XingVTON/graphs/commit-activity))
![Contributing](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

## Contents
  - [HCANet](#HCANet)
  - [Usage](#Usage)
  - [Installation](#Installation)
  - [Data Preparation](#Dataset-Preparation)
  - [Training](#Training)
  - [Evaluation](#Evaluation)
  - [Inference](#Inference)
  - [Acknowledgments](#Acknowledgments)
  - [Related Projects](#Related-Projects)
  - [Citation](#Citation)
  - [Contributions](#Contributions)
  - [Collaborations](#Collaborations)

## HCANet
Official PyTorch implementation of our paper "Hierarchical Cross-Attention for Virtual Try-On".
The code and pre-trained models are tested with pytorch 0.4.1, torchvision 0.2.1, opencv-python 4.1, and pillow 5.4 (Python 3.6).

### [License](./LICENSE.md)
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />
Copyright (C) 2021 University of Trento, Italy.

All rights reserved.
Licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) (**Attribution-NonCommercial-ShareAlike 4.0 International**)

The code is released for academic research use only. For commercial use, please contact [bjdxtanghao@gmail.com](bjdxtanghao@gmail.com).

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

For all packages, run `pip install -r requirements.txt`

## Data Preparation
For training/testing VITON dataset, our full and processed dataset is available here: https://1drv.ms/u/s!Ai8t8GAHdzVUiQQYX0azYhqIDPP6?e=4cpFTI. After downloading, unzip to your own data directory `./data/`.

## Training
Run `python train.py` with your specific usage options for GMM and TOM stage.

For example, GMM: ```python train.py --name GMM --stage GMM --workers 4 --save_count 5000 --shuffle```.
Then run test.py for GMM network with the training dataset, which will generate the warped clothes and masks in "warp-cloth" and "warp-mask" folders inside the "result/GMM/train/" directory. 
Copy the "warp-cloth" and "warp-mask" folders into your data directory, for example inside "data/train" folder.

Run TOM stage, ```python train.py --name TOM --stage TOM --workers 4 --save_count 5000 --shuffle```

## Evaluation
We adopt four evaluation metrics in our work for evaluating the performance of the proposed XingVTON. There are Jaccard score (JS), structral similarity index measure (SSIM), learned perceptual image patch similarity (LPIPS), and Inception score (IS).

Note that JS is used for the same clothing retry-on cases (with ground truth cases) in the first geometric matching stage, while SSIM and LPIPS are used for the same clothing retry-on cases (with ground truth cases) in the second try-on stage. In addition, IS is used for different clothing try-on (where no ground truth is available).

### For JS 
- Step1: Run```python test.py --name GMM --stage GMM --workers 4 --datamode test --data_list test_pairs_same.txt --checkpoint checkpoints/GMM_pretrained/gmm_final.pth```
then the parsed segmentation area for current upper clothing is used as the reference image, accompanied with generated warped clothing mask then:
- Step2: Run```python metrics/getJS.py```

### For SSIM
After we run test.py for GMM network with the testibng dataset, the warped clothes and masks will be generated in "warp-cloth" and "warp-mask" folders inside the "result/GMM/test/" directory. Copy the "warp-cloth" and "warp-mask" folders into your data directory, for example inside "data/test" folder. Then:
- Step1: Run TOM stage test ```python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs_same.txt --checkpoint checkpoints/TOM_pretrained/tom_final.pth```
Then the original target human image is used as the reference image, accompanied with the generated retry-on image then:
- Step2: Run ```python metrics/getSSIM.py```

### For LPIPS
- Step1: You need to creat a new virtual enviriment, then install PyTorch 1.0+ and torchvision;
- Step2: Run ```sh metrics/PerceptualSimilarity/testLPIPS.sh```;

### For IS
- Step1: Run TOM stage test ```python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/TOM_pretrained/tom_final.pth```
- Step2: Run ```python metrics/getIS.py```

## Inference
The pre-trained models are directly provided in this project (./checkpoints).
Just run the same step as Evaluation to test/inference our model.

## Acknowledgements
This source code is inspired by [CP-VTON](https://github.com/sergeywong/cp-vton), [CP-VTON+](https://github.com/minar09/cp-vton-plus), and [XingGAN](https://github.com/Ha0Tang/XingGAN).

## Related Projects
**[XingGAN](https://github.com/Ha0Tang/XingGAN) | [CIT](https://github.com/Amazingren/CIT) | [BiGraphGAN](https://github.com/Ha0Tang/BiGraphGAN) | [GestureGAN](https://github.com/Ha0Tang/GestureGAN) | [C2GAN](https://github.com/Ha0Tang/C2GAN) | [SelectionGAN](https://github.com/Ha0Tang/SelectionGAN) | [Guided-I2I-Translation-Papers](https://github.com/Ha0Tang/Guided-I2I-Translation-Papers)**

## Citation
If you use this code for your research, please consider giving a star :star: and citing our [paper](https://arxiv.org/abs/2007.09278) :t-rex::

XingGAN
```
@inproceedings{tang2020xinggan,
  title={XingGAN for Person Image Generation},
  author={Tang, Hao and Bai, Song and Zhang, Li and Torr, Philip HS and Sebe, Nicu},
  booktitle={ECCV},
  year={2020}
}
```

If you use the original [CIT](https://github.com/Amazingren/CIT), [BiGraphGAN](https://github.com/Ha0Tang/BiGraphGAN), [GestureGAN](https://github.com/Ha0Tang/GestureGAN), [C2GAN](https://github.com/Ha0Tang/C2GAN), and [SelectionGAN](https://github.com/Ha0Tang/SelectionGAN) model, please consider giving stars :star: and citing the following papers :t-rex::

Cloth Interactive Transformer (CIT)
```
@article{ren2021cloth,
  title={Cloth Interactive Transformer for Virtual Try-On},
  author={Ren, Bin and Tang, Hao and Meng, Fanyang and Ding, Runwei and Shao, Ling and Torr, Philip HS and Sebe, Nicu},
  journal={arXiv preprint arXiv:2104.05519},
  year={2021}
}
```

BiGraphGAN
```
@inproceedings{tang2020bipartite,
  title={Bipartite Graph Reasoning GANs for Person Image Generation},
  author={Tang, Hao and Bai, Song and Torr, Philip HS and Sebe, Nicu},
  booktitle={BMVC},
  year={2020}
}
```

GestureGAN
```
@article{tang2019unified,
  title={Unified Generative Adversarial Networks for Controllable Image-to-Image Translation},
  author={Tang, Hao and Liu, Hong and Sebe, Nicu},
  journal={IEEE Transactions on Image Processing (TIP)},
  year={2020}
}

@inproceedings{tang2018gesturegan,
  title={GestureGAN for Hand Gesture-to-Gesture Translation in the Wild},
  author={Tang, Hao and Wang, Wei and Xu, Dan and Yan, Yan and Sebe, Nicu},
  booktitle={ACM MM},
  year={2018}
}
```

C2GAN
```
@article{tang2021total,
  title={Total Generate: Cycle in Cycle Generative Adversarial Networks for Generating Human Faces, Hands, Bodies, and Natural Scenes},
  author={Tang, Hao and Sebe, Nicu},
  journal={IEEE Transactions on Multimedia (TMM)},
  year={2021}
}

@inproceedings{tang2019cycleincycle,
  title={Cycle In Cycle Generative Adversarial Networks for Keypoint-Guided Image Generation},
  author={Tang, Hao and Xu, Dan and Liu, Gaowen and Wang, Wei and Sebe, Nicu and Yan, Yan},
  booktitle={ACM MM},
  year={2019}
}
```

SelectionGAN
```
@inproceedings{tang2019multi,
  title={Multi-channel attention selection gan with cascaded semantic guidance for cross-view image translation},
  author={Tang, Hao and Xu, Dan and Sebe, Nicu and Wang, Yanzhi and Corso, Jason J and Yan, Yan},
  booktitle={CVPR},
  year={2019}
}

@article{tang2020multi,
  title={Multi-channel attention selection gans for guided image-to-image translation},
  author={Tang, Hao and Xu, Dan and Yan, Yan and Corso, Jason J and Torr, Philip HS and Sebe, Nicu},
  journal={arXiv preprint arXiv:2002.01048},
  year={2020}
}
```

## Contributions
If you have any questions/comments/bug reports, feel free to open a github issue or pull a request or e-mail to the author Hao Tang ([bjdxtanghao@gmail.com](bjdxtanghao@gmail.com)).

## Collaborations
I'm always interested in meeting new people and hearing about potential collaborations. If you'd like to work together or get in contact with me, please email bjdxtanghao@gmail.com.
___
*If you want something you've never had, you must be willing to do something you've never done.*
