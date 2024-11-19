---
created: 
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
- 
![[Pasted image 20241119112719.png]]