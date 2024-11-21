## 자연어 처리 NLP
---
**자연어 Natural Language**
- 인공적으로 만들어진 프로그래밍 언어와 다르게 사람들이 쓰는 언어 활동을 위해 자연히 만들어진 언어
  
**자연어 처리 Natural Language Processing**
- 컴퓨터가 인간의 언어를 이해하고 해석 및 생성하기 위한 기술
- 컴퓨터가 인간과 유사한 방식으로 인간의 언어를 이해하고 처리하는 것이 주목표
- 인간 언어의 구조, 의미, 맥락 분석 & 이해할 수 있는 알고리즘과 모델 개발
  
**자연어 처리 모델 개발을 위해 해결해야할 문제**
- **모호성 Ambiguity**: 인간의 언어는 단어, 구가 사용되는 맥락에 따라 다양한 의미를 가짐
- **가변성 Variability**: 인간의 언어는 다양한 사투리, 강세, 신조어, 작문 스타일로 인해 매우 가변적
- **구조 Structure**: 인간의 언어는 구문을 파악하여 의미를 해석한다.
  
## 말뭉치와 토큰
---
- 말뭉치를 일정한 단위인 토큰으로 나눠야 한다.
  
### **말뭉치 Corpus**
- 자연어 모델을 훈려하고 평가하는데 사용되는 대규모의 자연어
- 뉴스 기사, 사용자 리뷰, 저널이나 칼럼 등에서 목적에 따라 구축되는 텍스트 데이터
- 일련의 단어의 가능성을 예측하는 알고리즘인 언어 모델을 구축하고 평가할 때 사용
  
### **토큰 Token**
- 개별 단어나 문장 부호와 같은 텍스트를 의미하며 말뭉치보다 더 작은 단위
- 텍스트의 개별 단어, 구두점, 또는 기타 의미 단위일 수 있다
- **토큰화 Tokenization**: 컴퓨터가 자연어를 이해할 수 있게 나누는 과정
  
### **토크나이저 Tokenizer**
- 텍스트 문자열을 토큰으로 나누는 알고리즘 또는 소프트웨어
- **공백 분할**: 텍스트를 공백 단위로 분리해 개별 단어로 토큰화한다.
- **정규표현식 적용**: 정규표현시긍로 특정 패턴을 식별해 텍스트를 분할한다.
- **어휘 사전 Vocabulary 적용**: 사전에 정의된 단어 집합을 토큰으로 사용한다.
    - **OOV(Out of Vocab)**: 직접 어휘 사전을 구축하여 없는 단어나 토큰이 존재
    - 큰 어휘 사전 구축은 비용 증대와 **차원의 저주 (Curve of Dimensionality)** 발생
    - 벡터값이 모두 0의 값을 가지는 **희소 sparse** 데이터로 표현
- **머신러닝 활용**: 데이터세트를 기반으로 토큰화하는 방법을 학습한 머신러닝을 적용한다.
  
### 토큰화
- 토큰화는 자연어 처리에서 매우 중요한 전처리 과정  
    → 구조적으로 분해하여 개별 토큰으로 나누는 작업을 수행  
    
- 작은 단위로 분해된 텍스트 데이터는 컴퓨터가 이해하고 처리하기 용이  
    → 기계 번역, 문서 분류, 감성 분류 등 다양한 자연어 처리 작업에 활용  
    
  
## 문장 토큰화 Sentence Tokenization
---

> **입력**: Time is an illusion. Lunchtime double so!  
>   
> **출력**: “Time is an illusion”, “Lunchtime double so!”
- 문장의 마침표(.), 개행문자(\n) 등 문장의 마지막을 뜻하는 기호에 따라 분리
- nltk와 같은 nlp 처리 라이브러리나 정규식을 사용할 수 있다
  
**정규식**
```Python
import re
text = "Time is an illusion. Lunchtime double so!"
sentences = re.split(r'(?<=[.!?]) +', text)
print(sentences)
```
![[Source/Untitled 163.png|Untitled 163.png]]
  
**nltk**
```Python
from nltk import sent_tokenize
text = "Time is an illusion. Lunchtime double so!"
print(sent_tokenize(text))
```
![[Source/Untitled 1 109.png|Untitled 1 109.png]]
  
## 단어 토큰화 Word Tokenization
---

> **입력**: Time is an illusion. Lunchtime double so!  
>   
> **출력**: "Time", "is", "an", "illustion", "Lunchtime", "double", "so”
- 문장을 단어로 토큰화한다
- 띄어쓰기, 문장 부호, 대소문자 등의 특정 구분자를 사용하여 수행하낟
- 품사 태깅, 개체명 인식, 기계 번역 등의 작업에서 널리 사용된다
- 단어 토큰화는 한국어 접사, 문장 부호, 오타 혹은 띄어쓰기 오류 등에 취약하다
  
**spilt()**
```Python
text = "Time is an illusion. Lunchtime double so!"
print(text.split())
```
![[Source/Untitled 2 78.png|Untitled 2 78.png]]
- 문자열 데이터 형태를 쉽게 토큰화 가능
- 구분자를 입력하지 않으면 **공백**을 기준으로 나눈다
  
**정규식**
```Python
import re
text = "Time is an illusion. Lunchtime double so!"
words = re.findall(r'\w+', text)
print(words)
```
![[Source/Untitled 3 64.png|Untitled 3 64.png]]
  
**nltk**
```Python
from nltk import word_tokenize
text = "Time is an illusion. Lunchtime double so!"
print(word_tokenize(text))
```
![[Source/Untitled 4 46.png|Untitled 4 46.png]]
  
### n-gram
- 문장을 단어별로 하나씩 토큰화 할 경우 문맥적인 의미는 무시될 수 밖에 없다
- 이러한 문제를 조금이라도 해결하기 위해 도입된 것이 n-gram
- n-gram은 연속된 n개의 단어를 하나의 토큰화 단위로 분리
  
## 글자 토큰화 Character Tokenization
---

> **입력**: Time is an illusion. Lunchtime double so!  
>   
> **출력**: 'T', 'i', 'm', 'e', ' ', 'i', 's', ' ', 'a', 'n', ' ', 'i', 'l', 'l', 'u', 's', 'i', 'o', 'n', …
- 글자 단위로 문장을 나누는 방식
- 비교적 작은 단어 사전을 구축할 수 있다.
    
    → 학습 시 컴퓨터 자원을 아낄 수 있으며, 각 단어를 더 자주 학습한다.
    
- 언어 모델링과 시퀀스 예측 작업에서 활용된다.
  
**list()**
```Python
text = "Time is an illusion. Lunchtime double so!"
print(list(text))
```
![[Source/Untitled 5 36.png|Untitled 5 36.png]]
- 공백도 토큰으로 나뉜다
- 영어의 경우 알파벳으로 나뉜다
- 한글의 경우 자소 단위로 나누어 토큰화 (’현’과 같이 자음과 모음의 조합 단위)
  
**정규식**
```Python
import re
text = "Time is an illusion. Lunchtime double so!"
characters = re.findall(r'.', text, re.UNICODE)
print(characters)
```
![[Source/Untitled 6 28.png|Untitled 6 28.png]]
  
**[jamo](https://python-jamo.readthedocs.io/en/latest/)**
```Python
retval = jamo.h2j(
	hangul_string
)
```
- jamo를 사용하여 자소 단위 토큰화가 가능
- 한글 문자열을 유니코드 U+1100~U+11FE 사이의 조합형 한글 자모로 변환
- 자모 단위로 나누어 인코딩 후 조합하여 한글을 표현한다.
  
```Python
from jamo import h2j, j2hcj
text = "Time is an illusion. Lunchtime double so!"
tokenized = list(j2hcj(h2j(text)))
print(tokenized)
```
![[Source/Untitled 7 27.png|Untitled 7 27.png]]
- 개별 토큰은 아무런 의미가 없으므로 자연어 모델이 각 토큰의 의미를 조합해 결과 도출
- 개체명 인식 Name Entity Recognition 등을 구현할 경우 도메인에서 구별이 어려움
- **시퀀스 sequence**의 길이가 길어질수록 연산량 증가
  
## 형태소 토큰화 Morpheme Tokenization
---

> **입력**: Time is an illusion. Lunchtime double so!  
>   
> **출력**: 'T', 'i', 'm', 'e', ' ', 'i', 's', ' ', 'a', 'n', ' ', 'i', 'l', 'l', 'u', 's', 'i', 'o', 'n', …
- 텍스트를 형태소 단위로 나누는 토큰화 방법
- 언어의 문법과 구조를 고려해 단어를 분리하고 이를 의미 있는 단어로 분류하는 작업
- 한국어와 같은 **교착어 Agglutinative Language**인 언어에서 중요
    - 교착어: 어근과 접사에 의해 단어의 기능이 결정되는 언어 형태
  
### **형태소 Morpheme**
- 실제로 의미를 가지고 있는 최소의 단위
|   |   |
|---|---|
|**자립 형태소 Free Morpheme**|• 스스로 의미를 가지고 있는 형태소  <br>• 명사, 동사, 형용사와 같은 단어를 이루는 기본 단위  <br>• 그, 나, 인사|
|**의존 형태소 Bound Morpheme**|• 스스로 의미를 갖지 못하고 다른 형태소로 조합되어 사용  <br>• 자립 형태소와 함께 조합되어 문장에서 특정한 역할을 수행  <br>• 조사, 어미, 접두사, 접미사 등  <br>• -는, -에게, -를, 했-, -다|
  
### **형태소 어휘 사전 Morpheme Vocabulary**
- 자연어 처리에서 사용되는 단어의 집합인 어휘 사전 중 각 단어의 형태소 정보 포함
- **품사 태깅 POS Tagging:** 각 형태소에 해당하는 **품사 Part of Speech, POS**를 태깅
    - 자연어 처리 분야에서 문맥 고려 가능 → 더욱 정확한 분석 가능
  
**nltk**
```Python
import nltk
from nltk import tag
from nltk import tokenize
text = "Time is an illusion. Lunchtime double so!"
tokens = tokenize.word_tokenize(text)
pos = tag.pos_tag(tokens)
print(pos)
```
![[Source/Untitled 8 24.png|Untitled 8 24.png]]
  
**konlpy**
```Python
from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
okt = Okt()
kkma = Kkma()
hannanum = Hannanum()
text = "무엇을 상상할 수 있는 사람은 무엇이든 만들어낼 수 있다"
print(okt.pos(text))
print(kkma.pos(text))
print(hannanum.pos(text))
```
![[7fc0f13c-1cad-4317-b407-7aa8e5134409.png]]
  
**spaCy**
```Python
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Time is an illusion. Lunchtime double so!"
doc = nlp(text)
for token in doc:
    print(f"[{token.pos_:5} - {token.tag_:3}] : {token.text}")
```
![[Source/Untitled 9 21.png|Untitled 9 21.png]]
  
## 하위 단어 토큰화
---
**OOV (Out-Of-Vocabulary) 문제**
- 기계에게 학습시켰을 때 단어 집합에 없는 단어를 UNK(Unknown Token)라고 표현
- 언어는 시간이 지남에 따라 새로운 단어나 표현이 등장하며 더 이상 사용되지 않는 단어들도 존재한다
- 또한 텍스트 분석에 사용되는 데이터들에 오탈자가 발생할 확률도 있다
- 외래어, 띄어쓰기, 오류, 오탈자가 있는 경우 정확한 형태소 분석이 불가능하다
  
**서브워드 분리**

> **단어**: Reinforcement  
>   
> **하위단어**: ’Rein’, ‘force’, ‘ment’
- **하위 단어 토큰화**는 이러한 현대 자연어 처리의 문제를 해결하기 위해 사용된다
- 단어를 빈번하게 사용되는 하위단어의 조합으로 나누어 토큰화한다
  
### 바이트 페어 인코딩 Byte Pair Encoding
- 다이그램 코딩 Digram Coding이라고도 하며 하위 단어 토큰화의 한 종류
- 가장 빈번하게 등장하는 글자 쌍의 조합을 찾아 부호화하는 압축 알고리즘으로 개발
  

> **원문**: abracadabra  
>   
> **Step \#1**: AracadAra → A = ab  
>   
> **Step \#2**: ABcadAB → B = ra  
>   
> **Step \#3**: CcadC → C = AB
- 바이트 페어 인코딩은 입력 데이터에서 가장 많이 등장한 글자의 빈도수 측정 후 가장 빈도수가 높은 글자 쌍을 탐색한다
- 가장 빈도수가 높은 글자 쌍: ‘ab’
- 다음으로 빈도수가 높은 글자 쌍: ‘ra’
- 다음으로 빈도수가 높은 글자 쌍: AB
  

> 빈도 사전: (’low’, 5), (’lower’, 2), (’newest’, +), (’widest’, 3)  
> 어휘 사전:  
- 바이트 페어 인코딩을 활용하여 빈도 사전과 어휘 사전을 만들 수 있다
  
**코포라 Korpora**
- 국립 국어원이나 AI Hub에서 제공하는 말뭉치 데이터를 쉽게 사용할 수 있게 제공하는 오픈소스 라이브러리
  
**센텐스피스 Sentencepiece**
- 구글에서 개발한 오픈소스 하위 단어 토크나이저 라이브러리
- 바이트 페어 인코딩과 유사한 알고리즘을 사용해 입력 데이터 토큰화 및 단어 사전 생성
```Python
from sentence import SentencePieceTrainer
SentencePieceTrainer.Train(
)
```
  
### 워드피스
- 바이트 페어 인코딩 토크나이저와 유사한 방법으로 학습
- 빈도 기반이 아닌 확률기반으로 글자 쌍을 병합
- 이전 하위 단어와 함께 나타날 확률을 계산해 가장 높은 확률을 가진 하위 단어 선택
  
**토크나이저스 Tokenizers**
- 정규화와 사전 토큰화를 제공
- 정규화: 일관된 형식으로 텍스트 표준화, 모호한 경우를 방지하기 위해 대체 및 제거
- 불필요한 공백 제거, 대소문자 변환, 유니코드 정규과, 구두점 처리, 특수문자처리 등
  
## 다양한 라이브러리
---
- 영어와 한국어는 토큰화 방법이 다르
- 토큰화를 지원하는 다양한 라이브러리들이 존재한다
    - [NLTK](https://www.nltk.org/): 영어 형태소 분
    - [KoNLPy](https://konlpy.org/ko/latest/index.html): 한국어 형태소 분석
    - [spaCy](https://spacy.io/)
  
## 참고자료
---
- 파이토치 트랜스포머를 활용한 자연어 처리와 컴퓨터 비전 심층학습
- 파이썬 머신러닝 완벽가이드
- [딥러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)