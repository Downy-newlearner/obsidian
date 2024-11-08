![[%E3%80%8EMachine_Learning_%EA%B0%9C%EB%A1%A0%E3%80%8F_%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C_Download.pdf]]
## **Part 1. Introduction to Machine Learning**
기계학습의 명확한 정의, 대표적인 문제들에 대해 살펴본다.
  
기계학습은 알고리즘을 설계한다.
![[Source/Untitled 93.png|Untitled 93.png]]
  
  
![[image-1(Powered_by_MaxAI).jpeg]]
![[image-2(Powered_by_MaxAI).jpeg]]
![[image-3(Powered_by_MaxAI).jpeg]]
경험을 통해서 성능을 높이는 시스템을 학습이라고 한다.
기계학습은 직접적으로 프로그래밍하지 않고 컴퓨터가 스스로 학습하도록 하는 분야이다.
![[image-4(Powered_by_MaxAI).jpeg]]
T, P, E가 완벽히 정의되어야 올바른 기계학습을 진행할 수 있다.
E를 통해서 T에 대한 P를 개선한다.
![[image-5(Powered_by_MaxAI).jpeg]]
전통적인 프로그래밍과 기계학습의 비교.
기계학습에서의 인풋은 데이터와 아웃풋을 준다. 그렇게 한다면 우리가 큰 틀에서 짜놓은 프로그램이 디테일하게 수정되어 완성된 프로그램이 나오게 된다.
![[image-6(Powered_by_MaxAI).jpeg]]
![[image-7(Powered_by_MaxAI).jpeg]]
Generalization(일반화)는 기계학습의 가장 큰 목표이다.
3살 아이가 여러 종류의 나무를 보고, 그들의 similarity(유사성)을 파악해 프로토타입, 즉 일반화된 개념을 만들어 새로운 나무를 보아도 나무임과 아님을 구분할 수 있게된다.
만약 일반화가 잘 된다면 나무에 대한 이미지를 생성할 수도 있을 것이다.
![[image-8(Powered_by_MaxAI).jpeg]]
특정 기계학습 알고리즘이 모든 데이터셋에 대해서 항상 성능이 좋을 수는 없다.
![[image-9(Powered_by_MaxAI).jpeg]]
지도학습, 비지도학습, 준지도학습, 강화학습
![[image-10(Powered_by_MaxAI).jpeg]]
![[image-11(Powered_by_MaxAI).jpeg]]
데이터로 x만 주고 어떻게 하라는지 알려주지 않는다.
성능에 대해 크게 기대할 수 없다.
![[image-12(Powered_by_MaxAI).jpeg]]
학습데이터를 줄 때, 몇몇 데이터는 (x,y)를 몇몇 데이터는 x만 준다.
데이터 라벨링을 모든 데이터에 대해서 진행하기가 어려우므로 일부만 해서 학습하는 것이다.
![[image-13(Powered_by_MaxAI).jpeg]]
준지도학습은 레이블이 없는 데이터에 대해서도 상대적으로 정확한 Decision boundary를 구할 수 있다는 장점이 있다.
![[image-14(Powered_by_MaxAI).jpeg]]
환경과 상호작용한다.
환경의 상태와, 보상을 통해 상호작용한다.
그럼으로써 알고리즘이 스스로 배우도록한다.
리워드는 즉시 주어지지 않을 수 있다.
이 경우 State만 즉시 주어진다.
이것이 강화학습이 어려운 이유이다.
![[image-15(Powered_by_MaxAI).jpeg]]
아래 책들이 기계학습을 심도있게 공부할 수 있도록 해주는 책들이다.
  
## Part 2. Bias and Variance
![[image-16(Powered_by_MaxAI).jpeg]]
편향과 분산
이 챕터를 통해 어떤 기계학습 모델을 선택하는 방법을 배운다.(Bias, Variance, Overfitting, Underfitting과 관련이 있다.)
![[image-17(Powered_by_MaxAI).jpeg]]
우선 모델 클래스를 정해야한다.
이후 학습을 통해 모델의 파라미터를 결정한다.(w, b)
잘 동작한다는 것이 무엇인가?
Loss function을 기준으로 판단한다.
모델의 정답값과 예측값의 차이가 클 수록 손실함수에 큰 값을 준다.
![[image-18(Powered_by_MaxAI).jpeg]]
![[image-19(Powered_by_MaxAI).jpeg]]
기계학습에서 일반화란, ML 모델의 능력이다.
사실 우리가 하는 것은 학습 데이터에 대해서 처리를 잘 할 수 있도록 제공을 하는데, 우리가 기대하는 것은 모든 데이터에 대해서 잘 처리하기이다.(모순이 존재)
왼쪽은 학습 데이터의 소소한 디테일을 모두 반영하려고 노력한 것을 확인할 수 있고, 오른쪽은 학습 데이터를 smooth하게 반영하여 테스트 데이터를 잘 처리함을 확인할 수 있다.
학습 에러 관점에서는 왼쪽이 좋지만, 일반화능력은 오른쪽이 좋다.
![[image-20(Powered_by_MaxAI).jpeg]]
![[image-21(Powered_by_MaxAI).jpeg]]
True distribution는 가능한 모든 케이스이다.
Train set은 True distribution에서 발생한 것이다.
  
iid는 independent and identIcally distributed이다.
확률 변수나 데이터포인트들이 서로 독립적이며 동일한 확률 분포를 따른다는 가정을 나타낸다.
![[image-22(Powered_by_MaxAI).jpeg]]
E는 Expactation이다.
분포를 가지는 값을 하나의 숫자로 요약한 것이다.
loss를 하나의 숫자로 요약
![[Source/Untitled 1 63.png|Untitled 1 63.png]]
위 수식의 의미는 다음과 같다.
x와 y가 P(true distribution)을 따른다고 할 때, 구한 loss의 평균값 또는 기댓값.
![[image-23(Powered_by_MaxAI).jpeg]]
|   |   |   |
|---|---|---|
||모델 복잡도 높음|모델 복잡도 낮음|
||overfitting 가능성 증가|overfitting 가능성 감소|
||underfitting 가능성 감소|underfitting 가능성 증가|
적당한 복잡도를 가지는 모델을 사용하는 것이 중요하다.
![[image-24(Powered_by_MaxAI).jpeg]]
오컴의 면도날
인색함에 대한 원칙
현상을 설명할 수 있는 모델이 여러개 있다면, 가장 단순한 모델이 가장 좋을 확률이 좋더라~~
박스가 한 개일 확률이 높더라.
왜냐하면 두 개라면 박스가 마침 적당한 거리를 두고 존재하고, 마침 얇은 나무 밑동으로 가려져야한다.
복잡한 상황이 맞을 확률은 단순한 상황이 맞을 확률보다 낮다.
![[image-25(Powered_by_MaxAI).jpeg]]
모델의 capacity를 높일 수록 트레인 에러는 줄어든다.
하지만 목표는 일반화 에러를 줄이는 것이므로, 적당한 지점을 찾는 것이 목표이다.
![[image-26(Powered_by_MaxAI).jpeg]]
특정 솔루션에 대한 preferrence이다.
학습 과정에 최적화 문제를 푸는데 이를 위해서는 목적함수가 필요하다
목적함수는 로스 함수를 정의해서 이것이 최소가 되도록 하는 것이다.
만약 학습 로스만 쓴다고 한다면, 과적합에 빠질 수 있어서 어떤 텀을 추가하는데 그 텀이 정규화 텀이다.
정규화는 순전히 우리의 믿음이다.
모델의 capacity가 커질수록 값이 커지는 정규화 텀을 사용하여 결국에는 로스만 최소화하는 것이 아니라 모델의 capacity도 최소화 할 수 있도록 목적 함수를 구성할 수 있다.
많은 경우 목적함수에는 2가지의 텀이 있고 이 두 텀은 각기 다른 곳으로 유래되므로, 하이퍼파라미터라는 것을 준다.
하이퍼파라미터는 개발자가 제공해야하는 변수이다.(람다)
파라미터는 단순히 학습을 통해 배우는 변수
람다가 작으면 첫번째 텀(항)을 더 고려, 람다가 크면 두번째 텀을 더 고려한다는 뜻이다.
하이퍼파라미터 튜닝은 교차검증이라는 과정을 통한다.
정규화는 training error를 낮춘다는 목표가 아니다. 만약 training error만 고려한다면 두번째 텀은 필요가 없을 것이다.
![[image-27(Powered_by_MaxAI).jpeg]]
각 그림 설명
1. 람다를 매우 크게 주어, 정규화에 과도하게 집중
2. 람다를 적절히 주어 모든 데이터에 적절히 fitting되고, 정규화도 적당히 잘 된 모델
3. 람다를 매우 작게 줌 → 오버피팅(training error에만 집중)
![[image-28(Powered_by_MaxAI).jpeg]]
편향과 분산은 오버피팅, 언더피팅과 매우 밀접한 개념이다.
이를 가장 쉽게 이해할 수 있는 방법인 과녁문제이다.
양궁을 잘하려면, 영점이 잘 맞아야하고, 이 영점이 쏠 때마다 변동이 있으면 안된다.
왼쪽 아래 그림 : 안정적이지만 영점이 안 맞은 경우
오른쪽 위 : 영점은 맞지만, 안정화가 덜 되서 쏠 때마다 왔다갔다한다.
오른쪽 아래 : 영점, 안정화 둘 다 안된 상태
  
편향은 예측의 평균값과 True 값의 차이이다.
분산은 True값을 알 필요가 없다.
예측의 평균값을 구한 후 각 예측과의 거리를 구해서 제곱한다.
$V = E[(X-\mu)]$
테스트 에러를 낮추려면 편향과 분산을 낮춰야한다.
하지만 Bias와 Variance 사이에는 Trade off가 존재한다.
![[image-29(Powered_by_MaxAI).jpeg]]
편향과 분산을 모두 낮추기 위한 노력 중 하나가 앙상블 기법이다.
![[image-30(Powered_by_MaxAI).jpeg]]
분산을 낮추기 위한 가장 좋은 방법은 학습 데이터가 많은 것이다.
편향을 줄이기 위해서는 모델 복잡도를 높일 필요가 있다, 하지만 그렇게 한다면 분산이 높아질 우려가 있다.
  
## Part 3. Recent Progress of Large Language Models
![[image-31(Powered_by_MaxAI).jpeg]]
![[image-32(Powered_by_MaxAI).jpeg]]
General Purpopse Algorithm이다.
![[image-33(Powered_by_MaxAI).jpeg]]
GPT 3.5
GPT 3는 사용자의 언어는 이해를 했지만 지시를 잘 이행하지는 못했다. GPT3.5에서는 지시를 안전하게 잘 이행한다. 이것을 InstructGPT라고 한다.
![[image-34(Powered_by_MaxAI).jpeg]]
강화학습을 통해 InstructGPT를 만들어낸 것이다.
![[image-35(Powered_by_MaxAI).jpeg]]
처음엔 사람이 직접 응답을 한 것을 보여주며 레이블 된 학습을 진행한다.(지도학습)
어느정도 LLM이 응답을 생성한다면 RM(reward Model)을 만든다.
GPT에게 질문에 대해 여러 응답을 만들도록 하여, 각 응답에 대해 랭킹을 매긴다.
랭킹들에 기반으로 GPT가 스스로 응답들에 대한 랭킹을 매겨 제공하도록 한다.
질문과 응답이 주어지면 스코어를 예측하고 강화학습의 보상으로 하여 학습한다.
![[image-36(Powered_by_MaxAI).jpeg]]
![[image-37(Powered_by_MaxAI).jpeg]]
![[image-38(Powered_by_MaxAI).jpeg]]
OpenAI의 마일스톤
1. 멀티모달
2. 사람이 보는 시험
  
![[image-39(Powered_by_MaxAI).jpeg]]
![[image-40(Powered_by_MaxAI).jpeg]]
여러 언어에 대해서도 좋은 성능을 보인다.
![[image-41(Powered_by_MaxAI).jpeg]]
![[image-42(Powered_by_MaxAI).jpeg]]
![[image-43(Powered_by_MaxAI).jpeg]]
![[image-44(Powered_by_MaxAI).jpeg]]
![[image-45(Powered_by_MaxAI).jpeg]]
![[image-46(Powered_by_MaxAI).jpeg]]
![[image-47(Powered_by_MaxAI).jpeg]]
![[image-48(Powered_by_MaxAI).jpeg]]
![[image-49(Powered_by_MaxAI).jpeg]]
![[image-50(Powered_by_MaxAI).jpeg]]
![[image-51(Powered_by_MaxAI).jpeg]]
![[image-52(Powered_by_MaxAI).jpeg]]
![[image-53(Powered_by_MaxAI).jpeg]]
![[image-54(Powered_by_MaxAI).jpeg]]