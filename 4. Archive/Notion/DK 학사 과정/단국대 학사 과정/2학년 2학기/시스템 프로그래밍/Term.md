- bss
    - block started by symbol
- IPC
    - Inter Process Communication
    - 프로세스 간 통신
    - 예를 들면 파이프가 있다.
- Task struct
  
- signal()
    - 시스템 콜
    - 비동기적인 사건.
    - 현재 읽고있던 책을 멈추고 전화를 받는다. 전화가 끝나면 읽고있던 부분부터 책을 다시 읽는것과 같다.
    - 프로세스를 실행하다가 시그널을 받으면 프로세스를 멈추고 시그널을 handle한다.(signal catch function)
    - ==시그널과 인터럽트의 상관관계가 있나?==
- nice
    - 프로세스 우선순위를 제어한다.
    - nice(-2)를 실행하면 기존 우선순위 숫자에 -2를 한다.
- ptrace
    - 프로세스에게 다른 프로세스의 실행을 허용한다. ???
- gettimeofday()
    
    - 프로세스의 시간 정보를 가져온다.
    
      
    
- 동기화(Synchronization)
    
    - 경쟁 상태를 허락하지 않기 위해 순서 관계를 부여하는 것.
    
    ![[Source/Untitled 69.png|Untitled 69.png]]
    
    ```JavaScript
    else{
    	wait() //이렇게 wait()을 넣어서 해결할 수 있다.
    	charatatime("output from parent\n");
    }
    ```
    
    - wait()는 순서관계 즉, 동기화를 주기 위한 방법이다.
    - 다른 방법으론 ‘조건 변수 이용’도 있다.
    
      
    
- 스레드 모델
    
    - 데이터, 파일을 공유하는 모델이다.
    - 하지만 레지스터, 스택은 공유하지 않고 스레드마다 따로 가지고 있는다.
    
      
    
- 로드 스토어 아키텍쳐
    
    - 메모리에서 읽거나 쓸 때 고유한 명령어만 사용해서 접근한다.
    
      
    
- directive(지시자)
    
    - .data 지시자는 데이터 섹션을 선언
    - .long 지시자는 4바이트 메모리 공간을 생성
    - .string 지시자는 string 초기화 (array of character)
    
      
    
- iscpu
    
    - CPU의 정보를 알려준다.
    
      
    
- strace
    - 사용한 시스템 콜을 보여준다.
- top
- blktrace
    - 블럭 io들이 어떤 순서로 디스크에 접근되는지
- perf_event
    - 하드웨어적인 이벤트를 뽑아준다.
    - CPU내부 로직이 얼마만큼의 성능을 보이는지 알림
    - CPU가 지원을 해준다