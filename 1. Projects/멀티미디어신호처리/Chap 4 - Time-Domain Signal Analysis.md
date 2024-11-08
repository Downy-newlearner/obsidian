---
created: 2024-11-04 00:57
week: 10W
---
**복습**
anti 앨리어싱 필터
sample rate >= 2 B(만족하지 못하면 앨리어싱 에러가 발생한다.)

Quantization error and [[SNR]]
	컴퓨터가 표현할 수 있는 값에 제한이 있어서 truncation하는 중에 발생하는 에러
	비트 수를 늘리면 에러가 줄지만 자원이 많이 든다는 trade-off가 있다.
	[[SNR|Signal to Noise Ratio]](SNR)로 Quantization의 성능을 표현한다.
	$$SNG(dB) = 6.02N + 1.76 dB ~= 6N$$
	**예시**
	![[Pasted image 20241104152823.png|300]]

DA converter
	anti imaging filter는 LPF이다.
	간단히 읽어만 보면 된다.
![[DSPChap4_Time_Domain_Signal_Analysis_page-0001.jpg]]
신호를 분석하는 것을 frequency domain에서 수행한다.
![[DSPChap4_Time_Domain_Signal_Analysis_page-0002.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0003.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0004.jpg]]
**Discrete time system의 속성 1**
Additivity

![[DSPChap4_Time_Domain_Signal_Analysis_page-0005.jpg]]
**Discrete time system의 속성 2, 3**
Homogeneity
Linearity

Discrete time system은 Linear Operation이다.
![[DSPChap4_Time_Domain_Signal_Analysis_page-0006.jpg]]
**Discrete time system의 속성 4**
Time-invariance(십시 불변성)
$x[n] -> y[n]$인 시스템에서 n을 $n_0$만큼 딜레이 시켰을 때 y에서도 $n_0$만큼 딜레이된다면 time invariance하다고 한다.
![[DSPChap4_Time_Domain_Signal_Analysis_page-0007.jpg]]
태블릿 필가 참고
![[DSPChap4_Time_Domain_Signal_Analysis_page-0008.jpg]]
이번학기에서는 시스템을 LTI를 가정한다.(그래야 간단히 계산할 수 있다.)
이렇게 가정한다면 $y[n] = x[n]*h[n]$으로 구할 수 있다.(\*는 convolution이다.)
discrete time signal의 수학적 특성을 나타낸 것을 $h[n]$이라고 한다.


## LTI 시스템의 특성
1. Causality(인과성)
2. Stability
![[DSPChap4_Time_Domain_Signal_Analysis_page-0009.jpg]]
어떤 시점의 출력은 과거에 의존한다.(미래에 의존하지 않는다.)
causality를 따르는 시스템만이 구현이 가능하다.

![[DSPChap4_Time_Domain_Signal_Analysis_page-0010.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0011.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0012.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0013.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0014.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0015.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0016.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0017.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0018.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0019.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0020.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0021.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0022.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0023.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0024.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0025.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0026.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0027.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0028.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0029.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0030.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0031.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0032.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0033.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0034.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0035.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0036.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0037.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0038.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0039.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0040.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0041.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0042.jpg]]

![[DSPChap4_Time_Domain_Signal_Analysis_page-0043.jpg]]