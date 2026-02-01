
# **📘** 

# **U-Net 핵심 맛보기 문제 5문항 (정답 제공 X)**

---

## **문제 1.**

  

U-Net이 semantic segmentation에서 뛰어난 성능을 보이는 가장 큰 이유는 무엇인가?

  

A. 매우 깊은 네트워크 구조로 인해 더 많은 파라미터를 가진다.
B. Encoder만 사용하여 global semantic 정보를 집중적으로 학습한다.
C. Contracting path와 Expanding path를 결합하여 local detail과 semantic 정보를 동시에 활용한다.
D. Fully connected layers를 여러 개 사용하여 global 정보를 극대화한다.

---

## **문제 2.**

  

U-Net의 “U”자 형태가 나타나는 이유와 가장 관련이 깊은 구조는 무엇인가?

  

A. Residual connection
B. Skip connection을 통한 encoder–decoder feature 결합
C. Dilated convolution
D. Bottleneck layer만 반복적으로 쌓기 때문

---

## **문제 3.**

  

U-Net의 skip connection이 FCN의 skip connection과 비교될 때 가지는 가장 큰 특징은 무엇인가?

  

A. FCN보다 더 강하게 encoder feature의 spatial resolution을 유지한 상태로 전달한다.
B. FCN에서는 skip connection이 없고, U-Net에서 처음 도입되었다.
C. U-Net에서는 skip connection이 오직 coarse feature만 전달한다.
D. U-Net의 skip connection은 convolution 대신 fully connected layer를 사용한다.

---

## **문제 4.**

  

U-Net의 Expanding path(upsampling path)의 주요 목적은 무엇인가?

  

A. 입력 이미지를 더 작은 공간으로 압축한다.
B. segmentation 결과를 classification task로 변환한다.
C. spatial resolution을 복원하며 encoder의 fine-grained feature와 결합한다.
D. feature map의 채널 수를 크게 증가시켜 overfitting을 방지한다.

---

## **문제 5.**

  

U-Net 구조에서 각 upsampling 단계가 encoder feature와 결합할 때 사용하는 방식으로 가장 적절한 것은?

  

A. 단순 평균 연산

B. Concatenation

C. Fully connected projection

D. Max pooling


[[문제 1~5 해설]]




# **U-Net 고난도 문제 6–10 (정답 제공 X)**

---

## **문제 6. (난이도 상)**

  

U-Net의 contracting path에서 **padding을 사용하지 않는(valid convolution)** 방식이 사용하는 가장 중요한 이유는 무엇인가?

  
A. feature map 크기를 유지하여 skip connection을 쉽게 만들기 위해
	-> valid conv는 오히려 feature를 줄이는 역할을 한다. 크기를 유지하려면 same padding을 사용해야한다.
B. receptive field를 더 크게 확보하기 위해
	-> receptive field는 conv 커널 크가와 depth에 의해 결정된다. valid conv 때문이 아니다.
C. upsampling 시 encoder와 decoder feature map의 spatial 크기를 정확히 맞추기 위해 cropping 과정이 필요하기 때문
	-> valid conv 때문에 encoder와 decoder가 항상 크기 불일치. 그래서 crop 후 concatenate한다.
D. pooling 이후 feature map을 자동으로 중앙 정렬하기 위해
	-> pooling은 단순 downsampling이며 central alignment 문제를 해결해주지 않는다.





---

## **문제 7. (난이도 상)**

  

U-Net 논문에서 제안된 **Overlap-tile Strategy**가 필요한 이유와 가장 직접적으로 관련된 문제는 무엇인가?

  

A. 네트워크가 very deep structure라서 gradient vanishing이 발생하기 때문
B. valid convolution으로 인해 output size가 input보다 작아지며, 타일 사이의 context가 손실되기 때문
C. pooling이 너무 많아 coarse feature만 남기 때문
D. GPU 메모리 절약을 위해 입력을 강제로 줄여야 하기 때문


---

## **문제 8. (난이도 상)**

  

U-Net에서 **mirroring extrapolation** 기법이 필요한 이유로 가장 적절한 설명은 무엇인가?

  

A. 입력 이미지 외곽의 픽셀들이 zero padding되면 boundary artifact가 커지기 때문에, 자연스러운 context를 제공하기 위함
B. pooling 경로에서 feature 수가 갑자기 줄어드는 것을 방지하기 위함
C. skip connection이 spatial alignment를 잃지 않게 하기 위함
D. encoder와 decoder의 feature 수 차이를 자동으로 보정하기 위함

---

## **문제 9. (난이도 상)**

  

U-Net의 upsampling 단계에서 **2×2 transposed convolution**이 수행하는 두 가지 기능 중 더 중요한 의미는 무엇인가?

  

A. spatial resolution 복원 + feature 수 증가
B. pooling 역연산 수행 + activation function 대체
C. resolution 확장 + 채널 수 절반 감소
D. convolution을 두 번 적용한 것과 동일한 receptive field 유지

---

## **문제 10. (난이도 상)**

  

U-Net에서 skip connection을 수행할 때, **encoder feature를 crop**해야 하는 이유는 무엇인가?

  

A. valid convolution 때문에 encoder feature map 크기가 decoder feature map보다 작아서
B. decoder feature가 dilated convolution을 사용하여 더 큰 receptive field를 가지기 때문에
C. encoder feature가 decoder feature보다 spatial size가 크기 때문에 alignment를 맞춰야 해서
D. pooling의 stride가 변하기 때문에 encoder와 decoder의 output size가 불규칙해져서
