## 한국어에서 토큰화
---
- 한국어는 영어와 달리 띄어쓰기만으로 토큰화하기 부족
- 한국어는 교착어이기 때문에 띄어쓰기 단위인 어절을 통해 토큰화하는 것은 좋지 않다
  
**교착어**
- '그가', '그에게', '그를', '그와', '그는'과 같이 다양한 조사
- 다른 단어로 인식이 되면 자연어 처리가 힘들고 번거로워지는 경우가 많다
- 조사 등의 무언가가 붙어있는 경우가 많아서 이를 전부 분리해줘야 한다
- 따라서 한국어는 형태소 단위로 토큰화를 수행해야한다
  
**한국어는 띄어쓰기가 영어보다 잘 지켜지지 않는다**
- 한국어는 영어권 언어와 비교하여 띄어쓰기가 어렵고 잘 지켜지지 않는 경향이 있다
- 수많은 코퍼스에서 띄어쓰기가 무시되는 경우가 많아 자연어 처리가 어려워졌다
  
## KoNLPy
---
- 한국어 자연어 처리를 위해 개발된 라이브러리
- 명사 추출, 형태소 분석, 품사 태깅 등의 기능을 제공
- 텍스트 데이터를 전처리하고 분석하기 위한 다양한 도구와 함수를 제공
- 텍스트 마이닝, 감정 분석, 토픽 모델링 등 다양한 NLP 작업에서 사용
- **링크 모음**
    - 설치법: [https://konlpy.org/ko/latest/install/](https://www.google.com/url?q=https%3A%2F%2Fkonlpy.org%2Fko%2Flatest%2Finstall%2F)
    - KoNLPy 기본 지식: [https://konlpy.org/ko/latest/index.html#start](https://www.google.com/url?q=https%3A%2F%2Fkonlpy.org%2Fko%2Flatest%2Findex.html%23start)
    - KoNLPy 사용법 가이드: [https://konlpy.org/ko/latest/index.html#guide](https://www.google.com/url?q=https%3A%2F%2Fkonlpy.org%2Fko%2Flatest%2Findex.html%23guide)
    - KoNLPy API: [https://konlpy.org/ko/latest/index.html#api](https://www.google.com/url?q=https%3A%2F%2Fkonlpy.org%2Fko%2Flatest%2Findex.html%23api)
  
**KoNLPy 라이브러리 설치**
```Python
pip install konlpy
```
- **자바 개발 키트 JDK** 기반으로 개발
- Okt (Open Korean Text) 꼬꼬마(Kkma), 코모란(Komoran), 한나눔(Hannanum), 메캅(Mecab) 등의 다양한 형태소 분석기를 지원한다.
  
**Colab**
```Python
!apt-get update
!apt-get install g++ openjdk-8-jdk
!pip3 install konlpy JPype1-py3
!bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
!pip install mecab-python3
```
  
**한글 형태소 분석**
- 형태소 분석기 종류: Hannanum, Kkma, Komoran, Mecab, Okt
- Kkma: 처리 속도가 너무 느리다
- Mecab: 처리속도가 가장 빠르지만 설치 과정이 복잡하다
- Okt, Hannanum: 적은 데이터의 경우 유리하다
  
## [한나눔 Hannanum](https://konlpy.org/ko/latest/api/konlpy.tag/#module-konlpy.tag._hannanum)
---
```Python
from konlpy.tag import Hannanum
hannanum = Hannanum()
sentence = "무엇을 상상할 수 있는 사람은 무엇이든 만들어낼 수 있다"
analyze = hannanum.analyze(sentence)
morphs = hannanum.morphs(sentence)
nouns = hannanum.nouns(sentence)
pos = hannanum.pos(sentence)
print(analyze)
print(morphs)
print(nouns)
print(pos)
```
![[Source/Untitled 165.png|Untitled 165.png]]
- analyze(phrase)
    - 입력된 문장을 분석하여 형태소와 품사 정보를 포함하는 구조화된 결과를 반환
- morphs(phrase)
    - 입력된 문장에서 형태소 단위로 분리된 어절들을 반환
- nouns(phrase)
    - 입력된 문장에서 명사만을 추출하여 반환
- pos(phrase, ntags=9, flatten=True, join=False)
    - 입력된 문장에서 형태소 단위로 분리된 어절과 그에 해당하는 품사 태그를 튜플 형태로 반환
    - ntags – 반환되는 품사 태그의 개수를 설정, 9 또는 22 중 하나로 설정
    - flatten – False: 어절 단위의 구조를 유지하여 반환
    - join – True: 형태소와 품사 태그를 결합하여 반환
  
## [꼬꼬마 Kkma](https://konlpy.org/ko/latest/api/konlpy.tag/#module-konlpy.tag._kkma)
---
```Python
from konlpy.tag import Kkma
kkma = Kkma()
sentence = "무엇을 상상할 수 있는 사람은 무엇이든 만들어낼 수 있다"
nouns = kkma.nouns(sentence)
phrases = kkma.sentences(sentence)
morphs = kkma.morphs(sentence)
pos = kkma.pos(sentence)
print("명사 추출: ", nouns)
print("문장 추출: ", sentences)
print("형태소 추출: ", morphs)
print("품사 태깅: ", pos)
```
![[Source/Untitled 1 111.png|Untitled 1 111.png]]
- nouns(phrase)
    - 입력된 문장에서 명사만을 추출하여 리스트로 반환
- sentences(phrase)
    - 입력된 텍스트에서 문장 단위로 분리하여 리스트로 반환
- morphs(phrase)
    - 입력된 문장에서 형태소 단위로 분리된 어절들을 리스트로 반환
- pos(phrase)
    - 입력된 문장에서 형태소 단위로 분리된 어절과 그에 해당하는 품사 태그를 튜플 형태의 리스트로 반환
  
![[Source/Untitled 2 79.png|Untitled 2 79.png]]
![[Source/Untitled 3 65.png|Untitled 3 65.png]]
  
## [코모란 Komoran](https://konlpy.org/ko/latest/api/konlpy.tag/#module-konlpy.tag._komoran)
---
```Python
from konlpy.tag import Komoran
komoran = Komoran()
sentence = "무엇을 상상할 수 있는 사람은 무엇이든 만들어낼 수 있다"
morphs = komoran.morphs(sentence)
nouns = komoran.nouns(sentence)
pos = komoran.pos(sentence)
print(morphs)
print(nouns)
print(pos)
```
![[Source/Untitled 4 47.png|Untitled 4 47.png]]
- morphs(phrase)
    - 입력된 문장에서 형태소 단위로 분리된 어절들을 리스트로 반환
- nouns(phrase)
    - 입력된 문장에서 명사만을 추출하여 리스트로 반환
- pos(phrase)
    - 입력된 문장에서 형태소 단위로 분리된 어절과 그에 해당하는 품사 태그를 튜플 형태의 리스트로 반환
  
## [Mecab](https://konlpy.org/ko/latest/api/konlpy.tag/#mecab-class)
---
- Windows에서는 제공되지 않는다.
- discpath: the path of the mecab-ko dictionary
- morphs(phrase)
- nouns(phrase)
- pos(phrase, flatten=True, join=False)
    - flatten: False - preserves eojeols
    - join: True - returns joined sets of morph and tag
  
## [Okt](https://konlpy.org/ko/latest/api/konlpy.tag/#okt-class)
---
```Python
from konlpy.tag import Okt
okt = Okt()
sentence = "무엇을 상상할 수 있는 사람은 무엇이든 만들어낼 수 있다"
morphs = okt.morphs(sentence)
normalize = okt.normalize(sentence)
nouns = okt.nouns(sentence)
phrases = okt.phrases(sentence)
pos = okt.pos(sentence)
print(morphs)
print(normalize)
print(nouns)
print(phrases)
print(pos)
```
![[Source/Untitled 5 37.png|Untitled 5 37.png]]
- morphs(phrase, norm=False, stem=False)
    - 주어진 텍스트를 형태소 단위로 분리
- normalize(phrase)
    - 주어진 텍스트를 정규화
- nouns(phrase)
    - 주어진 텍스트를 형태소 단위로 분리해서 명사만
- phrases(phrase)
    - 주어진 텍스트에서 의미있는 구를 추출
- pos(phrase, norm=False, stem=False, join=False)
    - 주어진 텍스트를 형태소 단위로 분리해서 태깅하여 보여준다.
    - norm: True - normalize tokens
    - stem: True - stem tokens
    - join: True - returns joined sets of morph and tag
  
![[Source/Untitled 6 29.png|Untitled 6 29.png]]
  
## [corpus](https://konlpy.org/ko/latest/api/konlpy.corpus/)
---
- 대한민국 헌법 전문과 법률 서비스 제공
    - 헌법 전문: `konlpy.corpus.kolaw`
    - 법률: `konlpy.corpus.kobill`
  
```Python
from konlpy.corpus import kolaw
fids = kolaw.fileids()
fobj = kolaw.open(fids[0])
print(fobj.read(140))
```
- `kolaw.fileids()`: 파일명을 확인, 문서를 읽어들임
- `open(filename)`: file object를 반환
  
## 참고자료
---
- [토큰화](https://wikidocs.net/21698)
- [한글 형태소 분석기](https://wikidocs.net/127849)
- [konlpy documentation](https://konlpy.org/ko/latest/api/konlpy/)
- 파이토치 트랜스포머를 활용한 자연어 처리와 컴퓨터 비전 심층학습