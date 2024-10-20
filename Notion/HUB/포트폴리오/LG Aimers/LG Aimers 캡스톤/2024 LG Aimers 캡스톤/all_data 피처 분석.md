![[all_data.csv]]
- Dam dispensing: 외측 도포
- Fill1 dispensing: 내측 도포
- Fill2 dispensing: 내측 도포
- Auto Clave: 탈포 과정
  
1: Equipment_Dam:
2: Model.Suffix_Dam:
3: Workorder_Dam:
## 레진 도포&반경화
### 레진 토출 속도
4: DISCHARGED SPEED OF RESIN Collect Result_Dam:
  
### 레진 토출 좌표
5: HEAD NORMAL COORDINATE X AXIS(Stage1) Collect Result_Dam:
6: HEAD NORMAL COORDINATE X AXIS(Stage2) Collect Result_Dam:
7: HEAD NORMAL COORDINATE X AXIS(Stage3) Collect Result_Dam:
  
### Resin 토출 시간
  
### Resin 토출량
  
  
### Resin 대기 좌표
10: Head Zero Position Y Collect Result_Dam:
11: Head Zero Position Z Collect Result_Dam:
  
### 공정 소요 시간
  
### 노줄 클린 좌표
8: Head Clean Position Z Collect Result_Dam:
9: Head Purge Position Z Collect Result_Dam:
헤드 제거 좌표
  
### UV 경화 속도
  
### UV 경화 시간
  
### UV 경화 위치
## 합착
  
  
  
## 탈포
  
  
12: Machine Tact time Collect Result_Dam:
13: PalletID Collect Result_Dam:
14: Production Qty Collect Result_Dam:
15: Receip No Collect Result_Dam:
16: THICKNESS 1 Collect Result_Dam:
17: THICKNESS 2 Collect Result_Dam:
18: THICKNESS 3 Collect Result_Dam:
19: 1st Pressure Collect Result_AutoClave:
20: 1st Pressure 1st Pressure Unit Time_AutoClave:
21: 2nd Pressure Collect Result_AutoClave:
22: 2nd Pressure Unit Time_AutoClave:
23: 3rd Pressure Collect Result_AutoClave:
24: 3rd Pressure Unit Time_AutoClave:
25: Chamber Temp. Collect Result_AutoClave:
26: Chamber Temp. Unit Time_AutoClave:
27: Chamber Temp. Judge Value_AutoClave:
28: DISCHARGED SPEED OF RESIN Collect Result_Fill1:
29: HEAD NORMAL COORDINATE X AXIS(Stage1) Collect Result_Fill1:
30: HEAD NORMAL COORDINATE X AXIS(Stage2) Collect Result_Fill1:
31: HEAD NORMAL COORDINATE X AXIS(Stage3) Collect Result_Fill1:
32: Head Purge Position Z Collect Result_Fill1:
33: Machine Tact time Collect Result_Fill1:
34: HEAD NORMAL COORDINATE X AXIS(Stage1) Collect Result_Fill2:
35: HEAD NORMAL COORDINATE X AXIS(Stage2) Collect Result_Fill2:
36: HEAD NORMAL COORDINATE X AXIS(Stage3) Collect Result_Fill2:
37: Head Purge Position Z Collect Result_Fill2:
38: Machine Tact time Collect Result_Fill2:
39: target:
40: Set ID:
41: CURE DpS X Collect Result_Dam:
42: CURE DpS Z Collect Result_Dam:
43: CURE DpS Collect Result_Dam:
44: CURE DpS X Collect Result_Fill2:
45: CURE DpS Z Collect Result_Fill2:
46: CURE DpS Collect Result_Fill2:
47: DISCHARGED VpS RESIN(Stage1) Collect Result_Dam:
48: DISCHARGED VpS RESIN(Stage2) Collect Result_Dam:
49: DISCHARGED VpS RESIN(Stage3) Collect Result_Dam:
50: DISCHARGED VpS RESIN(Stage1) Collect Result_Fill1:
51: DISCHARGED VpS RESIN(Stage2) Collect Result_Fill1:
52: DISCHARGED VpS RESIN(Stage3) Collect Result_Fill1:
53: Average Stage1 CL Distance Speed Collect Result_Dam:
54: Average Stage2 CL Distance Speed Collect Result_Dam:
55: Average Stage3 CL Distance Speed Collect Result_Dam:
56: HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Dam:
57: HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Dam:
58: HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Fill1:
59: HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Fill1:
60: HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Fill2:
61: HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Fill2:
  
  
  
### 1. Resin 도포 & 반경화
|   |   |   |
|---|---|---|
|**번호**|**컬럼명**|**컬럼 설명**|
|1|Equipment_Dam|장비 상태를 나타내며, 0은 정상, 1은 비정상으로 표시됩니다.|
|2|Model.Suffix_Dam|모델의 접미사를 통해 차량의 범주를 나누는 식별 값입니다.|
|3|Workorder_Dam|작업 주문의 고유 식별자입니다. 총 664개의 고유 값이 있습니다.|
|4|DISCHARGED SPEED OF RESIN Collect Result_Dam|수지가 방출되는 속도를 나타내며, 3개의 고유 값이 존재합니다.|
|5|HEAD NORMAL COORDINATE X AXIS(Stage1) Collect Result_Dam|1단계 헤드의 X축 좌표를 나타내며, 36개의 고유 값이 있습니다.|
|6|HEAD NORMAL COORDINATE X AXIS(Stage2) Collect Result_Dam|2단계 헤드의 X축 좌표를 나타내며, 38개의 고유 값이 존재합니다.|
|7|HEAD NORMAL COORDINATE X AXIS(Stage3) Collect Result_Dam|3단계 헤드의 X축 좌표를 나타내며, 37개의 고유 값이 존재합니다.|
|8|Head Clean Position Z Collect Result_Dam|헤드 청소 위치의 Z좌표를 나타내며, 5개의 고유 값이 있습니다.|
|9|Head Purge Position Z Collect Result_Dam|헤드 퍼지 위치의 Z좌표를 나타내며, 3개의 고유 값이 있습니다.|
|10|Head Zero Position Y Collect Result_Dam|헤드의 Y좌표 제로 위치를 나타내며, 2개의 고유 값이 존재합니다.|
|11|Head Zero Position Z Collect Result_Dam|헤드의 Z좌표 제로 위치를 나타내며, 2개의 고유 값이 존재합니다.|
|12|Machine Tact time Collect Result_Dam|머신의 작업 시간(택트 타임)을 나타내며, 486개의 고유 값이 있습니다.|
|13|PalletID Collect Result_Dam|각 팔레트의 고유 식별자를 나타내며, 16개의 고유 값이 존재합니다.|
|14|Production Qty Collect Result_Dam|생산량을 나타내며, 609개의 고유 값이 존재합니다.|
|15|Receip No Collect Result_Dam|영수증 번호를 기록하며, 5개의 고유 값이 존재합니다.|
|16|THICKNESS 1 Collect Result_Dam|두께 측정의 첫 번째 값을 나타내며, 7개의 고유 값이 존재합니다.|
|17|THICKNESS 2 Collect Result_Dam|두께 측정의 두 번째 값을 나타내며, 8개의 고유 값이 존재합니다.|
|18|THICKNESS 3 Collect Result_Dam|두께 측정의 세 번째 값을 나타내며, 7개의 고유 값이 존재합니다.|
|19|1st Pressure Collect Result_AutoClave|1차 압력을 나타내며, 27개의 고유 값이 존재합니다.|
|20|1st Pressure 1st Pressure Unit Time_AutoClave|1차 압력의 단위 시간을 나타내며, 9개의 고유 값이 존재합니다.|
### 2. 합착
|   |   |   |
|---|---|---|
|**번호**|**컬럼명**|**컬럼 설명**|
|21|2nd Pressure Collect Result_AutoClave|2차 압력을 나타내며, 68개의 고유 값이 존재합니다.|
|22|2nd Pressure Unit Time_AutoClave|2차 압력의 단위 시간을 나타내며, 10개의 고유 값이 존재합니다.|
|23|3rd Pressure Collect Result_AutoClave|3차 압력을 나타내며, 67개의 고유 값이 존재합니다.|
|24|3rd Pressure Unit Time_AutoClave|3차 압력의 단위 시간을 나타내며, 11개의 고유 값이 존재합니다.|
|25|Chamber Temp. Collect Result_AutoClave|챔버 온도를 나타내며, 26개의 고유 값이 존재합니다.|
|26|Chamber Temp. Unit Time_AutoClave|챔버 온도의 단위 시간을 나타내며, 24개의 고유 값이 존재합니다.|
|27|Chamber Temp. Judge Value_AutoClave|챔버 온도의 판단 값을 나타내며, 2개의 고유 값이 존재합니다.|
|28|DISCHARGED SPEED OF RESIN Collect Result_Fill1|필1에서 방출된 수지의 속도를 나타내며, 4개의 고유 값이 존재합니다.|
|29|HEAD NORMAL COORDINATE X AXIS(Stage1) Collect Result_Fill1|필1의 1단계 헤드 X축 좌표를 나타내며, 11개의 고유 값이 존재합니다.|
|30|HEAD NORMAL COORDINATE X AXIS(Stage2) Collect Result_Fill1|필1의 2단계 헤드 X축 좌표를 나타내며, 21개의 고유 값이 존재합니다.|
|31|HEAD NORMAL COORDINATE X AXIS(Stage3) Collect Result_Fill1|필1의 3단계 헤드 X축 좌표를 나타내며, 12개의 고유 값이 존재합니다.|
|32|Head Purge Position Z Collect Result_Fill1|필1의 퍼지 위치 Z좌표를 나타내며, 3개의 고유 값이 존재합니다.|
|33|Machine Tact time Collect Result_Fill1|필1의 작업 시간(택트 타임)을 나타내며, 384개의 고유 값이 존재합니다.|
### 3. 탈포
|   |   |   |
|---|---|---|
|**번호**|**컬럼명**|**컬럼 설명**|
|34|HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Dam|헤드 Y축 좌표를 나타내며, 20개의 고유 값이 존재합니다.|
|35|HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Dam|헤드 Z축 좌표를 나타내며, 24개의 고유 값이 존재합니다.|
|36|HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Fill1|필1의 헤드 Y축 좌표를 나타내며, 19개의 고유 값이 존재합니다.|
|37|HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Fill1|필1의 헤드 Z축 좌표를 나타내며, 20개의 고유 값이 존재합니다.|
|38|HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Fill2|필2의 헤드 Y축 좌표를 나타내며, 2개의 고유 값이 존재합니다.|
|39|HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Fill2|필2의 헤드 Z축 좌표를 나타내며, 2개의 고유 값이 존재합니다.|
|40|CURE DpS X Collect Result_Dam|CURE 단계에 따른 X축 수치를 나타내며, 10개의 고유 값이 있습니다.|
|41|CURE DpS Z Collect Result_Dam|CURE 단계에 따른 Z축 수치를 나타내며, 10개의 고유 값이 있습니다.|
|42|CURE DpS Collect Result_Dam|CURE 측정을 나타내며, 5개의 고유 값이 존재합니다.|
|43|DISCHARGED VpS RESIN(Stage1) Collect Result_Dam|방출된 수지의 VpS 속도를 나타내며, 24개의 고유 값이 존재합니다.|
|44|DISCHARGED VpS RESIN(Stage2) Collect Result_Dam|방출된 수지의 VpS 속도를 나타내며, 36개의 고유 값이 존재합니다.|
|45|DISCHARGED VpS RESIN(Stage3) Collect Result_Dam|방출된 수지의 VpS 속도를 나타내며, 24개의 고유 값이 존재합니다.|
|46|DISCHARGED VpS RESIN(Stage1) Collect Result_Fill1|필1에서 방출된 VpS 수지의 속도를 나타내며, 9개의 고유 값이 존재합니다.|
|47|DISCHARGED VpS RESIN(Stage2) Collect Result_Fill1|필1에서 방출된 VpS 수지의 속도를 나타내며, 16개의 고유 값이 존재합니다.|
|48|DISCHARGED VpS RESIN(Stage3) Collect Result_Fill1|필1에서 방출된 VpS 수지의 속도를 나타내며, 9개의 고유 값이 존재합니다.|
|49|Average Stage1 CL Distance Speed Collect Result_Dam|평균 거리 속도를 나타내며, 11개의 고유 값이 존재합니다.|
|50|Average Stage2 CL Distance Speed Collect Result_Dam|평균 거리 속도를 나타내며, 15개의 고유 값이 존재합니다.|
|51|Average Stage3 CL Distance Speed Collect Result_Dam|평균 거리 속도를 나타내며, 9개의 고유 값이 존재합니다.|
|52|HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Dam|헤드 Y축 좌표를 나타내며, 20개의 고유 값이 존재합니다.|
|53|HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Dam|헤드 Z축 좌표를 나타내며, 24개의 고유 값이 존재합니다.|
|54|HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Fill1|필1의 헤드 Y축 좌표를 나타내며, 19개의 고유 값이 존재합니다.|
|55|HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Fill1|필1의 헤드 Z축 좌표를 나타내며, 20개의 고유 값이 존재합니다.|
|56|HEAD NORMAL COORDINATE Y AXIS(Stage) Collect Result_Fill2|필2의 헤드 Y축 좌표를 나타내며, 2개의 고유 값이 존재합니다.|
|57|HEAD NORMAL COORDINATE Z AXIS(Stage) Collect Result_Fill2|필2의 헤드 Z축 좌표를 나타내며, 2개의 고유 값이 존재합니다.|