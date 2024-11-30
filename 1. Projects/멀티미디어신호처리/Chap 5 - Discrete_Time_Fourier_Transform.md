


## 1차시(12w-2)
*복습*
지난 시간은 time domain 분석 기법을 살펴봤다.(convolution, cross correlation 등 기법들은 time domain에서 유용하게 사용된다.)
DSP 대부분은 frequency domain 분석을 사용한다. 이제 살펴보자

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0001.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0002.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0003.jpg]]
Frequency spectrum은 우리가 알고시펑 하


![[DSPChap5_Discrete_Time_Fourier_Transform_page-0004.jpg]]
$\Omega$는 radian frequency이다.
	$\Omega = 2\pi F$
x라는 스펙트럼이 finite할 때 DTFT를 적용할 수 있다.
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0005.jpg]]
오타: $H(\Omega)$가 아니라 $x(\Omega)$이다.
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
1. DTFT X(오메가)는 2파이 주기르 ㄹ가진다
	1. 주 주기는 -파이부터 파이까지이다.
2. 라디안 프리퀀시는 디지털 프리퀀시와 2파이를 곱한 관계가 있고 디지털 프리퀀시는 아날로그 프리쿼시를 나눈것과 관계가 있다.
![[DSPChap5_Discrete_Time_Fourier_Transform_page-0012.jpg]]
**오일러의 항등식**

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0013.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0014.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0015.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0016.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0017.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0018.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0019.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0020.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0021.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0022.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0023.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0024.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0025.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0026.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0027.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0028.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0029.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0030.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0031.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0032.jpg]]
