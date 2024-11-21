[[HUB/포트폴리오/LG Aimers/LG Aimers 캡스톤/Git|Git]]
- ==**대회 소개 및 일정**==
    
    ![[Source/Untitled 91.png|Untitled 91.png]]
    
      
    
    > [!info] 엘리스 :: elice  
    > 파이썬부터 딥러닝, 인공지능까지, 초보도 가능한 실습형 코딩수업!  
    > [https://lgaimers5th.elice.io/](https://lgaimers5th.elice.io/)  
    
      
    
    **아카이브(수상작)**
    
    > [!info] LG AI ACADEMY  
    > Web site created using create-react-app  
    > [https://academy.lgresearch.ai/archive](https://academy.lgresearch.ai/archive)  
    
      
    
- ==**규칙**==
    
    ![[ba41c4c5-ab75-4d95-9c90-3f3a059030e8.png]]
    
      
    
    ![[Source/Untitled 1 62.png|Untitled 1 62.png]]
    
    ![[Source/Untitled 2 46.png|Untitled 2 46.png]]
    
      
    
      
    
      
    
- **참고 자료**
    
    **데이터 분석**
    
    ![[%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%B6%84%EC%84%9D_%EB%B0%8F_%EC%A0%84%EC%B2%98%EB%A6%AC_%EB%B0%A9%EB%B2%95.pdf]]
    
      
    
    **해커톤 도메인**
    
    ![[%ED%95%B4%EC%BB%A4%ED%86%A4_%EB%8F%84%EB%A9%94%EC%9D%B8_%EC%A0%95%EB%A6%AC.pdf]]
    
    ![[%ED%95%B4%EC%BB%A4%ED%86%A4_%EB%AC%B8%EC%A0%9C_%EC%86%8C%EA%B0%9C_%EC%A0%95%EB%A6%AC.pdf]]
    
    ![[LG_%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4_%EC%84%A4%EB%AA%85_%EB%B0%8F_%EB%B6%88%EB%9F%89_%EC%9A%94%EC%9D%B8_%EA%B4%80%EB%A0%A8_%EB%B3%80%EC%88%98%EC%99%80_%ED%95%B4%EA%B2%B0%EB%B0%A9%EC%95%88.pdf]]
    
    [[도메인 분석]]
    
    **입상작 코드**
    
    ![[2%EA%B8%B0_%EC%9E%85%EC%83%81_%ED%8C%80_%EC%BD%94%EB%93%9C_%EB%B0%8F_%EB%B0%9C%ED%91%9C.zip]]
    
    ![[LG_Aimers_4%EA%B8%B0_%EC%BD%94%EB%93%9C.zip]]
    
  
- **피쳐**
    
    - Resin 도포 & 반경화
        - Resin 토출 좌표
        - Resin 토출 속도
        - Resin 토출 시간
        - Resin 토출량
        - Resin 대기 좌표
        - 공정 소요 시간
        - 노줄 클린 좌표
        - UV 경화 속도
        - UV 경화 시간
        - UV 경화 위치
    - 합착
        - Glass 이동 좌표
        - Disp. 위치 좌표
        - Glass 이동 속도
        - 합착 Gap
        - 공정 온도
        - 공정 습도
        - Disp. 평탄도
        - 공정 소요 시간
        - 대기 좌표
    - 탈포
        - 1st 탈포 압력
        - 1st 탈포 시간
        - 2nd 탈포 압력
        - 2nd 탈포 시간
        - 3rd 탈포 압력
        - 3rd 탈포 시간
        - 챔버 온도
        - 챔버 습도
        - 공정 소요시간
        - 평탄
    
      
    
- **피쳐 분석**
    
    Dam dispensing: 외측 도포
    
    Fill1 dispensing: 내측 도포
    
    Fill2 dispensing: 내측 도포
    
    Auto Clave: 탈포 과정
    
    - HEAD NORMAL COORDINATE X AXIS(Stage1)
        - HEAD NORMAL COORDINATE X AXIS(Stage1)과 Stage 3는 반대되는 특성을 가짐 stage1이 500대면 stage3은 160대임
        - 2023-10-2일부터 12-9까진 HEAD NORMAL COORDINATE X AXIS(Stage1)의 데이터가 없음
        - 2023-12-13부터 2024-03-09까지 OK로 표시 이때 처음 Set ID는 OP753345013120000379
        - 2024-03-13부터 다시 데이터 없음
        - stage 1~3에서 500과 160대가 계속 반복되는 이유는 장비가 2개(Dam dispenser \#1, Dam dispenser \#2)라서 왔다갔다 하는 것처럼 보임.
    
      
    
- **피쳐 그룹핑**
    
    |   |   |   |   |   |
    |---|---|---|---|---|
    |CURE END POSITION (X, Z, Θ)|경화 공정이 종료되는 위치|Collect Result.~2 - Dam||Collect Result.~2 - Fill2|
    |CURE SPEED|경화 공정 동안의 이동 속도|Collect Result.3 - Dam||Collect Result.3 - Fill2|
    |CURE STANDBY POSITION (X, Z, Θ)|경화 공정이 시작되기 전 대기 위치|Collect Result.4~6 - Dam||Collect Result.4~6 - Fill2|
    |CURE START POSITION (X, Z, Θ)|경화 공정이 시작되는 위치|Collect Result.7~9 - Dam||Collect Result.7~9 - Fill2|
    |DISCHARGED SPEED OF RESIN|레진 방출 속도|Collect Result.10 - Dam|Collect Result - Fill1|Collect Result.10 - Fill2|
    |DISCHARGED TIME OF RESIN(Stage1, 2, 3)|레진 방출 시간|Collect Result.11~13 - Dam|Collect Result.1~3 - Fill1|Collect Result.11~13 - Fill2|
    |Dispense Volume(Stage1, 2, 3)|레진 방출량|Collect Result.14~16 - Dam|Collect Result.4~6 - Fill1|Collect Result.14~16 - Fill2|
    |HEAD NORMAL COORDINATE X AXIS(Stage1, 2, 3)|장비 헤드의 공정별 X축 좌표|Collect Result.17~19 - Dam|Collect Result.7~9 - Fill1|Collect Result.17~19 - Fill2|
    |HEAD NORMAL COORDINATE Y AXIS(Stage1, 2, 3)|장비 헤드의 공정별 Y축 좌표|Collect Result.20~22 - Dam|Collect Result.10~12 - Fill1|Collect Result.20~22 - Fill2|
    |HEAD NORMAL COORDINATE Z AXIS(Stage1, 2, 3)|장비 헤드의 공정별 Z축 좌표|Collect Result.23~25 - Dam|Collect Result.13~15 - Fill1|Collect Result.23~25 - Fill2|
    |HEAD Standby Position X, Y, Z|장비 대기 위치|Collect Result.26~28 - Dam|Collect Result.16~18 - Fill1|Collect Result.26~28 - Fill2|
    |Head Clean Position X, Y, Z|장비 청소 위치|Collect Result.29~31 - Dam|Collect Result.19~21 - Fill1|Collect Result.29~31 - Fill2|
    |Head Purge Position X, Y, Z|장비 잔여물 제거 위치|Collect Result.32~34 - Dam|Collect Result.22~24 - Fill1|Collect Result.32~34 - Fill2|
    |Head Zero Position X, Y, Z|장비 기준 위치|Collect Result.35~37 - Dam|||
    |Machine Tact time|전체 공정에서 한 제품의 처리 시간|Collect Result.38 - Dam|Collect Result.25 - Fill1|Collect Result.35 - Fill2|
    |PalletID|특정 제품이나 공정을 처리하는 팔레트 식별자|Collect Result.39 - Dam|Collect Result.26 - Fill1|Collect Result.36 - Fill2|
    |Production Qty|특정 공정이나 기간 동안 생산된 제품의 수량|Collect Result.40 - Dam|Collect Result.27 - Fill1|Collect Result.37 - Fill2|
    |Receip No|제품이나 재료의 입고 번호|Collect Result.41 - Dam|Collect Result.28 - Fill1|Collect Result.38 - Fill2|
    |Stage1 Circle1, 2, 3, 4 Distance Speed|Stage1에서 원형으로 이동할 때의 속도|Collect Result.42~45 - Dam|||
    |Stage1 Line1, 2, 3, 4 Distance Speed|Stage1에서 직선으로 이동할 때의 속도|Collect Result.46~49 - Dam|||
    |Stage2 Circle1, 2, 3, 4 Distance Speed|Stage2에서 원형으로 이동할 때의 속도|Collect Result.50~53 - Dam|||
    |Stage2 Line1, 2, 3, 4 Distance Speed|Stage2에서 직선으로 이동할 때의 속도|Collect Result.54~57 - Dam|||
    |Stage3 Circle1, 2, 3, 4 Distance Speed|Stage3에서 원형으로 이동할 때의 속도|Collect Result.58~61 - Dam|||
    |Stage3 Line1, 2, 3, 4 Distance Speed|Stage3에서 직선으로 이동할 때의 속도|Collect Result.62~65 - Dam|||
    |THICKNESS 1, 2, 3|제품의 두께|Collect Result.66~68 - Dam|||
    |WorkMode|작업 모드|Collect Result.69 - Dam|Collect Result.29 - Fill1|Collect Result.39 - Fill2|
    
    ![[Group.xlsx]]
    
### 사용 데이터
![[train.csv]]
![[merge.csv]]
  
### 제공 코드
![[code.ipynb]]
  
#### 2024 LG Aimers 캡스톤
|이름|태그|날짜|
|---|---|---|
|[[1차 회의]]||2024/08/07|
|[[새 데이터 분석]]|||
|[[all_data 피처 분석]]|||
|[[3차 회의]]|||
  
  
  
### 제공 코드
[[제출 결과 공유]]
![[1929_fixed_preprocessing.ipynb]]
[[1929]]
### 데이터 전처리 진행 히스토리
[[begin]]
[[second]]
[[third(예정)]]
  
[[피처 분석]]
  
[[하이퍼파라미터 튜닝]]