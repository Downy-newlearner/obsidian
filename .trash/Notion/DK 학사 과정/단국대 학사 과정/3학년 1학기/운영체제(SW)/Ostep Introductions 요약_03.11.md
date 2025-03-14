## 복습 및 과제
**|Dialog**
우리가 배울 세 가지 핵심 아이디어에요: ==가상화==, ==동시성==, 그리고 ==지속성==입니다. 이러한 아이디어에 대해 배우면, 운영 체제가 어떻게 작동하는지, CPU에서 다음으로 실행할 프로그램을 어떻게 결정하는지, 가상 메모리 시스템에서 메모리 과부하를 어떻게 처리하는지, 가상 머신 모니터가 어떻게 작동하는지, 디스크에서 정보를 관리하는 방법 등에 대해 모두 배우게 될 거예요. 그리고 일부 부분이 고장났을 때 작동하는 분산 시스템을 구축하는 방법에 대해서도 알게 될 거예요. 그런 종류의 것이죠.
  
**|Introduction**
가상화 → 동시성 → 지속성 → OS디자인 목표 → 역사

> [!info]  
>  
> [https://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf](https://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf)  
## 서문
- 학부 운영 체제 과목을 수강 중인 경우, 프로그램이 실행될 때의 기본적인 동작 방식에 대한 이해가 필요하다.
- 프로그램 실행 도중 프로세서는 명령을 메모리에서 가져와 해독하고 실행하는 과정을 반복한다.
- 폰 노이만 모델에서 프로그램 실행에 대한 기본 개념이 설명된다.
- 운영 체제는 프로그램 실행을 용이하게 하기 위한 소프트웨어를 포함하여 시스템을 관리한다.
- 이 과목에서는 프로그램 실행 중에 다양한 작업이 이루어지며, 시스템 사용을 용이하게 하는 것이 주요 목표라는 것을 배우게 된다.
- 프로그램이 메모리를 공유하도록하고 다른 기기와 상호작용하도록 하는 SW가 바로 OS이다.
- 운영 체제(OS)는 시스템이 올바르고 효율적으로 운영되며 사용하기 쉬운 방식으로 동작하도록 보장하는 책임이 있다.
- 운영 체제는 가상화라는 일반적인 기술을 통해 이를 달성하는데, 이는 물리적 자원(프로세서, 메모리, 디스크 등)을 더 일반적이고 강력하며 사용하기 쉬운 가상 형태로 변환한다.
- 사용자가 운영 체제에게 명령을 내리고 이러한 가상 머신의 기능(프로그램 실행, 메모리 할당, 파일 액세스 등)을 활용할 수 있도록 운영 체제는 몇 가지 인터페이스(API)를 제공한다.
- 운영 체제는 응용 프로그램에 사용 가능한 몇 백 개의 시스템 호출을 내보내므로, 프로그램 실행, 메모리 및 장치 액세스 등을 위해 이러한 호출을 제공한다고 말할 수 있다.
- 가상화를 통해 많은 프로그램이 동시에 실행되고 CPU를 공유하며, 각각의 명령과 데이터에 동시에 액세스할 수 있게 되고, 장치에 액세스할 수 있게 되면서, 운영 체제는 종종 리소스 관리자로 알려져 있다. CPU, 메모리 및 디스크는 시스템의 자원이므로, 이러한 자원을 효율적이거나 공정하게 관리하는 것이 운영 체제의 역할이다.
  
## 2.1 CPU 가상화
- Figure 2.1은 우리의 첫 번째 프로그램을 보여줍니다. 이 프로그램은 많이 하지 않습니다. 실제로, 이 프로그램은 반복적으로 시간을 확인하고 1초가 경과하면 반환하는 함수인 Spin()을 호출합니다. 그런 다음, 사용자가 명령 줄에 전달한 문자열을 출력하고 영원히 반복합니다.
- 우리는 이 파일을 cpu.c로 저장하고, 단일 프로세서(또는 CPU로 가끔 부를 것입니다)를 가진 시스템에서 컴파일하고 실행하기로 결정했다고 가정해 봅시다.
- 다음은 우리가 볼 내용입니다:
    - prompt> gcc -o cpu cpu.c -Wall
    - prompt> ./cpu "A"
    - A
    - A
    - A
    - A
    - ˆC
    - prompt>
- 별로 흥미로운 실행은 아닙니다 - 시스템은 프로그램을 실행하고, 1초가 지날 때까지 반복적으로 시간을 확인합니다. 1초가 지나면, 코드는 사용자가 입력한 입력 문자열(이 예제에서는 문자 "A")을 출력하고 계속됩니다. 프로그램은 영원히 실행될 것입니다; "Control-c"를 누르면 (UNIX 기반 시스템에서 프로그램을 종료하는데 사용되는) 프로그램을 중지시킬 수 있습니다.
- Figure 2.2: 동시에 여러 프로그램 실행하기
- 이제 같은 작업을 하되, 이번에는 이 같은 프로그램의 여러 다른 인스턴스를 실행해 봅시다. Figure 2.2는 이 약간 더 복잡한 예제의 결과를 보여줍니다.
- 이제 상황이 조금 더 흥미롭게 되고 있습니다. 하나의 프로세서만 있음에도 불구하고, 이 네 가지 프로그램은 어떻게든 동시에 실행되는 것 같습니다! 이런 마법이 어떻게 가능한 걸까요?
- 이것은 운영 체제가 하드웨어의 도움을 받아 이 환상, 즉 시스템이 매우 큰 가상 CPU 수를 가지고 있는 것처럼 보이도록 하는 것을 담당한다는 것이 밝혀졌습니다. 단일 CPU(또는 소수의 CPU)를 seemingly 무한대의 CPU로 바꾸어 많은 프로그램이 seemingly 동시에 실행되게 하는 것이 이 책의 첫 번째 주요 부분인 CPU 가상화에 집중됩니다.
- 물론 프로그램을 실행하고 중지하고, 그리고 기타 OS에게 어떤 프로그램을 실행할지 알리는 방법이 있어야 합니다. 이러한 욕망을 OS에 전달하기 위해 사용할 수 있는 인터페이스(API)가 있어야 합니다. 우리는 이 책 전반에 걸쳐 이러한 API에 대해 이야기할 것입니다; 실제로, 이들은 대부분의 사용자가 운영 체제와 상호 작용하는 주요 방법입니다.
- 여러 프로그램을 동시에 실행할 수 있는 능력은 새로운 종류의 다양한 질문을 던집니다. 예를 들어, ==특정 시간에 두 개의 프로그램이 실행되길 원한다면 어느 것이 실행되어야 할까요? 이 질문은 OS의 정책에 따라 결정됩니다.== 정책은 OS 내에서 이러한 유형의 질문에 대한 답변으로 사용되며, 따라서 우리는 운영 체제가 구현하는 기본 메커니즘(여러 프로그램을 동시에 실행하는 능력과 같은)을 배우면서 이에 대해 연구할 것입니다. 이것이 리소스 관리자로서의 운영 체제의 역할입니다.
  
## 2.2 메모리 가상화
- 현대 시스템에서 제시된 물리적 메모리 모델은 매우 간단합니다. 메모리는 단순히 바이트의 배열일 뿐입니다. 메모리를 읽으려면 데이터가 저장된 위치를 지정해야 하고, 메모리를 쓰려면 (또는 업데이트하려면) 주어진 주소에 쓸 데이터도 지정해야 합니다.
- 프로그램이 실행되는 동안 메모리에 항상 액세스됩니다. 프로그램은 모든 데이터 구조를 메모리에 유지하고, 로드 및 저장 또는 다른 명시적인 명령을 통해 메모리에 액세스하여 작업을 수행합니다. 프로그램의 각 명령도 메모리에 있으므로, 메모리는 각 명령 검색 시에도 액세스됩니다.
- malloc()을 호출하여 일부 메모리를 할당하는 프로그램 (Figure 2.3에 표시됨)을 살펴보겠습니다. 이 프로그램의 출력은 다음과 같습니다:
    - prompt> ./mem
        - (2134) p가 가리키는 주소: 0x200000
        - (2134) p: 1
        - (2134) p: 2
        - (2134) p: 3
        - (2134) p: 4
        - (2134) p: 5
        - ˆC
    - prompt> ./mem & ./mem &
        - [1] 24113
        - [2] 24114
        - (24113) p가 가리키는 주소: 0x200000
        - (24114) p가 가리키는 주소: 0x200000
        - (24113) p: 1
        - (24114) p: 1
        - (24114) p: 2
        - (24113) p: 2
        - (24113) p: 3
        - (24114) p: 3
        - (24113) p: 4
        - (24114) p: 4
        - ...
- Figure 2.4: 메모리 프로그램을 여러 번 실행하기
- 이 프로그램은 몇 가지 작업을 수행합니다. 먼저, 일부 메모리를 할당합니다 (라인 a1). 그런 다음, 메모리의 주소를 출력합니다 (a2) 그리고 새롭게 할당된 메모리의 첫 번째 슬롯에 숫자 0을 넣습니다 (a3). 마지막으로, 반복문을 실행하여 1초 동안 딜레이를 주고 p에 저장된 주소의 값을 증가시킵니다. 각 출력 문에는 실행 중인 프로그램의 프로세스 식별자 (PID)도 출력됩니다. 이 PID는 실행 중인 프로세스마다 고유합니다.
- 다시 말하지만, 이 첫 번째 결과는 그다지 흥미롭지 않습니다. 새롭게 할당된 메모리는 주소 0x200000에 있습니다. 프로그램이 실행됨에 따라 값이 천천히 업데이트되고 결과가 출력됩니다.
- 이제 다시 이 같은 프로그램의 여러 인스턴스를 실행하여 무엇이 발생하는지 살펴보겠습니다 (Figure 2.4). ==예제에서 보듯이 각 실행 중인 프로그램은 동일한 주소 (0x200000)에서 메모리를 할당했지만, 각각이 독립적으로 주소 0x200000의 값을 업데이트하는 것처럼 보입니다!== 마치 각 실행 중인 프로그램이 다른 실행 중인 프로그램과 물리적 메모리를 공유하는 대신 자체 개인 메모리를 갖고 있는 것처럼 보입니다.
- 실제로 여기서 일어나는 것이 바로 운영 체제가 메모리를 가상화하고 있는 것입니다. 각 프로세스는 자체 개인 가상 주소 공간 (가끔은 단순히 주소 공간이라고 함)에 액세스하며, 이를 운영 체제가 기계의 물리적 메모리에 어떻게 매핑하는지는 알 수 없습니다. 한 실행 중인 프로그램 내에서의 메모리 참조는 다른 프로세스 (또는 운영 체제 자체)의 주소 공간에 영향을 미치지 않습니다. 실행 중인 프로그램은 물리적 메모리를 완전히 자체 것으로 생각합니다. 그러나 실제로는 물리적 메모리가 운영 체제에 의해 관리되는 공유 리소스입니다. 모든 이러한 것이 어떻게 수행되는지도 이 책의 첫 번째 부분인 가상화 주제의 대상입니다.
  
## 2.3 동시성(Concurrency)

> [!important]  
> 동시성(Concurrency)은 여러 작업이 동시에 실행되는 것을 의미합니다. 이는 프로그램이 여러 스레드를 사용하여 동시에 작업을 수행하거나, 여러 프로세스가 동시에 실행되는 상황을 포함합니다. 동시성은 프로그램의 성능을 향상시키고 자원을 효율적으로 활용하기 위해 사용됩니다. 그러나 동시에 여러 작업이 진행될 때 발생할 수 있는 문제들을 이해하고 처리하는 것이 중요합니다. 이러한 문제 중 하나는 동시에 여러 스레드나 프로세스가 공유하는 데이터에 대한 접근 제어입니다. 동시성을 다룰 때에는 이러한 문제들을 고려하여 프로그램을 설계하고 구현해야 합니다.  
- Figure 2.5: 다중 스레드 프로그램 (threads.c)
- 이 책의 또 다른 주요 주제 중 하나는 동시성입니다. 우리는 이 개념적 용어를 사용하여 동일한 프로그램에서 동시에 많은 일을 처리할 때 발생하는 문제들을 참조합니다. 동시성의 문제는 운영 체제 자체에서 먼저 발생했습니다. 위에서 가상화에 관한 예제에서 볼 수 있듯이, 운영 체제는 동시에 많은 일을 처리하고 있습니다. 먼저 하나의 프로세스를 실행한 다음 다른 것을 실행하고 그렇게 반복합니다. 이렇게 하면 깊고 흥미로운 문제가 발생합니다.
- 유감스럽게도, 동시성의 문제는 더 이상 운영 체제 자체에만 국한되지 않습니다. 실제로, 현대의 다중 스레드 프로그램도 같은 문제를 나타냅니다. 우리는 다중 스레드 프로그램의 예제로 이를 시연하겠습니다 (Figure 2.5).
- 메인 프로그램은 Pthread create()를 사용하여 두 개의 스레드를 생성합니다.
- 각 스레드는 worker() 루틴에서 실행되며, 여기서는 루프를 사용하여 카운터를 증가시킵니다.
- 두 스레드가 완료되면 카운터의 최종 값은 각 스레드가 카운터를 1000번씩 증가시켰으므로 2000이 됩니다.
- 루프의 입력 값이 N으로 설정된 경우, 프로그램의 최종 출력은 일반적으로 2N이 될 것으로 예상됩니다.
- 그러나 높은 값의 루프를 사용할 때 예상치 못한 결과가 나올 수 있습니다.
- 입력 값이 100,000일 때 예상치 못한 결과가 발생합니다.
- 프로그램을 여러 번 실행하면 각각 다른 결과가 나올 수 있습니다.
- 명령어가 한 번에 하나씩 실행되는 방식이 결과에 영향을 줍니다.
- 공유 카운터를 증가시키는 부분이 세 단계의 명령어로 이루어져 있어, 원자적으로 실행되지 않습니다.
- 이러한 동시성 문제를 해결하기 위해 운영 체제 및 하드웨어에서 어떤 기능과 메커니즘이 필요한지 고민해야 합니다.
  
## 2.4 영속성(Persistence)

> [!important]  
> 영속성(Persistence)은 데이터가 지속적으로 보존되는 것을 의미합니다. 시스템 메모리에서는 데이터가 휘발성으로 저장되어 전원이 꺼지거나 시스템이 충돌하면 데이터가 손실될 수 있습니다. 따라서 하드웨어와 소프트웨어를 사용하여 데이터를 영구적으로 저장하는 것이 중요합니다. 이를 위해 파일 시스템과 같은 소프트웨어가 디스크에 데이터를 쓰고 관리하며, 하드웨어로는 하드 드라이브나 SSD와 같은 저장 장치가 사용됩니다. 영속성은 사용자 데이터의 중요성으로 인해 시스템에서 필수적인 요소입니다.  
- 시스템 메모리의 데이터는 휘발성으로 저장되기 때문에 전원 손실 시 데이터 손실이 발생할 수 있습니다.
- 영속적인 데이터 저장을 위해 하드웨어와 소프트웨어가 필요하며, 이는 사용자 데이터에 대한 중요성으로 인해 시스템에서 필수적입니다.
- 하드웨어로는 하드 드라이브와 SSD가 주로 사용되며, 소프트웨어로는 파일 시스템이 디스크를 관리합니다.
- 운영 체제는 각 애플리케이션에 대해 개별적인 가상 디스크를 생성하지 않고, 파일을 공유하기 위한 메커니즘을 제공합니다.
- 파일을 편집, 컴파일 및 실행하는 과정에서 파일이 여러 프로세스 간에 공유되는 방법을 이해할 수 있습니다.
**IO를 하는 프로그램(io.c)**
- Figure 2.6은 파일을 생성하고 그 안에 "hello world"라는 문자열을 저장하는 코드를 제시합니다.
- 프로그램은 파일을 열고 생성하는 open(), 데이터를 파일에 쓰는 write(), 파일을 닫는 close()과 같은 세 가지 운영 체제 호출을 수행합니다.
- 이러한 시스템 호출은 파일 시스템으로 라우팅되어 처리되며, 오류 코드를 반환합니다.
- 파일 시스템은 디스크에 데이터를 쓰기 위해 많은 작업을 수행해야 하며, 이는 디스크 상의 데이터 위치를 결정하고 추적하는 것을 포함합니다.
- 대부분의 파일 시스템은 쓰기 지연 및 쓰기 중 시스템 충돌 문제를 다루기 위한 복잡한 프로토콜을 사용하여 데이터를 영구적으로 관리합니다.
  
11페이지 중간까지 완. 2.5Design Goals부터 시작하면 됨(03.11)
  
## 2.5 OS 디자인의 목표
- 운영 체제는 CPU, 메모리, 디스크 등과 같은 물리적 자원을 가상화합니다.
- 동시성 문제를 효과적으로 처리합니다.
- 파일을 장기적으로 안전하게 저장하여 보장합니다.
- 설계, 구현 및 트레이드 오프를 안내하는 목표를 수립합니다.
- 시스템을 편리하고 관리하기 쉽게 만드는 추상화의 중요성을 강조합니다.
- 운영 체제를 설계하고 구현하는 주요 목표 중 하나는 시스템의 오버헤드를 최소화하여 높은 성능을 제공하는 것입니다.
- 가상화와 시스템의 사용 편의성은 가치가 있지만, 과도한 오버헤드 없이 가상화와 기타 OS 기능을 제공해야 합니다.
- 이러한 오버헤드는 추가적인 시간(더 많은 명령어)과 공간(메모리 또는 디스크) 형태로 발생합니다.
- 응용 프로그램 간 및 OS와 응용 프로그램 간의 보호를 제공하는 것도 목표 중 하나입니다.
- 운영 체제는 중단 없이 실행되어야 하며, 신뢰성이 높아야 합니다. 에너지 효율성, 보안, 이동성 등의 목표도 중요합니다.
  
## 2.6 OS의 역사
- 운영 체제가 어떻게 발전해 왔는지 간단한 역사를 소개합니다.
- 인간들에 의해 구축된 모든 시스템과 마찬가지로, 엔지니어들이 설계에서 중요한 점을 깨달을 때 운영 체제에는 좋은 아이디어가 시간이 흐름에 따라 축적되었습니다.
- 여기서는 몇 가지 주요 발전 사항을 논의합니다. 더 풍부한 내용은 Brinch Hansen의 운영 체제 역사에 관한 훌륭한 책을 참조하십시오.
- Brinch Hansen의 훌륭한 운영 체제 역사 책 [BH00]에서 자세한 내용을 확인하십시오.
  
### 초기 운영 체제: 단순한 라이브러리
- 처음에는 운영 체제가 많은 일을 하지 않았습니다. 기본적으로, 일반적으로 사용되는 기능들의 라이브러리 세트였습니다.
- 예를 들어, 시스템의 각 프로그래머가 저수준의 I/O 처리 코드를 작성하는 대신, "OS"가 해당 API를 제공하여 개발자의 작업을 쉽게 했습니다.
- 보통 이러한 오래된 메인프레임 시스템에서는 한 번에 하나의 프로그램이 실행되었으며, 이는 인간 운영자에 의해 제어되었습니다.
- 현대의 운영 체제가 수행하는 것처럼 (예: 작업 실행 순서 결정) 많은 작업은 이 운영자에 의해 수행되었습니다.
- 이 모드는 배치 처리로 알려져 있었으며, 운영자가 일련의 작업을 설정한 다음 "일괄적으로" 실행했습니다.
  
### 라이브러리를 넘어서: Protection
- 운영 체제는 단순한 라이브러리 역할을 넘어서 기계를 관리하는 중심적 역할을 맡게 됨
- 코드 실행에 있어 운영 체제를 대신하는 코드(시스템 콜)는 특별 취급되며, 장치 제어 등 ==특수한 권한==을 갖게 됨
- 시스템 콜의 개념은 Atlas 컴퓨팅 시스템에서 고안되어 하드웨어 명령과 상태를 사용하여 운영 체제로의 전환을 공식적이고 제어된 프로세스로 만듦
- 시스템 콜은 하드웨어 권한 수준을 높이고, 제어를 운영 체제로 전달함으로써 프로시저 호출과 구별됨
- 운영 체제는 커널 모드에서 하드웨어에 완전한 액세스를 허용하여, I/O 요청을 시작하고 메모리를 할당하는 등의 작업을 수행함
  
### 멀티프로그래밍 시대
- ⚠️메인프레임을 넘어 미니컴퓨터 시대에서 운영 체제가 크게 발전했습니다.
- 디지털 장비의 ⚠️PDP 시리즈와 같은 클래식한 기계들이 컴퓨터를 훨씬 더 저렴하게 만들어, 대규모 조직 당 하나의 메인프레임을 가지는 것이 아니라 조직 내 소수의 사람들이 각자 컴퓨터를 가질 수 있게 되었습니다.
- 이로 인해 비용이 감소함에 따라 개발자 활동이 증가하게 되었고, 더 많은 사람들이 컴퓨터를 사용하여 더 많은 흥미로운 일을 할 수 있게 되었습니다.
- 특히, 자원을 더 잘 활용하기 위한 욕구로 멀티프로그래밍이 보편화되었습니다. 하나의 작업만 실행하는 것이 아니라 ==여러 작업을 메모리에 로드하고 그 사이를 빠르게 전환하여 CPU 사용률을 향상==시켰습니다.
- 멀티프로그래밍을 지원하고 I/O 및 인터럽트의 동시 발생을 처리하기 위한 운영 체제의 개념적 발전이 필요하였으며, 이로 인해 메모리 보호와 같은 문제가 중요해졌습니다.
  
### 현대 시대
- 현대 시대는 개인용 컴퓨터(PC)의 등장으로 시작됨
- 초기 PC 운영 체제는 미니컴퓨터 시대의 교훈을 잊거나 무시함
- PC 운영 체제의 초기 버전은 메모리 보호 및 작업 스케줄링과 같은 중요한 기능을 제공하지 않았음
- 그러나 몇 년 후에 미니컴퓨터 운영 체제의 기능이 PC에 도입되기 시작함
- 현재의 PC 및 모바일 운영 체제는 미니컴퓨터 시대의 운영 체제에서 개발된 좋은 아이디어를 채택하여 사용자 및 응용 프로그램에 더 많은 기능을 제공함
  
## 2.7 요약
- 현재의 운영 체제는 시스템을 상대적으로 쉽게 사용할 수 있게 만들었으며, 우리가 이 책 전반에 걸쳐 논의할 발전에 영향을 받았습니다.
- 시간 제약으로 인해 책에서 다루지 않는 운영 체제의 여러 부분이 있습니다. 예를 들어, 운영 체제에는 많은 네트워킹 코드가 있습니다. 네트워킹에 대해 더 많이 배우기 위해 네트워킹 수업을 수강하십시오.
- 마찬가지로, 그래픽 디바이스는 특히 중요합니다. 그래픽 수업을 들어 지식을 확장하십시오.
- 마지막으로, 일부 운영 체제 교재는 보안에 대해 많이 다룹니다. 우리는 운영 체제가 실행 중인 프로그램 사이에 보호를 제공하고 사용자가 파일을 보호할 수 있도록 해야 한다는 측면에서 이에 대해 다룰 것입니다.
- 그러나 CPU와 메모리의 가상화, 동시성 및 장치 및 파일 시스템을 통한 지속성과 같은 많은 중요한 주제를 다룰 것입니다.
- 걱정하지 마십시오! 다룰 내용이 많지만 대부분은 꽤 멋집니다. 그리고 끝까지 가면 컴퓨터 시스템이 실제로 어떻게 작동하는지에 대한 새로운 인식을 얻게 될 것입니다.