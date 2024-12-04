![[Ch5_Clustering_page-0001.jpg]]
그룹을 어떻게 지을 것인가? -> 클러스터링

![[Ch5_Clustering_page-0002.jpg]]
## Hierarchical Clustering(Agglomerative Clustering)

![[Ch5_Clustering_page-0003.jpg]]

![[Ch5_Clustering_page-0004.jpg]]

![[Ch5_Clustering_page-0005.jpg]]

![[Ch5_Clustering_page-0006.jpg]]

![[Ch5_Clustering_page-0007.jpg]]

![[Ch5_Clustering_page-0008.jpg]]

![[Ch5_Clustering_page-0009.jpg]]

![[Ch5_Clustering_page-0010.jpg]]

![[Ch5_Clustering_page-0011.jpg]]

![[Ch5_Clustering_page-0012.jpg]]

![[Ch5_Clustering_page-0013.jpg]]

![[Ch5_Clustering_page-0014.jpg]]

![[Ch5_Clustering_page-0015.jpg]]

![[Ch5_Clustering_page-0016.jpg]]

![[Ch5_Clustering_page-0017.jpg]]

![[Ch5_Clustering_page-0018.jpg]]
클러스터 구하고 mean을 구함 
mean으로부터 variance를 구함
variance가 작아지도록 클러스터링을 하는 방식이다.

![[Ch5_Clustering_page-0019.jpg]]

![[Ch5_Clustering_page-0020.jpg]]

![[Ch5_Clustering_page-0021.jpg]]

![[Ch5_Clustering_page-0022.jpg]]
계산량이 상당히 많다는 것을 알 수 있다.
대신 클러스터링 결과는 준수하다.

![[Ch5_Clustering_page-0023.jpg]]

![[Ch5_Clustering_page-0024.jpg]]
## Partitional Clustering
k개의 클러스터 값(시드)을 정하고 시작한다.
첫 샘플이 시드 중 어디에 가장 가까운지 계산 후 그 곳으로 포함시킨다.
이후 시드의 위치를 업데이트한다.

![[Ch5_Clustering_page-0025.jpg]]

![[Ch5_Clustering_page-0026.jpg]]

![[Ch5_Clustering_page-0027.jpg]]

![[Ch5_Clustering_page-0028.jpg]]
### k-means Algorithm
샘플이 하나 들어갈 때 마다 샘플이 업데이트 된다.
훨씬 빠르게 클러스터링이 가능하다.
![[Ch5_Clustering_page-0029.jpg]]

![[Ch5_Clustering_page-0030.jpg]]

![[Ch5_Clustering_page-0031.jpg]]

![[Ch5_Clustering_page-0032.jpg]]

![[Ch5_Clustering_page-0033.jpg]]