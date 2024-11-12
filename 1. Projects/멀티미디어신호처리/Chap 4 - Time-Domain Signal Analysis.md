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
	[[SNR|Signal to Noise Ratio]](SNR)로 [[Quantization]]의 성능을 표현한다.


	$SNG(dB) = 6.02N + 1.76 dB ~= 6N$
	
**예시**
![[Pasted image 20241104152823.png|300]]

DA converter
	anti imaging filter는 LPF이다.
	간단히 읽어만 보면 된다.



## 1차시
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
Time-invariance
	시스템의 특성이 시간에 따라 변하지 않음을 나타낸다.
	$x[n] -> y[n]$인 시스템에서 n을 $n_0$만큼 딜레이 시켰을 때 y에서도 $n_0$만큼 딜레이된다면 time invariance하다고 한다.
![[DSPChap4_Time_Domain_Signal_Analysis_page-0007.jpg]]
태블릿 필가 참고
![[DSPChap4_Time_Domain_Signal_Analysis_page-0008.jpg]]
이번학기에서는 시스템을 [[LTI]]를 가정한다.(그래야 간단히 계산할 수 있다.)
이렇게 가정한다면 $y[n] = x[n]*h[n]$으로 구할 수 있다.(\*는 convolution이다.)
discrete time signal의 수학적 특성을 나타낸 것을 $h[n]$이라고 한다.


### [[LTI|LTI 시스템]]의 특성
1. Causality(인과성)
2. Stability
![[DSPChap4_Time_Domain_Signal_Analysis_page-0009.jpg]]
어떤 시점의 출력은 과거에 의존한다.(미래에 의존하지 않는다.)
causality를 따르는 시스템만이 구현이 가능하다.

![[DSPChap4_Time_Domain_Signal_Analysis_page-0010.jpg]]
## 2차시
**복습**
- LTI 시스템
	- Causality: 미래가 아닌 과거를 기반으로 결과를 도출해야한다.
		- non causal system은 구현이 불가능하다.
![[DSPChap4_Time_Domain_Signal_Analysis_page-0011.jpg]]
**BIBO**: 입력이 유한하면 출력이 유한하게 유지되는 시스템의 특성
	- Input이 한정되어있으면, Output도 한정된 값 안에서 나와야한다.

**핵심 디테일**

- **BIBO 안정성 정의**: 유한한 입력은 유한한 출력을 보장해야 함.
- **[[LTI|LTI 시스템]]에서의 조건**: 임펄스 응답의 절대 합이 유한하면 BIBO 안정성이 유지됨.
- **안정성 수식**: $\sum_{k=-\infty}^{\infty} |h[k]| < \infty$이면 안정성 확보
![[DSPChap4_Time_Domain_Signal_Analysis_page-0012.jpg]]
임펄스 응답이 $h[n] = a^n u[n]$일 때, 시스템은 $|a| < 1$일 경우에 안정적입니다. (무한등비급수가 수렴할 조건)


![[DSPChap4_Time_Domain_Signal_Analysis_page-0013.jpg]]
시스템을 Impulse response로 표현하느냐, Difference equation(입력과 출력의 관계식)으로 표현하냐에 따라서 분석하는 방법이 달라진다.(분석이 다를 수 있지만 동일한 시스템을 이야기하는 것이다.)
두 번째 방법을 확인해보자
	recursive / non recursive를 구분하는 것이 중요하다.

![[DSPChap4_Time_Domain_Signal_Analysis_page-0014.jpg]]
출력 y는 입력 뿐만 아니라 과거의 출력에도 의존한다. 
	이를 Recursive system(재귀 시스템), IIR이라고 부른다.

![[DSPChap4_Time_Domain_Signal_Analysis_page-0015.jpg]]
non recursive system을 FIR이라고 부른다.

![[DSPChap4_Time_Domain_Signal_Analysis_page-0016.jpg]]
임펄스 응답은 시스템이 단위 임펄스 입력에 반응하여 생성하는 출력이다.
FIR과 IIR 시스템의 구분은 임펄스 응답의 길이에 따라 결정된다.
	- FIR은 유한 길이의 임펄스 응답을 가짐
	- IIR은 무한 길이의 임펄스 응답을 가짐

Impulse response
	어떤 unknown 시스템이 있다고 하자.
	그 시스템에 impulse function을 입력하고 출력을 측정하면 이것이 inpulse response이다.

inpulse function은 singularity function이다. 
이것은 인공적으로 만들어낸 함수이다.(순간 확 튀는 함수는 존재하지 않음)
그러므로 적당히 inpulse function에 유사한 함수를 unknown 시스템에 입력해서 그 시스템을 추측한다.

| 특징            | FIR (Finite Impulse Response) | IIR (Infinite Impulse Response) |
| ------------- | ----------------------------- | ------------------------------- |
| **임펄스 응답 길이** | 유한 (finite)                   | 무한 (infinite)                   |
| **구조**        | 비재귀적 (Non-recursive)          | 재귀적 (Recursive)                 |
| **출력 의존성**    | 과거 입력에만 의존                    | 과거 입력과 출력에 모두 의존                |
| **안정성**       | 항상 안정적                        | 계수에 따라 불안정할 수 있음                |
| **인과성**       | 항상 인과적                        | 인과적 또는 비인과적일 수 있음               |
| **설계 복잡도**    | 일반적으로 간단함                     | 상대적으로 복잡함                       |
| **연산 효율성**    | 더 많은 계수를 필요로 하여 연산이 상대적으로 느림  | 적은 계수로 동일 효과를 낼 수 있어 연산이 빠름     |
| **위상 반응**     | 선형 위상(Linear Phase) 구현 가능     | 선형 위상 구현 어려움                    |
| **응용 예시**     | 오디오 신호 필터, 디지털 통신 필터          | 아날로그 필터의 디지털 구현, 제어 시스템 필터      |




![[DSPChap4_Time_Domain_Signal_Analysis_page-0017.jpg]]
이 시스템은 non recursive 시스템이다.
	왜냐하면 이 함수는 입력에만 의존하기 때문이다.

입력 $x[n]$, 그리고 출력 $y[n]$를 알기 위해서는 시스템에 대해서 알아야한다.
그래서 입력에 Inpulse function을 넣어 시스템을 추측한다.
	$x[n] = \delta[n]$
	결과를 확인해보니 결과는 finite impulse response이다.
	그러므로 이 시스템은 FIR system이다.
	
이 시스템은 causal 시스템이다.
	$h[n] = 0 (n<0)$
	
![[DSPChap4_Time_Domain_Signal_Analysis_page-0018.jpg]]
FIR 시스템의 임펄스 응답은 유한 길이를 가지며 그래프에서 유한한 범위 내에서만 값이 존재한다.

![[DSPChap4_Time_Domain_Signal_Analysis_page-0019.jpg]]
이 시스템은 출력이 과거에 의존한다.

마찬가지로 입력에 Inpulse function을 넣어서 확인해보니 위와 같다.
	$h[0] = 0.4h[-1] + \delta[0] - \delta[-1] = 0 + 1 - 0 = 1 (\because h[-1] = 0)$
	$h[1] = 0.4h[0] + \delta[1] - \delta[0] = 0.4 + 0 - 1 = -0.6$
$0.4h[n-1]$이라는 피드백이 존재하므로 Infinite Impulse response이다.


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