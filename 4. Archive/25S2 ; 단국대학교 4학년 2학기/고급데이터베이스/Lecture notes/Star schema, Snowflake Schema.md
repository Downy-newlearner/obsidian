---
created: 2025-09-10
Question:
---
좋은 질문이에요 👍

---

### 1. Star Schema (스타 스키마)

- 구조: 중앙에 Fact Table(사실 테이블)** 이 있고, 이를 둘러싸고 여러 개의 **Dimension Table(차원 테이블)** 이 별 모양으로 연결된 구조.
    
- 특징:
    
    - Dimension Table이 정규화되지 않음(denormalized) → 한 테이블에 속성들이 다 들어있음.
        
    - 쿼리 성능이 빠르고 이해하기 쉬움.
        
    
- 예시: 매출 분석 DW
    
    - Fact Table: 매출(날짜, 상품ID, 매출액…)
        
    - Dimension Table: 상품(상품ID, 상품명, 카테고리), 고객(고객ID, 이름, 지역), 시간(날짜, 요일, 분기)…
        
    

---

### 2. Snowflake Schema (스노우플레이크 스키마)

- 구조: Star Schema에서 Dimension Table을 더 정규화(normalized)**시켜 여러 작은 테이블로 분리한 구조. 차원 테이블이 여러 단계로 뻗어나가면서 눈송이 모양처럼 보임.
    
- 특징:
    
    - 중복 데이터가 줄어들고 저장공간 효율↑
        
    - 하지만 조인이 많아져서 쿼리 성능↓
        
    
- 예시: 매출 분석 DW
    
    - 상품 Dimension을 분리: 상품(상품ID, 상품명, 카테고리ID) + 카테고리(카테고리ID, 카테고리명)
        
    - 고객 Dimension을 분리: 고객(고객ID, 이름, 지역ID) + 지역(지역ID, 도시, 국가)
        
    

---

### ✅ 차이 요약

- Star Schema: 단순, 빠름, 공간 낭비 있음 (중복 데이터)
    
- Snowflake Schema: 정규화, 저장 효율적, 하지만 조인 많아서 느림
    

---

👉 그래서 빠른 분석이 중요하면 Star Schema, 저장 효율이나 데이터 일관성이 중요하면 Snowflake Schema를 선택합니다.

  

혹시 제가 두 스키마 구조를 도식 그림으로 간단히 그려드릴까요?