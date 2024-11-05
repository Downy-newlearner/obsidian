Progressive Growing of Generative Adversarial Networks
이미지의 해상도를 저해상도부터 고해상도까지 차례로 학습시키는 것이 핵심 특징이다.

생성자: 해상도를 늘려가면서 학습
판별자: 해상도를 줄여가면서 학습

고해상도

## 생성자 & 판별자의 기본 작동 구조
![[Pasted image 20241105124130.png]]
### 생성자


![[Pasted image 20241105124545.png]]
$\alpha$값은 0에서 1로 점차 커져서 새로운 toRGB 이미지의 비중이 높아진다.

