### 1. Gradle 개요
- Gradle은 [[빌드]] 자동화 도구로, Java, Groovy, Kotlin 등 여러 언어를 지원합니다.
- Java 프로젝트에 자주 사용되지만, Android 앱 개발, 웹 애플리케이션 배포, 서버 설정 등 다양한 분야에서 활용됩니다.

### 2. Gradle의 특징

- 유연성: 매우 유연하고 확장 가능하여 다양한 빌드 요구 사항에 맞게 설정할 수 있습니다.
- 의존성 관리: 프로젝트에 필요한 라이브러리 및 플러그인을 자동으로 다운로드하고 관리할 수 있습니다.
- 성능: Gradle은 빌드 성능을 최적화하기 위한 여러 기능(예: 병렬 빌드, 증분 빌드)을 제공합니다.

### 3. Gradle 설정 파일

- build.gradle: Gradle 프로젝트의 설정을 포함하는 핵심 파일입니다.
    - Groovy DSL과 Kotlin DSL을 지원하며, 의존성, 플러그인, 빌드 태스크 등을 설정할 수 있습니다.
- 예시 (`build.gradle`):
    
    ```groovy
    plugins {
        id 'java'
    }
    
    repositories {
        mavenCentral()
    }
    
    dependencies {
        implementation 'org.springframework:spring-core:5.3.8'
    }
    ```
    

### 4. Gradle Wrapper

- Gradle Wrapper는 프로젝트에서 특정 Gradle 버전을 일관되게 사용할 수 있도록 해줍니다.
    
- `gradlew` 스크립트를 사용하여 Gradle을 실행할 수 있으며, 프로젝트에 Gradle이 설치되지 않아도 자동으로 다운로드하여 실행됩니다.
    
- Wrapper 설치:
    
    ```bash
    gradle wrapper
    ```
    
- Wrapper 사용:
    
    - 윈도우에서는 `gradlew.bat`
    - 유닉스 시스템에서는 `./gradlew`

### 5. Gradle 빌드 라이프사이클

Gradle은 다음과 같은 기본 빌드 라이프사이클을 가지고 있습니다:

- Initialization: 어떤 프로젝트를 빌드할지 결정합니다.
- Configuration: 빌드를 위한 설정을 구성합니다.
- Execution: 실제 빌드를 실행합니다.

### 6. 의존성 관리

Gradle은 프로젝트에 필요한 라이브러리나 외부 의존성을 자동으로 관리합니다.

- 로컬 및 원격 저장소에서 의존성을 가져옵니다.
- 예시:
    
    ```groovy
    repositories {
        mavenCentral()
    }
    
    dependencies {
        implementation 'com.google.guava:guava:30.1-jre'
    }
    ```
    

### 7. Gradle 태스크

- Gradle 빌드는 태스크라는 단위 작업으로 구성됩니다. 태스크는 특정 작업을 정의하고 실행합니다.
- 예시:
    
    ```groovy
    task hello {
        doLast {
            println 'Hello, Gradle!'
        }
    }
    ```
    
- 이 예제에서 `hello` 태스크는 `Hello, Gradle!`을 출력합니다.

### 8. Gradle 플러그인

Gradle은 플러그인을 사용하여 빌드를 확장할 수 있습니다. 예를 들어, `java` 플러그인을 사용하면 Java 프로젝트에 필요한 설정을 자동으로 처리합니다.

### 9. 멀티 프로젝트 빌드

Gradle은 멀티 프로젝트 빌드를 지원합니다. 여러 프로젝트를 하나의 빌드 스크립트에서 관리하고, 공통 의존성 및 설정을 공유할 수 있습니다.

- settings.gradle에서 프로젝트를 설정하고, 각 하위 프로젝트에서 개별 빌드를 정의합니다.

### 10. Gradle과 다른 빌드 도구 비교

- [[Maven]]: Maven은 XML 기반의 설정 파일을 사용하고, Gradle은 Groovy/Kotlin 기반으로 더 유연하고 다이나믹한 구성이 가능합니다.
- Ant: Ant는 스크립트를 사용한 빌드 도구로, Gradle보다 더 복잡한 구성이 필요하지만 유연성은 뛰어납니다.

### 11. Gradle 학습 리소스

- Gradle 공식 문서: [https://gradle.org/docs/](https://gradle.org/docs/)
- Gradle 공식 튜토리얼 및 블로그
- Gradle 관련 책: "Gradle for Android" 등

---

이 팔레트를 따라가면 Gradle의 전반적인 개념부터 실전 활용까지 이해할 수 있을 것입니다. 각 항목에 대해 더 깊이 있는 학습을 원하시면, 관련 문서나 튜토리얼을 참고하여 학습을 진행하세요!