#### 딥러닝&파이썬 용어 정리
|책 이름|챕터/날짜|이름|설명|
|---|---|---|---|
|딥러닝/클라우드||[[시계열 데이터]]|데이터의 변화가 시간의 변화에 따라 표현되는 데이터|
|딥러닝/클라우드||[[Gini impurity]]||
  
  
![[chap07_FS_stacking_page-0001.jpg]]
![[chap07_FS_stacking_page-0002.jpg]]
![[chap07_FS_stacking_page-0003.jpg]]
![[chap07_FS_stacking_page-0004.jpg]]
![[chap07_FS_stacking_page-0005.jpg]]
영역의 크기를 impurity라고 한다.
겹치는 부분이 적을 수록 구분이 클래스 구분을 잘 하는 피처이고, 이런 피처들을 선택해서 사용한다.
  
![[chap07_FS_stacking_page-0006.jpg]]
![[chap07_FS_stacking_page-0007.jpg]]
팀워크까지 고려하면 1등, 2등, 5등으로 구성하는 것이 1등, 2등, 3등으로 구성하는 것보다 성능이 좋을 수 있다.
filter method 이름의 의미는 안좋은 피처를 골라낸다는 것이다.
![[chap07_FS_stacking_page-0008.jpg]]
![[chap07_FS_stacking_page-0009.jpg]]
![[chap07_FS_stacking_page-0010.jpg]]
카이제곱 또는 뮤추얼 인포를 이용해서 피처 셀렉션을 할 수 있다.
![[chap07_FS_stacking_page-0011.jpg]]
![[chap07_FS_stacking_page-0012.jpg]]
k개를 셀렉트하는데 지금 코드는 전체를 셀렉트 한다는 의미이다.
이것의 역할은 피처의 랭킹을 알 수 있다.
![[chap07_FS_stacking_page-0013.jpg]]
![[chap07_FS_stacking_page-0014.jpg]]
![[chap07_FS_stacking_page-0015.jpg]]
![[chap07_FS_stacking_page-0016.jpg]]
![[chap07_FS_stacking_page-0017.jpg]]
![[chap07_FS_stacking_page-0018.jpg]]
SFS: Sequential Feature Selection
전진, 후진 피처 셀렉션을 모두 지원하는 효율 좋은 알고리즘이다.
![[chap07_FS_stacking_page-0019.jpg]]
![[chap07_FS_stacking_page-0020.jpg]]
![[chap07_FS_stacking_page-0021.jpg]]
![[chap07_FS_stacking_page-0022.jpg]]
![[chap07_FS_stacking_page-0023.jpg]]
![[chap07_FS_stacking_page-0024.jpg]]
![[chap07_FS_stacking_page-0025.jpg]]
![[chap07_FS_stacking_page-0026.jpg]]
![[chap07_FS_stacking_page-0027.jpg]]
![[chap07_FS_stacking_page-0028.jpg]]
![[chap07_FS_stacking_page-0029.jpg]]
![[chap07_FS_stacking_page-0030.jpg]]
![[chap07_FS_stacking_page-0031.jpg]]
![[chap07_FS_stacking_page-0032.jpg]]