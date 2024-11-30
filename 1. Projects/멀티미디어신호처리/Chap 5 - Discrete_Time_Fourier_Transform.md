


## 1차시(12w-2)
*복습*
지난 시간은 time domain 분석 기법을 살펴봤다.(convolution, cross correlation 등 기법들은 time domain에서 유용하게 사용된다.)
DSP 대부분은 frequency domain 분석을 사용한다. 이제 살펴보자

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0001.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0002.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0003.jpg]]
Frequency spectrum은 


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

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0008.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0009.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0010.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0011.jpg]]

![[DSPChap5_Discrete_Time_Fourier_Transform_page-0012.jpg]]

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
