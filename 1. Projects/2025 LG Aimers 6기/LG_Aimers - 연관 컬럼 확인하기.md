
'시술 유형', '특정 시술 유형', '배란 자극 여부', '배란 유도 유형'


'총 시술 횟수', '클리닉 내 총 시술 횟수', 'IVF 시술 횟수', 'DI 시술 횟수', '총 임신 횟수', 'IVF 임신 횟수', 'DI 임신 횟수', '총 출산 횟수', 'IVF 출산 횟수', 'DI 출산 횟수'


'총 생성 배아 수', 

'저장된 배아 수', '미세주입 후 저장된 배아 수', '해동된 배아 수', '해동 난자 수', '수집된 신선 난자 수', '저장된 신선 난자 수', '혼합된 난자 수', '파트너 정자와 혼합된 난자 수', '기증자 정자와 혼합된 난자 수', 


'동결 배아 사용 여부', '신선 배아 사용 여부', '기증 배아 사용 여부', '대리모 여부', '난자 채취 경과일', '난자 혼합 경과일', '배아 이식 경과일'


'임신 성공 여부'


'미세주입된 난자 수', '미세주입에서 생성된 배아 수', '미세주입 배아 이식 수'

'정자 나이', '난자 나이'


## 임신  성공 여부와 관련이 있어보이는 컬럼들
1. 시술 당시 나이
2. 


## 같은 주제로 묶이는 컬럼들

### 1. 불임 원인
'단일 배아 이식 여부', '남성 주 불임 원인', '남성 부 불임 원인', '여성 주 불임 원인', '여성 부 불임 원인', '부부 주 불임 원인', '부부 부 불임 원인', '불명확 불임 원인'

'불임 원인 - 난관 질환', '불임 원인 - 남성 요인', '불임 원인 - 배란 장애', '불임 원인 - 여성 요인', '불임 원인 - 자궁경부 문제', '불임 원인 - 자궁내막증', '불임 원인 - 정자 농도', '불임 원인 - 정자 면역학적 요인', '불임 원인 - 정자 운동성', '불임 원인 - 정자 형태'


### 2. 난자
'난자 출처', '난자 기증자 나이', '대리모 여부', '난자 채취 경과일', '난자 혼합 경과일',

### 3. 배아 이식
'단일 배아 이식 여부', '이식된 배아 수'

- 이식된 배아 수가 0이면 단일 배아 이식 여부가 0임(단일 배아 이식을 안했다는 의미)
- 즉 

## 시술 당시 나이
- 연관 컬럼이 굉장히 많을 것으로 예상됨.

```
def create_age_columns(row):

# 정자 나이 컬럼: 정자 출처가 '기증 제공'이면 정자 기증자 나이 사용, 그렇지 않으면 '알 수 없음'

sperm_age = row['정자 기증자 나이'] if row['정자 출처'] == '기증 제공' else '알 수 없음'

  

# 난자 나이 컬럼 생성

egg_age = row['난자 기증자 나이'] if '난자 기증자 나이' in row else '알 수 없음'

  

# 새로운 정보 반환

return pd.Series({'정자 나이': sperm_age, '난자 나이': egg_age})

  

df[['정자 나이', '난자 나이']] = df.apply(create_age_columns, axis=1)
```
- 정자 나이, 난자 나이 컬럼을 생성했음
- '시술 당시 나이', '정자 기증자 나이', '난자 기증자 나이', '난자 출처', '정자 출처' 컬럼을 삭제해도 된다.


임신 성공 vs 임신 실패
컬럼별 value_count

![[Pasted image 20250214012136.png|400]]

![[Pasted image 20250214012154.png]]