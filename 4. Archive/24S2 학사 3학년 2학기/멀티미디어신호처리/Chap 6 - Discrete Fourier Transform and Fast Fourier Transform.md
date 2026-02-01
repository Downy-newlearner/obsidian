---
Lecture date: 2024-12-06
tags:
  - 멀티미디어신호처리
---
*복습*
시그널 처리는 대부분 frequency domian
타임 도메인에서 하는 건 컨볼루션, 코렐레이션이다.(나머지는 프리퀀시에서)
100퍼센트 맞는 분석 기법은 DTFT이다. 하지만 연속적이라 컴퓨터로 처리가 불가능


# 1차시
![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0001.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0002.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0003.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0004.jpg]]
F는 디지털 프리퀀시

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0005.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0006.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0007.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0008.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0009.jpg]]
중요 프로퍼티
DTFT는 주기를 가지고있다: 2$\pi$
DFT는 N포인트로 어프로치하니까 주기가 N포인트 주기
수식을 정리하면 
	![[Pasted image 20241206200943.png]]
	얘가 1이 되면 한 주기 성립
	그래서 DFT는 주기가 N이다.

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0010.jpg]]
인버스 트랜스폼은 기억하지 않아도 좋다

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0011.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0012.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0013.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0014.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0015.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0016.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0017.jpg]]





![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0018.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0019.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0020.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0021.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0022.jpg]]



# 2차시
복습
FFT는 DFT를 실시간으로 연산할 수 있는 아록리즘이다.(1966)
유닛 서클 다시 보기

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0023.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0024.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0025.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0026.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0027.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0028.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0029.jpg]]

### DIT FFT 예제
![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0030.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0031.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0032.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0033.jpg]]
stage를 지날 때마다 다음 스테이지의 올바른 순서로 입력하기 위한 과정이 필요하다.(다음 슬라이드)

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0034.jpg]]
bit reversing을 하면 공교롭게도 순서가 맞는다.



## DFT vs FFT 연산 속도 비교
![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0035.jpg]]




![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0036.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0037.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0038.jpg]]
Chap4에서 컨볼루션, 코레스폰딩을 타임 도메인에서 했는데, 이는 연산량이 많아서 보통은 frequency domain에서 FFT를 이용한다.

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0039.jpg]]



## FFT 예제
![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0040.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0041.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0042.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0043.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0044.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0045.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0046.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0047.jpg]]

![[DSPChap6_Discrete_Fourier_Transform_and_Fast_Fourier_Transform_page-0048.jpg]]