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
- 이를 수행하기 위해, Latent Diffuion 모델의 CLIP 이라는 Text Encoder가 필요하다. 
	- 모델은 영어와 같은 언어를 이해할 수 없기 때문에 Text Encoder가 필요한것이다. 
- Text Encoder는 Tokenizer를 이용해서 문장에서 단어를 추출하여 숫자로 변환하고(이 과정을 tokenize 라고도 한다), 이 숫자를 latent vector의 형태인 text embedding로 만든다. 
- text embedding으로 변환하는 이 과정을 거쳐야 비로소 text가 이미지를 생성하는 Unet에 Conditioning을 할 수 있게 되기 때문이다. (Unet과 Conditioning에 대해서는 다음 섹션에서 설명한다.)
