# 🧐 Discriminative Model이란 무엇인가?

## 형식적 답

Discriminative Model은 주어진 입력 데이터에서 그 데이터가 속하는 레이블 또는 카테고리를 예측하는 모델을 말합니다. 이 모델은 입력 데이터가 주어졌을 때 특정 레이블이 될 확률을 계산하는 데 초점을 맞춥니다. 주로 분류(classification) 작업에서 사용되며, 두 클래스 또는 여러 클래스 간의 경계(boundary)를 학습하여 새로운 데이터를 해당 클래스에 할당합니다.

예시와 설명:
Logistic Regression: 주어진 입력 데이터에 대해 특정 클래스에 속할 확률을 예측하는 모델입니다.
Support Vector Machine (SVM): 데이터 포인트들을 분리하는 최적의 초평면(hyperplane)을 찾는 모델입니다.
신경망(Neural Networks): 입력 데이터에 대해 특정 클래스로 분류하는 모델입니다.
특징:
결정 경계 학습: Discriminative Model은 데이터의 클래스 간 결정 경계에 초점을 맞추어 학습합니다.
확률 모델링: 데이터의 조건부 분포 
𝑃(𝑌∣𝑋)
P(Y∣X)를 학습합니다. 여기서 𝑌
Y는 레이블, 𝑋
X는 입력 데이터입니다.
응용: 이미지 분류, 텍스트 분류, 스팸 필터링, 감정 분석 등 다양한 분류 작업에 사용됩니다.
비교:
Generative Model은 데이터 생성 및 분포에 대한 이해를 목표로 하며, 데이터가 어떻게 만들어졌는지를 모델링합니다. 예를 들어, 이미지 생성, 텍스트 생성과 같은 작업에 사용됩니다.
Discriminative Model은 주어진 데이터로부터 레이블을 예측하는 데 초점을 맞추며, 데이터가 어떤 클래스에 속하는지를 구분합니다. 주로 분류 문제에 사용됩니다.

## 내가 이해한 정답

분류문제 - 경계면 가지고 구분하는것이 목표 

피처들간 차이점으로 클래스 차이확인
디시젼 바운더리 선정해서 두 클래스가 어떻게 다른지 정함

작은데이터로 잘하고 컴퓨테이션 적음 오버피팅 높을 수 있음

## AI 답변

Discriminative Model은 머신러닝 모델 중 하나로, 주어진 입력 데이터(Input Data)에 대한 레이블(Label)이나 타겟(Target)을 직접적으로 예측하는 모델입니다. 

Discriminative Model은 조건부 확률 분포 P(Y|X)를 모델링하여, 입력 X가 주어졌을 때 레이블 Y를 예측합니다. 이는 주어진 입력에 대한 출력 분포를 직접 학습하는 것입니다.

대표적인 Discriminative Model로는 다음과 같은 것들이 있습니다:

1. 로지스틱 회귀(Logistic Regression)
2. 서포트 벡터 머신(Support Vector Machines, SVM)
3. 신경망(Neural Networks)
4. 의사 결정 트리(Decision Trees)
5. 커널 기법(Kernel Methods)

Discriminative Model은 Generative Model과 대비되는 개념으로, Generative Model은 데이터의 전체 확률 분포 P(X, Y)를 모델링합니다. 일반적으로 Discriminative Model이 Generative Model보다 예측 성능이 좋은 편입니다.

