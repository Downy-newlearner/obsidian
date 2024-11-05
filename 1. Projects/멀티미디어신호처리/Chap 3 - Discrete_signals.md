---
created: 2024-11-04 00:57
week: 9W
---
 ![[DSPChap3_Discrete_Signals_page-0001.jpg]]

![[DSPChap3_Discrete_Signals_page-0002.jpg]]

![[DSPChap3_Discrete_Signals_page-0003.jpg]]
신호 분류
x축과 y축이 각각 연속적 / 이산적인지 여부에 따라 4가지로 구분할 수 있다.(a~d)

PCA
	Sampling & Quantization
	a -> c -> d 과정이 PCA이다.

![[DSPChap3_Discrete_Signals_page-0004.jpg]]

![[DSPChap3_Discrete_Signals_page-0005.jpg]]
수학적인 표현을 간편하게 하기 위해서 $T_s$를 1로 가정한다.
하지만 일반적으로 $T_s\neq1$이다.

![[DSPChap3_Discrete_Signals_page-0006.jpg]]

![[DSPChap3_Discrete_Signals_page-0007.jpg]]
에너지 값이 유한한지, 무한한지로 Energy Signal / Power Signal을 구분한다.
Energy signal은 파워를 측정할 수 없으므로, Average power를 사용하여 비교한다.
![[DSPChap3_Discrete_Signals_page-0008.jpg]]

![[DSPChap3_Discrete_Signals_page-0009.jpg]]
주기함수를 더하면 원래는 주기함수이다.(아날로그 신호에서)
하지만 이산 신호에서 주기함수끼리 더해도 주기함수가 아니다.

sin함수는 주기가 $2\pi$이므로 $\frac{3\pi N_1}{4} = 2\pi k$라면 
![[DSPChap3_Discrete_Signals_page-0010.jpg]]

![[DSPChap3_Discrete_Signals_page-0011.jpg]]

![[DSPChap3_Discrete_Signals_page-0012.jpg]]

![[DSPChap3_Discrete_Signals_page-0013.jpg]]

![[DSPChap3_Discrete_Signals_page-0014.jpg]]

![[DSPChap3_Discrete_Signals_page-0015.jpg]]

![[DSPChap3_Discrete_Signals_page-0016.jpg]]

![[DSPChap3_Discrete_Signals_page-0017.jpg]]

![[DSPChap3_Discrete_Signals_page-0018.jpg]]

![[DSPChap3_Discrete_Signals_page-0019.jpg]]

![[DSPChap3_Discrete_Signals_page-0020.jpg]]

![[DSPChap3_Discrete_Signals_page-0021.jpg]]

![[DSPChap3_Discrete_Signals_page-0022.jpg]]

![[DSPChap3_Discrete_Signals_page-0023.jpg]]

![[DSPChap3_Discrete_Signals_page-0024.jpg]]

![[DSPChap3_Discrete_Signals_page-0025.jpg]]

![[DSPChap3_Discrete_Signals_page-0026.jpg]]

![[DSPChap3_Discrete_Signals_page-0027.jpg]]

![[DSPChap3_Discrete_Signals_page-0028.jpg]]

![[DSPChap3_Discrete_Signals_page-0029.jpg]]

![[DSPChap3_Discrete_Signals_page-0030.jpg]]

![[DSPChap3_Discrete_Signals_page-0031.jpg]]

![[DSPChap3_Discrete_Signals_page-0032.jpg]]

![[DSPChap3_Discrete_Signals_page-0033.jpg]]

![[DSPChap3_Discrete_Signals_page-0034.jpg]]

![[DSPChap3_Discrete_Signals_page-0035.jpg]]

![[DSPChap3_Discrete_Signals_page-0036.jpg]]

![[DSPChap3_Discrete_Signals_page-0037.jpg]]

![[DSPChap3_Discrete_Signals_page-0038.jpg]]

![[DSPChap3_Discrete_Signals_page-0039.jpg]]

![[DSPChap3_Discrete_Signals_page-0040.jpg]]

![[DSPChap3_Discrete_Signals_page-0041.jpg]]