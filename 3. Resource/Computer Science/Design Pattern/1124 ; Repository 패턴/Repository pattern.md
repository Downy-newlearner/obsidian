---
created: 2025-11-24
tags: []
aliases:
reference:
---


**Repository 패턴, 한 줄로 말하면**
**“데이터를 어디서 어떻게 가져오는지 숨겨주는 중간 창구”야.**

  

조금 풀어서:

1. 기본 아이디어
    - UI / 도메인 코드는 “이 유저 정보 좀 줘”라고만 말하고
        
    - Repository가
        “로컬 캐시에서 줄까? DB에서 줄까? 서버에서 받아올까?” 를 대신 결정해서 처리해 주는 패턴이야.
        
    
2. 계층 구조에서 위치
    
    보통 이런 흐름이 돼:
    
    UI(View / Activity / Fragment)
    
    → ViewModel / UseCase
    
    → Repository
    
    → Local(DataStore, SharedPreferences, Room 등) / Remote(API)
    
3. 왜 쓰냐 (장점)
    
    - 데이터 소스 교체가 쉬움
        
        - 서버 API 바뀌거나, SharedPreferences → Room으로 바꿔도
            
            Repository 내부만 수정하면 위쪽 코드(ViewModel, UseCase)는 그대로.
            
        
    - 테스트하기 쉬움
        
        - Repository를 interface로 빼두면,
            
            테스트에서 FakeRepository / MockRepository 주입해서 단위 테스트 가능.
            
        
    - “단 하나의 진실 소스”(Single Source of Truth)
        
        - 캐시 + 로컬 + 원격이 있을 때,
            
            “최종적으로 앱에서 쓰는 데이터는 Repository를 통해서만 온다”라는 규칙을 만들 수 있음.
            
        
    
4. 간단한 예시 (Kotlin 느낌으로)
    
    인터페이스:
    

```
interface UserRepository {
    suspend fun getUser(id: String): User
}
```

4. 구현체:
    

```
class UserRepositoryImpl(
    private val api: UserApi,
    private val userDao: UserDao
) : UserRepository {

    override suspend fun getUser(id: String): User {
        // 1) 로컬 DB에서 먼저 시도
        val local = userDao.getUser(id)
        if (local != null) return local

        // 2) 없으면 서버에서 가져오고
        val remote = api.getUser(id)
        // 3) DB에 저장 후 리턴
        userDao.insert(remote)
        return remote
    }
}
```

4. 위쪽 ViewModel에서는 그냥:
    

```
val user = userRepository.getUser("123")
```

4. 만 알면 되고,
    
    “DB냐 서버냐 캐시냐”는 전혀 신경 안 써도 됨.
    
5. 너가 쓰고 있는 상황에 대입하면
    
    - SharedPreferences(캐시)
        
    - 로컬 DB 또는 메모리 캐시
        
    - API 호출 결과
        
        이런 걸 한 Repository 아래로 모으고,
        
    
    ViewModel/UseCase 쪽에서는
    
    “assessmentRepository.getAssessment(id)”
    
    정도만 쓰게 만들면 돼.
    

  
