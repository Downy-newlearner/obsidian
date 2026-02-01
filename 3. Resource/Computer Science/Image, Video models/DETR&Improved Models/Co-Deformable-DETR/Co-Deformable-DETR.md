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


- libGL.so.1 패키지 문제 해결
	- 현재 경로에 해당 패키지 다운로드
		```apt download libgl1-mesa-glx```
	- .deb 파일로 다운로드 되니 압축 해제
		```
		ar x libgl1-mesa-glx*.deb 
		tar -xvf data.tar.* 
		```
	- 홈 디렉토리에 복사
		```
		mkdir -p ~/local_libs
		cp ./usr/lib/x86_64-linux-gnu/libGL.so.1 ~/local_libs/
		```
	- 환경 변수 설정
		```export LD_LIBRARY_PATH=$HOME/local_libs:$LD_LIBRARY_PATH```

- mmdet 모듈이 없다는 에러 해결
	- (real_coenv) jdh251425@mlpa-titanx4:~/co-deformable-detr/mmdet$ export PYTHONPATH=$(pwd):$PYTHONPATH
	- mmdet 폴더로 이동해서 파이썬 경로 추가하면 된다.




export LD_LIBRARY_PATH=$HOME/local_libs:$LD_LIBRARY_PATH
find / -name "libGLdispatch.so.0" 2>/dev/null
echo 'export LD_LIBRARY_PATH=/home/jdh251425/miniconda3/pkgs/libglvnd-1.7.0-ha4b6fd6_2/lib/:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
cd mmdet/
export PYTHONPATH=$(pwd):$PYTHONPATH
cd ..


export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:64
nohup bash tools/dist_train.sh projects/configs/co_deformable_detr/co_deformable_detr_r50_1x_coco.py 4 path_to_exp > nohup_241230.out & 