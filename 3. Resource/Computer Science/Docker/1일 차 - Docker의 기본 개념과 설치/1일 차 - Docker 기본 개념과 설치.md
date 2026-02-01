우선 GPT에게 자세히 무엇을 공부해야하고, 관련 자료를 검색할 때 사용할 수 있는 키워드를 제공받았다.


1일 차 커리큘럼에 대한 공부 방법과 관련 자료 검색 키워드를 구체적으로 안내드립니다.

### 1. **Docker란 무엇인가?**

#### **컨테이너와 가상 머신의 차이점**

- **공부 내용**:
    - **컨테이너**는 OS의 커널을 공유하여 실행되며, 가상 머신보다 가벼운 오버헤드를 가집니다. 또한, 컨테이너는 특정 애플리케이션과 그 실행 환경을 격리된 환경에서 실행할 수 있게 해 줍니다.
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

### 2. **Docker 설치**

#### **Windows, macOS, Linux에서 Docker 설치**

- **공부 내용**:
    - **Windows**: Docker Desktop을 설치하여 Windows에서 Docker를 실행할 수 있습니다. Docker Desktop은 Hyper-V를 통해 가상 머신을 실행하여 컨테이너를 격리합니다.
    - **macOS**: Docker Desktop을 사용하여 설치합니다. macOS에서는 LinuxKit을 통해 Linux 기반 컨테이너를 실행합니다.
    - **Linux**: 리눅스에서는 Docker Engine을 설치하여 운영 체제에서 직접 Docker를 사용할 수 있습니다.
- **자료 검색 키워드**:
    - "How to install Docker on Windows"
    - "How to install Docker on macOS"
    - "How to install Docker on Linux"
    - "Docker installation guide"

#### **Docker Desktop과 Docker Engine의 차이점**

- **공부 내용**:
    - **Docker Desktop**은 GUI(그래픽 사용자 인터페이스)를 제공하며, Windows와 macOS에서 Docker를 실행할 수 있도록 가상 머신을 사용합니다. Windows에서는 Hyper-V, macOS에서는 HyperKit을 사용합니다.
    - **Docker Engine**은 리눅스 기반에서 직접 Docker 컨테이너를 관리하는 데 사용되는 서버 프로그램으로, GUI가 없고 CLI를 통해 관리됩니다.
- **자료 검색 키워드**:
    - "Docker Desktop vs Docker Engine"
    - "What is Docker Engine?"

### 3. **Docker 명령어 기초**

#### **`docker --version`, `docker info`**

- **공부 내용**:
    - `docker --version`은 현재 설치된 Docker 버전을 확인하는 명령어입니다.
    - `docker info`는 Docker 시스템의 정보(예: 컨테이너와 이미지 개수, Docker Daemon 상태 등)를 출력합니다.
- **자료 검색 키워드**:
    - "docker --version"
    - "docker info command"

#### **기본 명령어**: `docker run`, `docker ps`, `docker stop`, `docker rm`, `docker images`, `docker rmi`

- **공부 내용**:
    - **`docker run`**: 이미지를 기반으로 컨테이너를 실행하는 명령어입니다.
    - **`docker ps`**: 실행 중인 컨테이너 목록을 보여줍니다.
    - **`docker stop`**: 실행 중인 컨테이너를 종료합니다.
    - **`docker rm`**: 중지된 컨테이너를 삭제합니다.
    - **`docker images`**: 로컬에 저장된 Docker 이미지 목록을 보여줍니다.
    - **`docker rmi`**: Docker 이미지를 삭제합니다.
- **자료 검색 키워드**:
    - "docker run command"
    - "docker ps command"
    - "docker stop command"
    - "docker rm command"
    - "docker images command"
    - "docker rmi command"

### 4. **이미지와 컨테이너 이해**

#### **Docker 이미지 빌드 및 실행**

- **공부 내용**:
    - **이미지 빌드**: `docker build` 명령어로 Dockerfile을 기반으로 이미지를 생성합니다.
    - **이미지 실행**: `docker run` 명령어를 통해 이미지를 실행하여 컨테이너를 생성합니다.
- **자료 검색 키워드**:
    - "How to build Docker image"
    - "How to run Docker image"
    - "docker build command"
    - "docker run command examples"

#### **컨테이너의 생명 주기**

- **공부 내용**:
    - 컨테이너의 생명 주기는 이미지에서 생성되며, 실행되고 종료된 후에는 삭제할 수 있습니다.
    - 컨테이너는 독립적인 실행 환경으로, 실행 중인 동안 프로세스가 격리되어 실행됩니다.
- **자료 검색 키워드**:
    - "Container lifecycle"
    - "Docker container lifecycle"

이 자료를 바탕으로 공부하고, 각 키워드로 더 구체적인 내용을 검색하여 깊이 있는 이해를 돕도록 하세요.