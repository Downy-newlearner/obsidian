---
태그:
  - CV
  - Image Generation
---
#### 딥러닝&파이썬 용어 정리
|책 이름|챕터/날짜|이름|설명|
|---|---|---|---|
|독학|turtle 사용해보기|[[Latent space]]|한국어로는 해공간, 잠재공간 이라고 부른다. 이미지들이 Convolution Layers를 거쳐 나온 feature vector들의 공간을 Latent space라고 부른다. 좋은 latent space가 형성되었다면(개, 고양이 이미지들의 feature vector들이 섞이지 않고 경계가 명확함) 뒤에 연결된 fully connected layer들은 클래스들을 쉽게 구분할 것이다.|
|독학|turtle 사용해보기|[[Fully Connected Layers]]|feature vector가 입력으로 들어가고 예측값이 출력으로 나온다. 예를 들어 강아지와 고양이 이미지를 구별하는 모델이라면 예측값은 강아지 또는 고양이가 될 것이다.|
|독학|turtle 사용해보기|[[Convolution Layers = Feature Extractor = Encoder]]|이들은 서로 같은 의미이다. 이들은 입력으로부터 유용한 feature를 뽑아내는 역할을 한다. 뽑아낸 정보를 feature vector라고 부른다.|
|독학|turtle 사용해보기|[[차원 축소]]|n차원 벡터는 있는 그대로서 시각화하기가 불가능한데, 이런 n차원 벡터들을 2차원으로 시각화하는 방법이다.|
|독학|turtle 사용해보기|[[Feature Vector]]|이미지 하나를 하나의 n차원 벡터로 표현하곤 하는데, 이 n차원 벡터를 Feature Vector라고 부른다.(Encoder의 출력이 feature vector이다. 입력은 이미지이다.) feature vector는 fully connected layers의 입력으로 들어간다.|
|독학|turtle 사용해보기|[[representation]]|딥러닝에서 representation은 말 그대로 ‘표현’을 의미한다. 딥러닝 모델이 이미지를 표현하는, 즉 representation하는 방법으로는 Feature Vector가 있다.|
|독학|turtle 사용해보기|[[cifar100 데이터셋]]|컴퓨터 비전 분야에서 널리 사용되는 데이터셋 중 하나이다. 비행기 사진들이 포함되어있는 데이터셋이다.|
|독학|turtle 사용해보기|[[dinov2]]|이미지 인식, 객체 탐지, 이미지 분류 등 다양한 작업에서 뛰어난 성능을 발휘하는 Meta의 딥러닝 모델이다.|
|독학|turtle 사용해보기|[[clipvitL14]]|Clip Vit L14. CLIP(Contrastive Language–Image Pretraining)은 텍스트와 이미지를 동시에 학습하여 텍스트 설명과 이미지 간의 연관성을 이해할 수 있도록 설계된 모델이다. Vit는 비전 트랜스포머를 의미한다. L14는 레이어 수가 14개임을 의미한다. clip, vit는 각각 딥러닝 모델을 의미한다.|
|독학|Diffusion Model|[[결합 분포(joint distribution)]]|두 개 이상의 확률 변수의 분포를 나타내는 개념으로, 여러 확률 변수가 동시에 어떤 값을 가질 확률을 설명한다.|
|독학|Diffusion Model|[[이미지가 가우시안 분포를 따른다는 것은]]|각 픽셀은 R, G, B 값으로 각각 0~255 사이의 값을 갖는다. 이 때 R, G, B 각각을 서로 독립적으로 보아 모든 픽셀의 R 값이 가우시안 분포를 따르고, G값, B값도 가우시안 분포를 따른다는 것이다.|
|독학|Diffusion Model|[[variational inference(변분 추론)]]|이후 타임스텝으로 근사하기 위해 사용하는 베이지 추론 기법 중 하나로, 효율적이고 실용적이라는 특징이 있다. 후방 분포를 직접 계산하는 것이 아니라 그저 후방분포를 근사하는 간단한 분포를 설정한다는 아이디어를 통해 효율성과 실용성을 챙기는 것이다.|
|독학|Diffusion Model|[[parameterized Markov chain]]|마르코프 체인의 전이 확률이 특정한 매개변수들에 의해 조정되고 결정된다는 것을 의미한다. 그리고 이 매개변수들은 모델의 훈련 과정에서 최적화된다.|
|독학|Diffusion Model|[[Conditional]]|“Conditional”이라는 용어가 붙은 이미지 생성형 모델 아키텍처는 특정 조건이나 입력에 따라 생성할 결과물이 결정된다는 의미이다.|
|독학|Diffusion Model|[[Objective function, Cost function]]|목적 함수, 최적화 문제에서 변수가 최소화 또는 최대화해야 하는 함수이다. 일례로 경사 하강법의 대상이 목적 함수인 것이다.|
|독학|Diffusion Model|[[브이랩]]|Virtual Lab 가상환경에서 실험을 수행할 수 있도록 도와주는 시스템|
|독학|Diffusion Model|[[robust learning]]|다양한 환경이나 조건에서도 강력한 성능을 유지할 수 있도록 모델을 학습하는 방법. 데이터의 노이즈, 잡음, 이상치에 대한 강인성을 강조하며 이런 불확실성에서도 안정적이고 신뢰성 있는 예측 모델을 만드는 것이 목표인 학습 방법이다.|
|독학|Diffusion Model|[[Noise Scheduler]]|Diffusion Process에서 노이즈가 추가되는 정도를 조절한다. 예시로 linuer noise scheduler는 시간이 지날 수록 더 많은 노이즈가 추가되도록 한다.|
|독학|Diffusion Model|[[Markov chain]]|각 전이의 단계는 현재 상태에만 의존한다는 메모리리스 속성을 가진다. 즉 현재 데이터 포인트(상태)에서 노이즈를 추가하여 다음 데이터 포인트(다음 상태)가 생성된다. 이 과정은 여러 단계에 걸쳐 진행되며, 각 단계가 가우시안 전이로 이루어지게 된다.|
|독학|Diffusion Model|[[Gaussian transition]]|Diffusion model에서 데이터의 변환 과정이 가우시안(정규) 분포를 따르는 것과 관련이 있습니다. 확산 모델은 노이즈를 점진적으로 추가하거나 제거하여 데이터를 생성합니다. 이 과정에서 각 단계는 가우시안 분포를 통해 정의된 전이 과정을 따릅니다.|
|독학|Diffusion Model|[[Diffusion Model]]|주로 데이터를 생성하거나 모사하는 데 사용되는 수학적 또는 컴퓨터 과학적 모델을 의미한다. 이 모델은 확산의 원리를 기반으로 하여, 데이터를 점진적으로 "노이즈"와 함께 변화시키고, 그 과정을 역으로 수행하여 원래 데이터를 복원하거나 새로운 데이터를 생성하는 데 사용된다.|
|독학|Diffusion Model|[[deep generative model]]||
|독학|Stable Diffusion Models|[[모델 샘플링]]|딥러닝 등의 모델을 다룰 때, 샘플링은 주어진 확률 분포에서 값을 추출하는 과정이다.|
|독학|Stable Diffusion Models|[[데이터 샘플링]]|전체 데이터 세트에서 샘플(일부) 데이터를 선택하는 과정이다.|
|독학|Stable Diffusion Models|[[checkpoint]]|학습된 모델을 저장하는 기능이다. 체크포인트는 모델의 일관성을 유지하고, 실험의 재현성을 보장하는 데 도움을 준다.|
|독학|Stable Diffusion Models|[[LoRA]]|Low-Rank Adaptation. 모델을 세부 조정하기 위한 학습 기법이다.|
  
  
Diffusion models([https://www.youtube.com/watch?v=uFoGaIVHfoE](https://www.youtube.com/watch?v=uFoGaIVHfoE))
AE
VAE
KL-Divergence([https://hyunw.kim/blog/2017/10/27/KL_divergence.html](https://hyunw.kim/blog/2017/10/27/KL_divergence.html))
Cross Entrophy
Entrophy([https://hyunw.kim/blog/2017/10/14/Entropy.html](https://hyunw.kim/blog/2017/10/14/Entropy.html))