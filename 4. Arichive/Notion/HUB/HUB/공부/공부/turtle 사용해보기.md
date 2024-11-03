---
태그:
  - CV
설명: 이미지 클러스터링 모델
---
## 용어
|   |   |
|---|---|
|clipvitL14|Clip Vit L14. CLIP(Contrastive Language–Image Pretraining)은 텍스트와 이미지를 동시에 학습하여 텍스트 설명과 이미지 간의 연관성을 이해할 수 있도록 설계된 모델이다. Vit는 비전 트랜스포머를 의미한다. L14는 레이어 수가 14개임을 의미한다. clip, vit는 각각 딥러닝 모델을 의미한다.|
|dinov2|이미지 인식, 객체 탐지, 이미지 분류 등 다양한 작업에서 뛰어난 성능을 발휘하는 Meta의 딥러닝 모델이다.|
|cifar100 데이터셋||
#### 딥러닝&파이썬 용어 정리
|책 이름|챕터/날짜|이름|설명|
|---|---|---|---|
|독학|turtle 사용해보기|[[clipvitL14]]|Clip Vit L14. CLIP(Contrastive Language–Image Pretraining)은 텍스트와 이미지를 동시에 학습하여 텍스트 설명과 이미지 간의 연관성을 이해할 수 있도록 설계된 모델이다. Vit는 비전 트랜스포머를 의미한다. L14는 레이어 수가 14개임을 의미한다. clip, vit는 각각 딥러닝 모델을 의미한다.|
|독학|turtle 사용해보기|[[dinov2]]|이미지 인식, 객체 탐지, 이미지 분류 등 다양한 작업에서 뛰어난 성능을 발휘하는 Meta의 딥러닝 모델이다.|
|독학|turtle 사용해보기|[[cifar100 데이터셋]]|컴퓨터 비전 분야에서 널리 사용되는 데이터셋 중 하나이다. 비행기 사진들이 포함되어있는 데이터셋이다.|
|독학|turtle 사용해보기|[[representation]]|딥러닝에서 representation은 말 그대로 ‘표현’을 의미한다. 딥러닝 모델이 이미지를 표현하는, 즉 representation하는 방법으로는 Feature Vector가 있다.|
|독학|turtle 사용해보기|[[Feature Vector]]|이미지 하나를 하나의 n차원 벡터로 표현하곤 하는데, 이 n차원 벡터를 Feature Vector라고 부른다.(Encoder의 출력이 feature vector이다. 입력은 이미지이다.) feature vector는 fully connected layers의 입력으로 들어간다.|
|독학|turtle 사용해보기|[[차원 축소]]|n차원 벡터는 있는 그대로서 시각화하기가 불가능한데, 이런 n차원 벡터들을 2차원으로 시각화하는 방법이다.|
|독학|turtle 사용해보기|[[Convolution Layers = Feature Extractor = Encoder]]|이들은 서로 같은 의미이다. 이들은 입력으로부터 유용한 feature를 뽑아내는 역할을 한다. 뽑아낸 정보를 feature vector라고 부른다.|
|독학|turtle 사용해보기|[[Fully Connected Layers]]|feature vector가 입력으로 들어가고 예측값이 출력으로 나온다. 예를 들어 강아지와 고양이 이미지를 구별하는 모델이라면 예측값은 강아지 또는 고양이가 될 것이다.|
|독학|turtle 사용해보기|[[Latent space]]|한국어로는 해공간, 잠재공간 이라고 부른다. 이미지들이 Convolution Layers를 거쳐 나온 feature vector들의 공간을 Latent space라고 부른다. 좋은 latent space가 형성되었다면(개, 고양이 이미지들의 feature vector들이 섞이지 않고 경계가 명확함) 뒤에 연결된 fully connected layer들은 클래스들을 쉽게 구분할 것이다.|
  
  
[https://unist.tistory.com/4](https://unist.tistory.com/4)
![[img1.daumcdn.png]]
  
![[img1.daumcdn 1.png]]
나쁜 Latent space와 좋은 Latent space