### 1. **Docker란 무엇인가?**

#### **컨테이너와 가상 머신의 차이점**

- **공부 내용**:
    - **컨테이너**는 OS의 [[커널]]을 공유하여 실행되며, 가상 머신보다 가벼운 오버헤드를 가집니다. 또한, 컨테이너는 특정 애플리케이션과 그 실행 환경을 격리된 환경에서 실행할 수 있게 해 줍니다.
    - **가상 머신**은 하드웨어에서 가상화된 독립적인 운영 체제를 실행하며, 각각의 VM은 자체적인 운영 체제 커널을 가지고 있습니다. 이로 인해 리소스를 더 많이 소비하고, 부팅 시간이 길어집니다.
- **자료 검색 키워드**:
    - "container vs virtual machine"
    - "What is Docker container?"
    - "Virtualization vs containerization"

#### **Docker의 구성 요소**

- **공부 내용**:
    - **Docker 이미지**: 애플리케이션과 그 실행 환경을 포함하는 불변의 템플릿입니다. 이미지에서 컨테이너가 생성됩니다.
    - **컨테이너**: 이미지를 기반으로 실행되는 가벼운 격리된 프로세스입니다. Docker에서는 컨테이너가 애플리케이션을 실제로 실행합니다.
    - **Docker Daemon**: Docker 서비스를 관리하는 백그라운드 프로세스입니다. `dockerd`라고 불리며, 클라이언트 요청을 받아 Docker 컨테이너와 이미지를 관리합니다.
    - **Docker CLI**: Docker를 관리하는 명령줄 도구입니다. `docker` 명령어를 사용하여 컨테이너와 이미지를 제어할 수 있습니다.
- **자료 검색 키워드**:
    - "What are Docker images?"
    - "Docker container overview"
    - "Docker Daemon and Docker CLI"