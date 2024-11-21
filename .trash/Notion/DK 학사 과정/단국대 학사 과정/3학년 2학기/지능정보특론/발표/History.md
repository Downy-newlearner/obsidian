역대 대표 이미지 생성형 모델
|   |   |
|---|---|
|시기|모델명|
|2013|VAE, GAN|
|2021|DALL-E, CLIP|
|2022|Stable Diffusion & Midjourney|
GAN → DCGAN, Pix2Pix(Conditional GAN), CycleGAN, StyleGAN
DDPM → DDIM, Score-Based Diffusion, Stable Diffusion
  
현재 미드저니와 쌍벽을 이루는 Stable Diffusion은 DDPM의 뿌리를 두고 있어서 DDPM을 이해할 필요가 있습니다.
그래서 오늘 발표의 주제인 Denoising Diffusion Probablistic Model에 대해서 설명하겠습니다.
  
## GAN, VAE가 대체된 이유
1. GAN과 VAE는 한때 이미지 생성 분야에서 주류 모델이었으나, 그 훈련의 불안정성 및 생성 품질의 한계로 점점 덜 사용되게 되었다.
2. GAN은 모드 붕괴 문제로 인해 다양성 부족에 시달렸고, VAE는 블러링 현상으로 고해상도 이미지 생성에 한계가 있었다.
3. 최근 Diffusion 모델이 등장하면서 고품질의 사실적인 이미지를 안정적으로 생성할 수 있게 되어 주목받고 있다.
4. 새로운 모델들은 조건부 생성에 있어서도 우수한 성능을 보이며, 사용의 용이성을 향상시켰다.
5. 인공지능 및 머신러닝 분야의 연구가 지속적으로 발전함에 따라, GAN과 VAE는 보조적인 역할로 전환되고 있다.
  
## DALL-E, CLIP
둘 다 transformer 아키텍처를 가지고있다.
최신 아키텍처에 비해 고해상도 이미지를 만들지 못하거나 창의적, 예술적인 이미지를 만들지 못한다는 평가를 받으면서 대체까진 아니어도 특정 용도로만 사용되는 모델이 되었다.