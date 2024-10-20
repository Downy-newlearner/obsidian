### 텍스트-투-이미지 실행 방법
Stable Diffusion 2는 CLIP ViT-H/14 텍스트 인코더의 펜얼티밋 텍스트 임베딩에 조건화된 latent diffusion 모델입니다. 텍스트-투-이미지를 실행하기 위한 가이드는 다음과 같습니다.
### 1. 모델 가중치 다운로드
우선, 필요한 모델 가중치를 Hugging Face에서 다운로드해야 합니다:
- _[SD2.1-v](https://huggingface.co/stabilityai/stable-diffusion-2-1)_ [모델 가중치](https://huggingface.co/stabilityai/stable-diffusion-2-1)
- _[SD2.1-base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)_ [모델 가중치](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)
### 2. 모델 샘플링 실행
- **SD2.1-v 모델에서 샘플링하기**
```Shell
python scripts/txt2img.py --prompt "a professional photograph of an astronaut riding a horse" --ckpt "C:\Projects\stablediffusion\checkpoints\v2-1_768-ema-pruned.ckpt" --config configs/stable-diffusion/v2-inference-v.yaml --H 768 --W 768
```
- **기본 모델에서 샘플링하기**
```Shell
python scripts/txt2img.py --prompt "a professional photograph of an astronaut riding a horse" --ckpt <path/to/model.ckpt/> --config <path/to/config.yaml/>
```
### 3. 기타 사항
- 기본적으로 DDIM 샘플러를 사용하여 768x768 크기의 이미지를 50 스텝으로 생성합니다.
- v 모델은 더 높은 가이드 스케일로 샘플링할 수 있습니다.
### 4. Intel® Extension for PyTorch* 최적화
Intel CPU에서 실행할 경우, TorchScript와 Intel® Extension for PyTorch* 최적화를 활용할 수 있습니다. 다음과 같이 설치해야 합니다:
**필요한 라이브러리 설치**
```Shell
apt-get install numactl libjemalloc-dev
pip install intel-openmp
pip install intel_extension_for_pytorch -f <https://software.intel.com/ipex-whl-stable>
```
**최적화된 샘플링 명령어**
- **SD2.1-v 모델로 TorchScript + IPEX 최적화를 사용하여 샘플링하기**
```Shell
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt "a corgi is playing guitar, oil on canvas" --ckpt <path/to/768model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-v-fp32.yaml --H 768 --W 768 --precision full --device cpu --torchscript --ipex
```
- **기본 모델로 IPEX 최적화를 사용하여 샘플링하기**
```Shell
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt "a corgi is playing guitar, oil on canvas" --ckpt <path/to/model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-fp32.yaml --n_samples 1 --n_iter 4 --precision full --device cpu --torchscript --ipex
```
**bfloat16 지원 CPU 사용 시 샘플링**
- **SD2.1-v 모델**
```Shell
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt "a corgi is playing guitar, oil on canvas" --ckpt <path/to/768model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-v-bf16.yaml --H 768 --W 768 --precision full --device cpu --torchscript --ipex --bf16
```
- **SD2.1-base 모델**
```Shell
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt "a corgi is playing guitar, oil on canvas" --ckpt <path/to/model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-bf16.yaml --precision full --device cpu --torchscript --ipex --bf16
```
이와 같은 방법으로 텍스트-투-이미지 기능을 실행할 수 있습니다. 각 명령어에서 `<path/to/...>`는 실제 모델 가중치 파일의 경로로 대체해야 합니다.