### 데이터 샘플 (head) ###
 Date   Open   High    Low  Close     Volume  Name
0  2006-01-03  26.25  27.00  26.10  26.84   79974418  MSFT
1  2006-01-04  26.77  27.08  26.77  26.97   57975661  MSFT
2  2006-01-05  26.96  27.13  26.91  26.99   48247610  MSFT
3  2006-01-06  26.89  27.00  26.49  26.91  100969092  MSFT
4  2006-01-09  26.93  27.07  26.76  26.86   55627836  MSFT

### 데이터 타입 (dtypes) ###
Date       object
Open      float64
High      float64
Low       float64
Close     float64
Volume      int64
Name       object
dtype: object

### 데이터의 날짜 범위 (Date.min(), Date.max()) ###
최소 날짜: 2006-01-03 00:00:00
최대 날짜: 2017-12-29 00:00:00

### 결측치 확인 (isnull().sum()) ###
Date      0
Open      0
High      0
Low       0
Close     0
Volume    0
Name      0
dtype: int64

### 데이터 칼럼 이름 ###
Index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'], dtype='object')
