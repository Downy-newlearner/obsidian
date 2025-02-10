---
created: 2024-11-16
tags: 
aliases:
  - ldm
---
## Latent Diffusion을 이루는 요소
![[Pasted image 20241116172700.png]]

### 1. Text Encoder
- Latent Diffusion의 동작은 다음과 같다.
	- prompt 텍스트를 입력 -> 텍스트에 맞는 이미지를 출력
- 이를 수행하기 위해, Latent Diffuion 모델의 *CLIP* 이라는 Text Encoder가 필요하다. 
	- 모델은 영어와 같은 언어를 이해할 수 없기 때문에 필요. 

- Text Encoder는 *Tokenizer*를 이용해서 다음 작업을 수행한다.
	- 문장에서 단어를 추출 -> 숫자로 변환(Tokenize) -> 숫자를 텍스트 임베딩(text embedding)으로 만듦.
	- 텍스트 임베딩은 latent vector의 형태이다.

- text embedding으로 변환하는 이 과정을 거쳐야 비로소 text가 이미지를 생성하는 Unet에 Conditioning을 할 수 있게 되기 때문이다. (Unet과 Conditioning에 대해서는 다음 섹션에서 설명한다.)

### 2. Unet
![[Pasted image 20241118130813.png]]
먼저 간략하게 설명하자면, Text Encoder에서 만들어진 embedding 은 U-net으로 전달된다. U-net 에서는 text embedding에 따라 [[조건화(Conditioning)]]된 채로 random latent vector를 n번 반복하여 denoise 하는 과정을 거치게 된다. 바로 여기서 랜덤한 노이즈에서 이미지를 생성하는 부분이 초반부에 설명했던 Diffusion 모델의 원리이다. 

그리고 이 모델은 text embedding에 의하여 조건화 되었기 때문에 텍스트로 우리가 원하는 내용을 입력하여 이미지를 출력할 수 있는 것이다. 이 조건화 과정은 attention 등의 방법을 사용하여 매우 복잡한 과정을 거쳐서 이루어진다.

또, 위에서 random latent vector를 n번 반복하여 denoise 한다고 했는데, 이때 반복전에 어떤 방식(노이즈의 세기, 종류, 확률 편미분 방정식 이용 등)으로 처리하고 반복하느냐를 결정하는 것이 바로 scheduler의 역할이다. scheduler의 종류로는 여러가지가 있는데 DDPM, DDIM, PNDM, Euler, Euler a, DPM++ 등이 있다.  Stable diffusion을 직접 사용해본 사람이면 많이 봤을법한 스케줄러(샘플러)들이다. 스케줄러의 정확한 작동방식은 너무 다양하고 어려우므로 이 글에서는 생략하도록 하겠다.

그래서 위 과정을 전부 거치고 나면 저해상도의(위 예제에서는 64x64) latent vector 값이 생성되게 된다. 이 값은 마지막으로 VAE로 전달되게 된다.

U-net의 세부적인 원리는 이 글이 설명하고자 하는 범위를 넘어서므로 생략하겠다.

출처: [https://pitas.tistory.com/9](https://pitas.tistory.com/9) [Programming, IT, Algorithm, Security:티스토리]
