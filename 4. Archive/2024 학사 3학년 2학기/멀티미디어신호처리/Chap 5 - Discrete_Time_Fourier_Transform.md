                                                                                                    


## 1차시(12w-2)
*복습*
지난 시간은 time domain 분석 기법을 살펴봤다.(convolution, cross correlation 등 기법들은 time domain에서 유용하게 사용된다.)
DSP 대부분은 frequency domain 분석을 사용한다. 이제 살펴보자

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0001.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0002.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0003.jpg]]
Frequency spectrum은 우리가 알고싶어 하는 대부분의 정보를 가지고있다.
그래서 신호 분석은 대부분 frequency domain에서 한다.


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0004.jpg]]
$\Omega$는 [[radian frequency]]이다.
	$\Omega = 2\pi F$
$F$는 Digital frequency이다.
$f$는 Analog frequency이다.

x라는 스펙트럼이 finite할 때 DTFT를 적용할 수 있다.


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0005.jpg]]
오타: $H(\Omega)$가 아니라 $X(\Omega)$이다.


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0006.jpg]]
DTFT가 만들어낸 연속적인 것을 컴퓨터를 이용해 처리할 수 없기 때문에 이산적으로 근사시켜야한다.
그래서 DFT를 사용한다.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0007.jpg]]
DFT를 이용하여 이산값으로 근사는 성공했지만, 이 방법은 신호 처리에 시간이 걸려서 실시간으로 처리할 수 없다.
그래서 FFT를 사용한다.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0008.jpg]]
FFT는 에러가 존재할 수 밖에 없고, 이 에러를 줄이려면 n을 늘려서 더 촘촘하게 이산시키면 된다.
N은 보통 256~2048 정도로 설정한다.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0009.jpg]]
Impulse function(Singularity function이라고도 부름)은 White spectrum이라고 부른다.
white spectrum과 대비되는 개념으로는 colored specturm이라고 한다.
 
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0010.jpg]]
수식1과 수식3은 많이 사용되므로 기억해두는 것이 좋다.
1. 어떤 Discrete sequence가 $n_0$만큼 딜레이되면 exponential 형태로 $n_0$텀이 나온다.
2. 어떤 $\alpha^n u[n]$ 형태의 DTFT는 수식 3과 같이 나온다.
이 두가지는 기억하자.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0011.jpg]]
### DTFT Properties 1: Periodicity
*기억해야할 것*
1. DTFT X(오메가)는 2파이 주기를 가진다
	1. 주 주기는 -파이부터 파이까지이다.
2. 라디안 프리퀀시는 디지털 프리퀀시와 2파이를 곱한 관계가 있고 디지털 프리퀀시는 아날로그 프리쿼시를 나눈것과 관계가 있다.
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0012.jpg]]
**오일러의 항등식**

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0013.jpg]]
*Shifting Property 증명*
![[Pasted image 20241208210140.png]]


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0014.jpg]]
## 2차시(13w-1)
*복습*
이론적으로 철저한 기법은 DTFT지만 DTFT는 아웃풋이 연속적인 frequency spectrum이므로 DFT를 이용해 이산적으로 근사를 한 후에 컴퓨터에서 사용할 수 있다.
DFT는 여전히 연산량이 많아 FFT를 통해 빠르게, 실시간으로 연산할 수 있는 알고리즘이 등장했다.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0015.jpg]]
*Convolution의 DTFT는 두 인수를 DTFT한 것의 곱과 같다.*

y[n]을 구하는 방법
	1. $X[\Omega], H[\Omega]$를 구한다.
	2. 출력 DTFT는 구한 두 텀을 곱한 것과 같다.
	3. 구한 $Y[\Omega]$의 inverse DTFT를 구해서 $y[n]$을 구한다.

이 과정을 사용하는 이유는 연산 속도가 빠르다.
	왜냐하면 이 DTFT 연산은 결국 FFT를 이용하기 때문이다.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0016.jpg]]
### Frequency Response
frequency response는 time domain에서 Impulse response의 DTFT이다.
이는 주어진 시스템의 특성을 반영하므로 매우 중요하다.


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0017.jpg]]
- Frequency response 구하는 방법 2가지
	1. impulse response가 주어져있다면 이로부터 DTFT를 취해서 구한다.
	2. 입력과 출력의 관계식으로부터 $Y[\Omega]$를 구한다.
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0018.jpg]]
frequency response는 복소함수이다.
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0019.jpg]]
$|H(\Omega)|$로 그래프를 그리기도 하고, 여기에 로그를  붙여서 그리기도 한다.
로그를 붙여 확인하는 그래프는, 필터의 특징을 잘 보여줘서 자주 사용된다.

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0020.jpg]]
시스템 표현에는 2가지 방법이 있다.
Impulse Response, Difference Equation
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0021.jpg]]


## 3차시(13w-2)
**복습**
Frequency Response는 주어진 descrete time system의 주파수 특징을 설명하는 함수이다.
time domain에서 ipmulse resopnse의 dtft이다.
주어진 시스템의 frequency response를 구하는 2가지 방법
1.  $h[n]$에서 DTFT를 취하는 방법
2. 입출력의 관계식(Difference Equation)의 양변을 DTFT하여 X(오메가)와 Y(오메가)의 비율을 구한다.

FR는 complex function이어서 real 파트와 imagenary 파트로 나뉠 수 있다.
또한 magnitude와 phase 파트로 나뉠 수 있다.(p. 18)

Magnitude resopnse를 구하는 방법
1. 절댓값을 취해 그리는 방법
2. 절댓값 취하고 로그를 취해 그리는 방법
	- 이 경우에는 작은 값을 잘 표현하므로 stop band의 성능을 볼 수있는 장점이 있다.


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0022.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0023.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0024.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0025.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0026.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0027.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0028.jpg]]
comb 필터라고 한다.
	잔향을 만들어내는 필터이다.
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0029.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0030.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0031.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0032.jpg]]
