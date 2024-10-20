---
태그:
  - CV
  - Image Generation
---
#### 딥러닝&파이썬 용어 정리
|이름|설명|
|---|---|
|[[모델 샘플링]]|딥러닝 등의 모델을 다룰 때, 샘플링은 주어진 확률 분포에서 값을 추출하는 과정이다.|
|[[데이터 샘플링]]|전체 데이터 세트에서 샘플(일부) 데이터를 선택하는 과정이다.|
|[[checkpoint]]|학습된 모델을 저장하는 기능이다. 체크포인트는 모델의 일관성을 유지하고, 실험의 재현성을 보장하는 데 도움을 준다.|
|[[LoRA]]|Low-Rank Adaptation. 모델을 세부 조정하기 위한 학습 기법이다.|
  
  
[[디렉토리]]
image to image
**StableDiffusionImg2ImgPipeline(huggingface)** [https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/img2img](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/img2img)
LoRA
전반적인 ldm(latent diffusion model) 구조
[https://www.youtube.com/watch?v=nthpXARTduk](https://www.youtube.com/watch?v=nthpXARTduk)
[[정리]]
  
### txt2img
[[txt2img(README)]]
[[Error Summary]]
  
### img2img
[[arguments]]
[[Error Summary 2]]
python scripts/img2img.py --prompt "emoji, especially that of apple" --init-img "C:\Projects\apple000.jpg" --outdir "C:\Projects\stablediffusion\output_img" --ckpt "C:\Projects\stablediffusion\checkpoints\sd21-unclip-l.ckpt
  
python scripts/img2img.py --prompt "make it cute animation style" --init-img "C:\Projects\BROW7777.jpg" --outdir "C:\Projects\stablediffusion\output_img" --ckpt "C:\Projects\stablediffusion\checkpoints\sd21-unclip-l.ckpt"