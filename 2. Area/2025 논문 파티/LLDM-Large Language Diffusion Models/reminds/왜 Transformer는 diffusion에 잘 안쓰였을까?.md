- Transformer는 NLP에서는 성공했지만, diffusion에서는 거의 안 쓰였음.
    
- 이유:
    
    - 이미지는 공간 구조(locality)가 강한데, Transformer는 전역 self-attention을 쓰므로 계산량이 많고 효율이 떨어짐
        
    - 기존 diffusion 모델은 U-Net이라는 이미지 친화적인 구조를 사용해왔음.