
## 1. Repository 패턴

### - 개념:
    
- DB 같은 영속 계층(데이터 저장소)에 대한 접근 로직을 모아 두는 레이어(계층) 패턴.

### - 역할:
    
- insert / update / delete / find 같은 “데이터 CRUD 전용 함수”만 담당.
- Service, UI 코드가 직접 SQL이나 ORM 쿼리를 몰라도 되게 해 줌(= 데이터 접근 캡슐화).

### - 예시 느낌:
    
- UserRepository.getUserById(id)
- NotificationRepository.getUnreadNotifications(studentId)

  

## 2. Service 패턴
### - 개념:

- 비즈니스 로직(업무 규칙, 도메인 규칙)을 담당하는 레이어 패턴.


### - 역할:

- 여러 Repository를 조합해서 “하나의 기능/시나리오”를 완성.
- 트랜잭션 처리, 검증, 도메인 규칙 같은 것을 맡음.

### - 예시 느낌:

- NotificationService.markAllAsRead(studentId) 안에서
	- NotificationRepository.findAllUnread(studentId) 호출
	- 각 알림 isRead 변경 후 저장


  

한 줄로 정리하면:

- Repository = “데이터를 어떻게 저장/읽을지”를 담당하는 계층
- Service = “어떤 규칙으로 동작할지(업무 로직)”를 담당하는 계층