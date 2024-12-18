---
created: 2024-11-19
tags: 
aliases:
---
![[Pasted image 20241119112635.png]]
랭체인에서는 통합된 함수를 사용한다.
	예를 들어 load()함수는 무슨 형식의 데이터든지 상관없이 로드할 수 있다.(통합된 함수)
랭체인은 개발 속도를 향상시키는 역할을 한다.

### 1. Load 
랭체인에서 데이터를 가져오는 load함수,
```
# 뉴스기사 내용을 로드하고, 청크로 나누고, 인덱싱합니다.

loader = WebBaseLoader(

    web_paths=("https://n.news.naver.com/article/437/0000378416",),

    bs_kwargs=dict(

        parse_only=bs4.SoupStrainer(

            "div",

            attrs={"class": ["newsct_article _article_body", "media_end_head_title"]},

        )

    ),

)

  

docs = loader.load()

print(f"문서의 수: {len(docs)}")

docs
```

docs = loader.load()

print(f"문서의 수: {len(docs)}")

docs

이렇게 load()함수를 사용해서 어떤 형식의 파일이든 로드할 수 있다는 강력한 장점이 있다.


### 2. Split
- 만약 데이터가 100장 있으면 LLM모델이 입력받을 수 있는 사이즈로 쪼갠다.
- 만약 1장에 하나의 소주재로 100장이 있다면, 100개로 쪼개야한다.
	- 쪼갤 때의 기준이 주제가 되어야 LLM이 해석할 때 유리하다.
- 그래서 데이터의 특성과 테스트를 통해서 얼마나 쪼개야하는지 결정해야한다.

![[Pasted image 20241119114040.png]]
chunk size는 글자수
chunk overlap은 문단을 자를 때 내용이 잘릴 수도 있어서 앞 청크와 어느정도 겹치게 오버랩해서 자른다.

### 3. embedding
- 로드 후 split한 데이터에 대해 LLM에 질문을 하면 잘려진 각 문단에서 질문과 유사도 검사를 진행한다. 그 중 가장 유사한 부분을 찾아 답변에 포함한다.
- 위 작업은 임베딩 과정을 거친 후에 가능하다.

![[Pasted image 20241119112719.png]]

### 결론
![[Pasted image 20241119114951.png]]
질문을 함 -> 질문에 대해 검색을 우선 진행(retriever가 수행: 내 질문에 연관성이 가장 높은 단락을 뽑아준다.) -> 서칭된 결과를 하나로 합친다.(format_docs 함수) -> 합쳐서 이어진 문장들을 프롬프트에게 넘겨준다. -> LLM에게 넘겨준다. -> 완료