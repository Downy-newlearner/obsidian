---
created: 2024-11-04 00:57
week: 9W
---
 
# 1차시
**수업 내용 정리**
- Signal Classification and discrete signals
	- 시그널은 연속-연속, 연속-이산, 이산-연속, 이산-이산(x축-y축)
	- 아날로그 신호: 연속-연속
	- 디지털 신호: 이산-이산
	- 수업에서 다루는 신호: 이산-연속(discrete signals라고 부른다.)
- Signal measure
	- ***signal energy***(신호 에너지)를 정의했다.
		- ![[Pasted image 20241105154446.png]]
		- Energy Signal: 유한한 신호에너지를 가지는 시그널
		- Power Signal: 무한한 신호에너지를 가지는 시그널
	- ***Average Power***
		- ![[Pasted image 20241105154748.png]]
		- 무한한 신호에너지를 가지는 주기함수는 Average power로 정리한다.
- Digital signal operations
	1. Time delay(shift)
		$x[n] -> x[n+k]$
	2. Time reverse
		$x[n] -> x[-n]$
	3. Time delayed time reversal(1,2번 연산 둘 다 함)
		$y[n]=x[-n-a]$

	4. Time scaling
		- compress
		- expand
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

sin함수는 주기가 $2\pi$이므로 $\frac{3\pi N_1}{4} = 2\pi k$이면 되고, $N_1$과 $k$는 정수이므로 이를 만족하는 $N_1 = 8, k = 3$이다. $\therefore$주기는 8이다.
	**다른 풀이**
		$sin(\frac{3\pi n}{4})의 주기는 $\frac{8}{3}$이다. 하지만 이 예시에서는 정수 주기를 찾는 것이 목표이므로 정수 주기는 8이 된다.
![[DSPChap3_Discrete_Signals_page-0010.jpg]]

## 기본 이산 시그널 연산들
![[DSPChap3_Discrete_Signals_page-0011.jpg]]
time delay
![[DSPChap3_Discrete_Signals_page-0012.jpg]]
time reversal(mirror image)
![[DSPChap3_Discrete_Signals_page-0013.jpg]]
time delayed and time reversal
![[DSPChap3_Discrete_Signals_page-0014.jpg]]

![[DSPChap3_Discrete_Signals_page-0015.jpg]]
기본 이산 시그널 연산 2: time scaling
1. Compress
	compress는 $\alpha$가 짝수면 $X[n]$에서 n이 홀수일 때, 홀수면 n이 짝수일 때를 버려버린다.

2. EXpand
	중간에 0인 값을 삽입한다.
![[DSPChap3_Discrete_Signals_page-0016.jpg]]
Expansion을 한 후 LPF를 통과시키면 삽입되는 값들이 0이 아니라 양옆의 평균값이 된다.
그래서 더욱 부드러운 구조가 나타난다.
![[DSPChap3_Discrete_Signals_page-0017.jpg]]

# 2차시
![[DSPChap3_Discrete_Signals_page-0018.jpg]]
자주 사용하는 discrete signals


**Inpulse Functions**
현실에서는 만들 수는 없으나, 수학 연산에서 편하게 사용할 수 있는 함수이다.
![[DSPChap3_Discrete_Signals_page-0019.jpg]]

![[DSPChap3_Discrete_Signals_page-0020.jpg]]
모든 이산 시그널은 inpulse function으로 표현할 수 있다.
![[DSPChap3_Discrete_Signals_page-0021.jpg]]

![[DSPChap3_Discrete_Signals_page-0022.jpg]]
**Unit step function**
0보다 크거나 같은은 input에 대해 1을 output하는 함수이다.
![[DSPChap3_Discrete_Signals_page-0023.jpg]]
unit step function을 합성해서 함수를 조작할 수 있다.
![[DSPChap3_Discrete_Signals_page-0024.jpg]]

![[DSPChap3_Discrete_Signals_page-0025.jpg]]
unit step function을 ==곱하거나 빼서== rectangle pulse를 만들 수 있다.
![[DSPChap3_Discrete_Signals_page-0026.jpg]]

![[DSPChap3_Discrete_Signals_page-0027.jpg]]
복소수가 포함된 exponential function은 $cos, sin$으로 표현할 수 있다.
![[DSPChap3_Discrete_Signals_page-0028.jpg]]
[[Aliasing]]은 $f_s$(sampling rate)가 충분히 크지 않아서, 즉 $T_s$(sampling period)가 충분히 짧지 않아서 원본 신호의 정보를 잘못 해석하거나 왜곡하는 것이다.

이전에 우리가 본 adc - [[dsp]] - dac 표에서 앞 뒤에 필터 2개가 추가됐다.
![[DSPChap3_Discrete_Signals_page-0029.jpg]]

![[DSPChap3_Discrete_Signals_page-0030.jpg]]

![[DSPChap3_Discrete_Signals_page-0031.jpg]]
**[[나이퀴스트 샤논 샘플링 이론]]**

![[DSPChap3_Discrete_Signals_page-0032.jpg]]

![[DSPChap3_Discrete_Signals_page-0033.jpg]]
나이퀴스트 샘플링 조건을 만족하지 않으면 [[Aliasing]] effect가 발생할 수 있다.
이를 방지하기위해 [[안티 앨리어싱 필터|anti-aliasing filter]]를 사용한다.
![[DSPChap3_Discrete_Signals_page-0034.jpg]]
위와 같은 경우에는 $f_{max}$를 어떻게 잡아야하나? 무한대 아닌가? -> 아니다 유효한 [[주파수]]가 있다.

![[DSPChap3_Discrete_Signals_page-0035.jpg]]
음악 신호는 보통 sampling rate가 44.1k

sampling rate를 8kHZ로 정한다면 주파수가 4kHZ 이상인 신호들은 [[안티 앨리어싱 필터]]로 제거한다.
![[DSPChap3_Discrete_Signals_page-0036.jpg]]

![[DSPChap3_Discrete_Signals_page-0037.jpg]]

![[DSPChap3_Discrete_Signals_page-0038.jpg]]

![[DSPChap3_Discrete_Signals_page-0039.jpg]]

![[DSPChap3_Discrete_Signals_page-0040.jpg]]

![[DSPChap3_Discrete_Signals_page-0041.jpg]]