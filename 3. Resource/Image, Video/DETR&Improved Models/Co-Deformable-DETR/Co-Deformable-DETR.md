---
created: 2024-12-29
tags:
  - Terminology
aliases: 
reference: https://dohyeon.tistory.com/105
github: https://github.com/Sense-X/Co-DETR
---
## 환경 세팅
- *MMDetection V2.25.3* / *MMCV V1.5.0.* 이 필요하다.
	- MMDetection은 repo에 이미 포함되어있으니 MMCV만 준비하면 된다.

- 필요한 세팅
	- python=3.7.11,
	- pytorch=1.11.0,
	- cuda=11.3
	- MMCV V1.5.0
		- Pytorch가 먼저 설치되어있어야함.
		- **Note**: mmcv-full is only compiled on PyTorch 1.x.0 because the compatibility usually holds between 1.x.0 and 1.x.1. If your PyTorch version is 1.x.1, you can install mmcv-full compiled with PyTorch 1.x.0 and it usually works well. For example, if your PyTorch version is 1.8.1 and CUDA version is 11.1, you can use the following command to install mmcv-full.

conda install pytorch==1.11 torchvision torchaudio cudatoolkit=11.5 -c pytorch
pip install mmcv-full==1.5.0 -f https://download.openmmlab.com/mmcv/dist/cu115/torch1.11.0/index.html



pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8.0/index.html