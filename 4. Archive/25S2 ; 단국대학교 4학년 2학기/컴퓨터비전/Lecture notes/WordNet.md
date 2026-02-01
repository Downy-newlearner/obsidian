---
created: 2025-09-15
Question: WordNet 계층 구조가 뭐야?
---
좋은 질문이에요 🙂

  

**WordNet 계층 구조**는 **단어들 간의 의미 관계를 “트리(tree)나 그래프” 형태로 조직한 구조**를 말해요.

  

조금 더 구체적으로:

- WordNet은 프린스턴 대학에서 만든 **영어 어휘 데이터베이스**예요.
    
- 단어들을 동의어 집합(synset, synonym set)으로 묶고, 이 synset들을 **상위-하위 관계(hypernym-hyponym)**로 연결합니다.
    
- 예를 들어:
    
    - “animal” → “mammal” → “dog” → “bulldog” 이렇게 점점 구체적인 계층 구조를 형성
        
    - “vehicle” → “car” → “sedan” → “BMW 3 series” 같은 식으로도 표현 가능
        
    

  

ImageNet은 이 WordNet의 계층 구조를 그대로 차용해서, 각 synset(동의어 집합)을 **이미지 클래스**로 사용했어요.

- 예: WordNet에 있는 “dog.n.01” synset → ImageNet에서는 이 synset을 대표하는 이미지 수천 장을 모아서 “강아지 클래스” 데이터셋을 만듦.
    
- 이렇게 하면 클래스들이 “무작위 목록”이 아니라, **의미론적 구조**를 가진 계층으로 정리됨.
    

  

👉 정리: WordNet 계층 구조란, 단어들을 **추상적 개념에서 구체적 개념으로 내려가는 의미적 트리**로 연결한 것, 그리고 ImageNet은 이 구조를 빌려 이미지 라벨을 설계한 거예요.

  

혹시 제가 WordNet 구조를 **그림 예시(트리 다이어그램)**로 간단히 그려드릴까요?