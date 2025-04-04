## 1.1 LLM이란?
### 1.1.1 LLM 정의
- LLM과 트랜스포머가 해결하고있는 작업은 **언어 모델링 작업**이다.
	1. 자동 인코딩
	2. 자기회귀 언어 모델

![[Pasted image 20250112235952.png|400]]

- 자동 인코딩은 문장의 누락된 부분을 채우도록 모델에 요청한다.
- 자기회귀 언어 모델은 주어진 문장의 바로 다음에 가장 가능성 있는 토큰을 생성하도록 모델에 요청한다. (예시: BERT)

### 1.1.2 LLM 주요 특징
- 기존의 트랜스포머 아키텍처는 2017년에 고안된 **시퀀스-투-시퀀스**sequence-to-sequence (seq2 seq) 모델이었으며, 이는 두 가지 구성 요소를 주로 가지고 있었다.
	- ![[Pasted image 20250112235750.png|300]]
		- 인코더는 원시 텍스트를 받아들여 핵심 구성 요소로 분리하고, 해당 구성 요소를 벡터로 반환하는 업부를 담당한다. 또한 어텐션을 사용하여 텍스트의 맥락을 이해한다.
		- 디코더는 수정된 형식의 어텐션을 사용하여 다음에 올 토큰을 예측한다.

- LLM 예시
![[Pasted image 20250113000036.png]]
35


### 1.1.3 LLM 작동 원리

- 토큰화
	- 특별한 토큰이 존재한다.
		- CLS 토큰은 Classification이라는 뜻으로 모델이 주어진 입력에 대해 클래스 예측을 할 때 사용된다.
			- 이 토큰은 문장 앞에서 문장의 전체적인 의미를 이해하도록 도와주는 역할을 한다.
			- 모델은 입력 문장에 대해 CLS 토큰을 기준으로 문장의 전체적인 의미를 벡터로 인코딩하고, 이 벡터는 후속 분류 작업에 사용된다.
		- SEP 토큰은 Separator의 약자로, 문장의 구분을 나타내는 특수 토큰이다.



## 1.2 [[현재 많이 사용되는 LLM]]
[[4. Archive/2025 LLM 스터디/1주차 - 1/BERT]]
[[GPT]]
[[T5]]


## 1.3 도메인 특화 LLM
- 도메인 특화 LLM을 사용하는 장점은 특정 텍스트 집합에서의 훈련에 있다.
- 도메인에서 사용되는 언어와 개념을 더 이해할 수 있어서, 그 도메인 내의 NLP 작업에 대한 정확도와 유창성이 향상된다.

- 반면, 일반 목적의 LLM은 특정 도메인에서 사용되는 언어와 개념을 효과적으로 다루는 데 어려움을 겪을 수 있다.

## 1.4 LLM을 이용한 어플리케이션

### 1.4.1 전통적인 자연어 처리 작업

#### 텍스트 분류
#### 번역 작업
- "사람 언어 > 사람 언어" 번역이 가능하다
- SQL 생성 작업도 가능하다.

### 1.4.2 자유로운 텍스트 생성
- 이는 사람의 '백지상태' 문제를 해결하는 데 도움을 줄 수 있으며, 너무 오랜 시간 동안 빈 페이지를 바라보는 것보다는 적어도 시작할 수 있는 무언가를 제공해준다.

### 1.4.3 정보 검색/신경망 의미 기반 검색
- LLM을 학습시킨 데이터는 업데이트가 필요하기 마련인데, 이는 처음부터 훈련을 다시 해야하므로 까다로운 작업이다.
- *벡터 DB*를 사용하여 이를 해결할 수 있다.
![[Pasted image 20250113005638.png]]


### 1.4.4 챗봇
