---
created: 2024-12-23
tags:
  - Terminology
aliases:
  - Term Frequency-Inverse Document Frequency
reference:
---
단어 빈도-역 문서 빈도(문서의 빈도에 특정 식을 취함)(Term Frequency-Inverse Document Frequency)이다.
단어의 빈도와 역 문서 빈도를 사용하여 [[DTM]](Document-Term Matrix, 문서-단어 행렬) 내의 각 단어들마다 중요한 정도를 가중치로 주는 방법이다.
우선 DTM을 만든 후, TF-IDF 가중치를 부여한다.

*주로 문서의 유사도를 구하는 작업, 검색 시스템에서 검색 결과의 중요도를 정하는 작업, 문서 내에서 특정 단어의 중요도를 구하는 작업 등에 쓰일 수 있습니다.*

TF-IDF는 TF와 IDF를 곱한 값을 의미한다.
문서를 d, 단어를 t, 문서의 총 개수를 n이라고 표현할 때, TF, DF, IDF는 각각 다음과 같이 정의할 수 있다.

1. TF(d, t)
	- Term Frequency
	- 특정 문서 d에서의 특정 단어 t의 등장 횟수
1. DF(t)
	- Document Frequency
	- 특정 단어 t가 등정한 문서의 수
1. IDF(t)
	- ![[Pasted image 20241223155308.png|300]]
	- Inverse Document Frequency
	- DF(t)에 반비례하는 수