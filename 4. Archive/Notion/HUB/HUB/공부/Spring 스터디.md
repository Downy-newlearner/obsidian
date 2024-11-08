1. 개발환경 구축하기
2. 스프링 콘셉트 이해하기
3. MVC 패턴 이해하기 - 1  
    4 MVC 패턴 이해하기 - 2 (thymeleaf)  
    
4. DB 연결하기 (JPA, 하이버네이트, JDBC)
5. DB 설계하기
6. 로그인/로그아웃 구현하기 - 1 (JWT, 스프링 시큐리티)
7. 로그인/로그아웃 구현하기 - 2(OAuth2)
8. JUnit 이해하기
9. AWS 배포하기
  
[[2일차]]
[[3일차]]
## 대략적으로 아래 체크리스트를 채워나가며 살펴보고, 공부할 수 있는 것들과 실전에 사용할 수 있는 부분을 찾아 12차시 스터디 계획 세우기
#### Spring-웹 용어
|이름|설명|
|---|---|
|[[VMware]]||
|[[EJB]]|Enterprise JavaBeans, 기업환경의 시스템을 구현하기 위한 서버측 컴포넌트 모델|
|[[컴포넌트 모델]]|Component Object Model, COM. 마이크로소프트가 개발한 소프트웨어 구성 요소들의 응용 프로그램 이진 인터페이스 표준이다. COM을 이용해 개발된 프로그램들은 프로세스간 통신과 동적 오브젝트 생성이 가능하다.|
|[[Spring Boot]]|스프링을 기반으로 하여 애플리케이션을 쉽게 생성하고 배포하기 위해 개발된 모듈|
|[[AOP]]|Aspect-Oriented Programming. 관점 지향 프로그래밍, 어떤 로직을 기준으로 핵심 관점, 부가 관점으로 나누고 그 관점을 기준으로 각각 모듈화 하겠다는 의미이다.|
|[[POJO 방식]]|Plain Old Java Object. 의존성이나 상속이 없는 순수한 자바 객체를 사용하는 것을 의미한다.|
|[[JPA]]|Java Persistence API. 자바 애플리케이션에서 데이터베이스 작업을 수행하기 위한 표준 API|
|[[Hibernate]]|JPA의 구현체 중 하나로, 자바 애플리케이션에서 데이터를 영구 저장하기 위한 ORM 프레임워크|
|[[ORM]]|Object-Relational Mapping. 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술. 즉, 객체와 관계형 데이터베이스의 데이터를 매핑하는 것을 의미한다.|
|[[JDBC]]|Java Database Connectivity. 자바에서 데이터베이스에 접근하기 위한 표준 API|
  
  
## 스프링이란?
[[Spring알기]]
- [ ] 스프링 개발환경 구축하는 법
- [ ] 스프링 콘셉트, 큰 그림, 대략적인 역할과 무엇을 할 수 있는가?
- [ ] 스프링을 이용해 하는 일 중에 무엇이 가장 일반적인가?
  
## 마법의 주방으로 비유하기 - 6살 수준
**스프링 프레임워크**는 요리사들이 쉽게 맛있는 음식을 만들 수 있도록 도와주는 **마법의 주방**이에요. 이 주방에는 특별한 도구들과 비법들이 있어서, 요리사들이 훨씬 더 쉽게 일을 할 수 있어요.
### 1. 요리 도구 관리 (IoC와 DI)
마법의 주방에는 **자동 도구 정리 기계**가 있어요. 이 기계는 요리사들이 어떤 도구가 필요한지 알아서 꺼내주고, 쓰고 나면 다시 정리해줘요. 이렇게 요리사들은 필요한 도구를 찾는 데 시간을 낭비하지 않고, 바로 요리에 집중할 수 있죠.
### 2. 마법의 비법 노트 (AOP)
요리사들이 항상 맛있게 요리하려면 몇 가지 비법이 필요해요. 마법의 주방에는 **비법 노트**가 있어서, 이 노트를 참고하면 언제든지 간편하게 로깅이나 트랜잭션 관리 같은 비법을 사용할 수 있어요. 이렇게 요리사들은 중요한 비법을 일일이 외우지 않아도 돼요.
### 3. 자동 트랜잭션 관리 (트랜잭션 관리)
주방에서 요리를 만들 때 어떤 단계에서는 반드시 재료를 추가하거나 섞는 작업이 필요해요. 마법의 주방은 이런 중요한 단계를 자동으로 관리해줘서, 요리사가 실수로 빠뜨리는 일이 없도록 해줘요.
### 4. 요리 책 (MVC)
마법의 주방에는 **요리 책**이 있어서, 요리사들이 다양한 요리를 쉽게 만들 수 있어요. 이 요리 책은 어떻게 요리를 준비하고, 요리를 어떻게 보여줘야 하는지 체계적으로 알려줘요. 그래서 요리사들은 단계별로 따라하기만 하면 멋진 요리를 완성할 수 있어요.
### 5. 다용도 통합기 (통합 및 기타 서비스)
마법의 주방에는 **다용도 통합기**가 있어서, 주방에서 필요한 다양한 도구나 재료들을 쉽게 연결할 수 있어요. 예를 들어, 믹서기, 오븐, 냉장고 등을 다용도 통합기에 연결하면, 요리사들이 어떤 재료가 어디에 있는지 쉽게 알 수 있어요.
  
## 조금 더 깊게 이해해보기, 여전히 비유를 곁들인 - 15살 수준
### ==요리 도구 관리 (IoC와 DI)의 역할과 원리==
1. **IoC (Inversion of Control, 제어의 역전)**:
    - **비유**: 주방에서 요리사가 필요한 도구를 찾으러 돌아다니지 않고, 주방 관리자(마법의 주방)가 요리사에게 필요한 도구를 알아서 준비해주는 것.
    - **원리**: 보통은 요리사가 직접 필요한 도구를 찾지만, 제어의 역전에서는 주방 관리자가 요리사 대신 도구를 준비해줍니다. 즉, 애플리케이션에서는 객체를 직접 생성하고 관리하는 대신, 스프링 컨테이너가 객체의 생성과 생명주기를 관리합니다.
2. **DI (Dependency Injection, 의존성 주입)**:
    - **비유**: 주방 관리자가 요리사에게 필요한 도구를 직접 손에 쥐어주는 것.
    - **원리**: 요리사가 요리를 시작할 때, 주방 관리자가 필요한 도구들을 직접 전달해줍니다. 애플리케이션에서는 객체가 다른 객체를 필요로 할 때, 스프링 컨테이너가 필요한 객체를 주입해줍니다. 이렇게 하면 요리사(객체)는 자신이 필요한 도구(다른 객체)를 직접 찾지 않아도 됩니다.
### ==비법 노트 (AOP)의 역할과 원리==
1. **AOP (Aspect-Oriented Programming, 관점 지향 프로그래밍)**:
    - **비유**: 모든 요리사들이 참고할 수 있는 주방의 비법 노트.
    - **역할**: 비법 노트에는 요리할 때 공통으로 필요한 비법들이 적혀 있어요. 예를 들어, 모든 요리에 소금을 언제 넣어야 하는지, 불을 어떻게 조절해야 하는지 같은 것들이죠. 이렇게 비법 노트를 통해 요리사들이 각 요리마다 공통적으로 적용해야 하는 비법들을 따로 배우지 않아도 돼요.
    - **원리**: 주방에서는 특정 요리에만 적용되는 비법이 아니라, ==모든 요리에 공통으로 적용되는 비법들이 있어요==. 예를 들어, 로깅, 트랜잭션 관리, 보안 체크 등이 그런 비법들이에요. AOP는 이러한 공통 기능들을 비즈니스 로직과 분리해서 코드 중복을 줄이고 관리하기 쉽게 해줍니다. 비법 노트처럼 AOP를 통해 코드에 공통 기능을 적용하면, 비즈니스 로직은 더욱 깔끔해지고 관리하기 쉬워집니다.
### ==자동 트랜잭션 관리와 트랜잭션의 예시==
**자동 트랜잭션 관리**를 주방에서 중요한 단계로 비유했죠. 트랜잭션이란 요리할 때 매우 중요한 단계를 말하는데, 이 단계를 실패하면 요리가 망가질 수 있어요.
### 트랜잭션의 예시
- **비유**: 주방에서 케이크를 구울 때
    - 케이크 반죽을 만들고,
    - 오븐에 넣어 구우며,
    - 다 구워지면 꺼내서 식히는 단계가 있어요.
- 이 모든 단계가 다 성공해야 케이크가 완성돼요. 만약 오븐에 넣고 굽는 단계에서 실패하면, 케이크는 제대로 완성되지 않죠.
### 실제 트랜잭션의 예시
- **은행 계좌 이체**:
    - 돈을 보내는 사람의 계좌에서 돈을 빼고,
    - 돈을 받는 사람의 계좌에 돈을 넣는 단계가 있어요.
- 이 두 단계가 모두 성공해야 이체가 완료돼요. 만약 한 단계가 실패하면, 돈이 사라지거나 잘못될 수 있어요.
**자동 트랜잭션 관리**는 주방 관리자(스프링)가 이런 중요한 단계를 자동으로 관리해주는 거예요. 즉, 한 단계라도 실패하면 전체 과정을 되돌려서 안전하게 만드는 거예요.
### ==MVC의 풀네임과 실제 예시==
**MVC**의 풀네임은 **Model-View-Controller**에요. 요리책을 비유한 레시피는 실제로 다음과 같이 적용됩니다:
### Model-View-Controller (MVC)
1. **Model (모델)**:
    - **비유**: 레시피에 나오는 재료들
    - **설명**: 요리에 필요한 재료와 그 재료들이 어떻게 준비되어야 하는지에 대한 정보가 담겨 있어요.
    - **실제 예시**: 사용자의 정보, 데이터베이스의 데이터 등
2. **View (뷰)**:
    - **비유**: 레시피에 나오는 완성된 요리 사진
    - **설명**: 요리가 완성되었을 때 어떻게 보이는지에 대한 부분이에요. 요리를 어떻게 예쁘게 담아내야 하는지 보여주는 거죠.
    - **실제 예시**: 웹 페이지, 화면에 보여지는 내용들
3. **Controller (컨트롤러)**:
    - **비유**: 레시피의 단계별 요리 방법
    - **설명**: 요리사가 어떻게 요리를 만들어야 하는지 단계별로 설명해주는 부분이에요. 각 단계마다 무엇을 해야 하는지 알려줘요.
    - **실제 예시**: 사용자의 입력을 받아서 모델을 업데이트하고, 뷰를 선택해서 사용자에게 보여주는 로직
### MVC의 실제 예시
- **웹 애플리케이션**:
    - **Model**: 데이터베이스에서 사용자 정보를 가져오는 부분.
    - **View**: 사용자에게 보이는 웹 페이지, 예를 들어 로그인 페이지나 프로필 페이지.
    - **Controller**: 사용자가 로그인 버튼을 눌렀을 때, 사용자 정보를 확인하고 올바른지 체크한 후, 로그인 성공 메시지를 보여주는 부분.
이렇게 보면, 자동 트랜잭션 관리와 트랜잭션의 개념, 그리고 MVC가 실제로 어떻게 적용되는지 이해하기 더 쉬울 거예요.
  
### ==다용도 통합기의 실제 예시==
**다용도 통합기**는 주방에서 여러 도구를 연결하고 사용하는 것처럼, 스프링 프레임워크가 다양한 서비스와 도구들을 연결하고 통합하는 기능을 제공하는 것을 의미해요. 다음은 몇 가지 예시입니다.
### 1. 데이터베이스 연동
- **비유**: 주방에서 냉장고와 오븐을 사용하는 것.
- **설명**: 스프링은 애플리케이션이 데이터베이스와 쉽게 연동될 수 있도록 도와줘요.
- **실제 예시**: 스프링의 JDBC 모듈이나 JPA 모듈을 사용하면 데이터베이스와의 연결, 데이터 조회, 저장 등을 쉽게 할 수 있어요.
```Java
// 데이터베이스 연동 예시
@Repository
public class UserRepository {
    @Autowired
    private JdbcTemplate jdbcTemplate;
    public User findById(Long id) {
        return jdbcTemplate.queryForObject("SELECT * FROM users WHERE id = ?", new Object[]{id}, new UserRowMapper());
    }
}
```
### 2. 메시징 시스템 연동
- **비유**: 주방에서 믹서기와 냉장고를 동시에 사용하는 것.
- **설명**: 스프링은 메시징 시스템과의 통합을 지원해요. 이를 통해 애플리케이션 간 메시지를 주고받을 수 있어요.
- **실제 예시**: 스프링의 JMS 모듈을 사용하면, 메시지 큐를 통해 비동기적으로 메시지를 주고받을 수 있어요.
```Java
// 메시징 시스템 연동 예시
@Service
public class MessagingService {
    @Autowired
    private JmsTemplate jmsTemplate;
    public void sendMessage(String destination, String message) {
        jmsTemplate.convertAndSend(destination, message);
    }
}
```
### 3. 이메일 서비스 연동
- **비유**: 주방에서 오븐과 그릴을 함께 사용하는 것.
- **설명**: 스프링은 이메일 서비스를 쉽게 사용할 수 있게 해줘요. 이를 통해 애플리케이션에서 이메일을 보내는 기능을 구현할 수 있어요.
- **실제 예시**: 스프링의 JavaMailSender를 사용하면 이메일을 보낼 수 있어요.
```Java
// 이메일 서비스 연동 예시
@Service
public class EmailService {
    @Autowired
    private JavaMailSender mailSender;
    public void sendEmail(String to, String subject, String text) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(to);
        message.setSubject(subject);
        message.setText(text);
        mailSender.send(message);
    }
}
```
### 4. 웹 서비스 연동
- **비유**: 주방에서 냄비와 찜기를 함께 사용하는 것.
- **설명**: 스프링은 RESTful 웹 서비스나 SOAP 웹 서비스를 쉽게 만들고 사용할 수 있도록 도와줘요.
- **실제 예시**: 스프링의 RestTemplate이나 WebClient를 사용하면 다른 웹 서비스와 쉽게 통신할 수 있어요.
```Java
// 웹 서비스 연동 예시
@Service
public class WebServiceClient {
    @Autowired
    private RestTemplate restTemplate;
    public String getDataFromService(String url) {
        return restTemplate.getForObject(url, String.class);
    }
}
```
  
여기서 어려운 용어 10개를 뽑아 각각 설명을 표로 정리해볼게요.
|   |   |
|---|---|
|용어|설명|
|JDBC (Java Database Connectivity)|자바 애플리케이션이 데이터베이스와 연결하고 데이터를 주고받을 수 있게 해주는 표준 API.|
|JPA (Java Persistence API)|자바 객체를 데이터베이스에 쉽게 저장하고 불러올 수 있게 해주는 API. ORM (객체 관계 매핑) 기술을 사용.|
|Repository|데이터베이스와 상호 작용하는 객체. 데이터를 저장하고 검색하는 메서드를 제공.|
|JdbcTemplate|스프링에서 제공하는 클래스로, JDBC를 사용한 데이터베이스 연동을 더 쉽게 해줌.|
|JmsTemplate|스프링에서 제공하는 클래스로, JMS (Java Message Service)를 사용한 메시징 기능을 더 쉽게 해줌.|
|JavaMailSender|스프링에서 이메일을 보내기 위해 사용하는 인터페이스. 이메일 전송을 위한 다양한 메서드를 제공.|
|SimpleMailMessage|간단한 이메일 메시지를 만들기 위한 스프링 클래스. 수신자, 제목, 본문 등의 속성을 설정할 수 있음.|
|RestTemplate|스프링에서 제공하는 클래스로, RESTful 웹 서비스와 통신하기 위해 사용. HTTP 요청을 보내고 응답을 처리.|
|WebClient|스프링에서 제공하는 비동기 방식의 HTTP 클라이언트로, RESTful 웹 서비스와 통신하기 위해 사용.|
|RESTful 웹 서비스|웹을 통해 데이터를 주고받는 방식. REST (Representational State Transfer) 원칙을 따르며, HTTP 메서드를 사용해 자원을 관리.|
  
### ==요약==
- **IoC**는 주방 관리자(스프링 컨테이너)가 요리사(애플리케이션 코드)를 대신해서 필요한 도구(객체)를 준비하고 관리하는 것.
- **DI**는 주방 관리자(스프링 컨테이너)가 요리사(애플리케이션 코드)에게 필요한 도구(객체)를 직접 손에 쥐어주는 것.
- **AOP**는 주방의 비법 노트처럼, 모든 요리에 공통으로 적용되는 비법(기능)을 따로 정리해서 비즈니스 로직과 분리하여 관리하는 것.
- 다용도 통합기는 스프링이 다양한 외부 서비스와 애플리케이션을 쉽게 연결하고 사용할 수 있게 해주는 기능을 의미해요. 데이터베이스, 메시징 시스템, 이메일 서비스, 웹 서비스 등 다양한 서비스와의 연동을 통해 애플리케이션 개발을 더 쉽고 효율적으로 만들 수 있어요.
  
## 스프링 프레임워크를 사용한 프로젝트 예시
### 온라인 쇼핑몰 프로젝트
**프로젝트 개요**:
- **목적**: 사용자들이 상품을 검색하고, 장바구니에 담고, 결제할 수 있는 온라인 쇼핑몰을 구축.
- **기능**: 사용자 관리, 상품 관리, 장바구니, 주문 및 결제, 리뷰 및 평점, 관리자 대시보드 등.
### 주요 구성 요소 및 스프링 프레임워크 사용 예시
1. **사용자 관리**:
    
    - **비유**: 주방에서 요리사가 회원들을 관리하는 것.
    - **사용된 스프링 기능**: 스프링 시큐리티를 사용하여 사용자 인증 및 권한 관리.
    
    ```Java
    @Configuration
    @EnableWebSecurity
    public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
        @Override
        protected void configure(HttpSecurity http) throws Exception {
            http
                .authorizeRequests()
                    .antMatchers("/", "/home").permitAll()
                    .anyRequest().authenticated()
                    .and()
                .formLogin()
                    .loginPage("/login")
                    .permitAll()
                    .and()
                .logout()
                    .permitAll();
        }
    }
    ```
    
2. **상품 관리**:
    
    - **비유**: 주방에서 요리사가 재료를 관리하는 것.
    - **사용된 스프링 기능**: 스프링 데이터 JPA를 사용하여 상품 정보를 데이터베이스에 저장하고 조회.
    
    ```Java
    @Entity
    public class Product {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
        private String name;
        private Double price;
        // getters and setters
    }
    
    public interface ProductRepository extends JpaRepository<Product, Long> {
    }
    ```
    
3. **장바구니 및 주문**:
    
    - **비유**: 주방에서 손님이 요리를 주문하고 주방이 이를 처리하는 것.
    - **사용된 스프링 기능**: 스프링 MVC를 사용하여 장바구니와 주문 기능을 구현.
    
    ```Java
    @Controller
    public class CartController {
        @Autowired
        private CartService cartService;
    
        @GetMapping("/cart")
        public String viewCart(Model model) {
            model.addAttribute("cartItems", cartService.getCartItems());
            return "cart";
        }
    
        @PostMapping("/cart")
        public String addToCart(@RequestParam Long productId) {
            cartService.addToCart(productId);
            return "redirect:/cart";
        }
    }
    ```
    
4. **결제 처리**:
    
    - **비유**: 주방에서 손님이 요리를 먹고 결제하는 것.
    - **사용된 스프링 기능**: 스프링 통합을 사용하여 외부 결제 서비스와 통합.
    
    ```Java
    @Service
    public class PaymentService {
        @Autowired
        private RestTemplate restTemplate;
    
        public PaymentResponse processPayment(PaymentRequest request) {
            return restTemplate.postForObject("<https://payment-gateway.com/api/pay>", request, PaymentResponse.class);
        }
    }
    ```
    
5. **리뷰 및 평점**:
    
    - **비유**: 손님이 요리의 맛과 서비스를 평가하는 것.
    - **사용된 스프링 기능**: 스프링 데이터 JPA를 사용하여 리뷰와 평점 데이터를 관리.
    
    ```Java
    @Entity
    public class Review {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
        private Long productId;
        private String reviewText;
        private int rating;
        // getters and setters
    }
    
    public interface ReviewRepository extends JpaRepository<Review, Long> {
        List<Review> findByProductId(Long productId);
    }
    ```
    
### 결론
이 예시는 온라인 쇼핑몰 프로젝트에서 스프링 프레임워크의 다양한 기능을 어떻게 활용할 수 있는지 보여줍니다. 스프링 시큐리티, 스프링 데이터 JPA, 스프링 MVC, 그리고 스프링 통합을 사용하여 사용자 인증, 데이터 관리, 웹 애플리케이션 기능, 외부 서비스 연동 등을 쉽게 구현할 수 있습니다.
## MVC란?
- [ ] MVC란 무엇인가?
- [ ] (MVC 대략적인 내용 파악하고 질문거리 생각해본 후 진행하기)
  
## 스프링과 DB
- [ ] JPA, 하이버네이트, JDBC가 각각 무엇이고 서로의 차이점이 무엇인가. 각각의 장단점 표로 정리하기.
  
### 개념 설명
1. **JPA (Java Persistence API)**:
    - 자바 애플리케이션에서 데이터베이스 작업을 수행하기 위한 표준 API.
    - 객체지향 프로그래밍의 개념을 데이터베이스에 적용해 객체와 관계형 데이터베이스를 매핑함.
2. **Hibernate (하이버네이트)**:
    - JPA의 구현체 중 하나로, 자바 애플리케이션에서 데이터를 영구 저장하기 위한 ORM 프레임워크.
    - JPA의 표준 인터페이스를 구현하여 다양한 기능을 제공함.
3. **JDBC (Java Database Connectivity)**:
    - 자바에서 데이터베이스에 접근하기 위한 표준 API.
    - SQL 쿼리를 사용해 데이터베이스와 직접 상호작용함.
### 차이점
|   |   |   |   |
|---|---|---|---|
|항목|JPA|Hibernate|JDBC|
|**개념**|자바에서 ORM을 위한 표준 API|JPA의 구현체 중 하나|자바에서 데이터베이스와의 직접 상호작용을 위한 표준 API|
|**기능**|객체와 관계형 데이터베이스 매핑|JPA 표준을 따르며 추가 기능 제공|SQL 쿼리를 통해 데이터베이스와 직접 상호작용|
|**복잡도**|중간|중간~높음|높음|
|**유연성**|높음|높음|중간|
|**표준화**|표준 API|JPA 표준을 따름|표준 API|
### 장단점
|   |   |   |
|---|---|---|
|항목|장점|단점|
|**JPA**|- 객체지향 프로그래밍과 데이터베이스 간의 매핑이 용이  <br>  <br>- 코드의 가독성 및 유지보수성 향상  <br>  <br>- SQL의 자동 생성 및 실행  <br>  <br>- 애플리케이션과 데이터베이스 간의 결합도 감소|- 학습 곡선이 높음  <br>  <br>- 복잡한 쿼리의 경우 성능 저하 가능성  <br>  <br>- 특정 상황에서 예상치 못한 동작 발생 가능성|
|**Hibernate**|- JPA의 모든 장점 포함  <br>  <br>- 풍부한 추가 기능 제공 (캐싱, 고급 매핑 등)  <br>  <br>- 다양한 데이터베이스 지원  <br>  <br>- 복잡한 쿼리를 위한 HQL 지원|- JPA보다 학습 곡선이 더 높음  <br>  <br>- 성능 튜닝이 필요할 수 있음  <br>  <br>- 프로젝트 크기에 따라 초기 설정이 복잡할 수 있음|
|**JDBC**|- 데이터베이스와의 직접 상호작용으로 높은 제어력 제공  <br>  <br>- 단순한 데이터베이스 작업에 적합  <br>  <br>- 모든 관계형 데이터베이스에서 사용 가능|- 코드가 장황하고 반복적임  <br>  <br>- 데이터베이스 종속적인 코드 발생 가능성  <br>  <br>- 유지보수 및 확장성 저하|
### 요약
- **JPA**는 객체지향 프로그래밍과 데이터베이스 작업을 결합한 표준 API로, 유지보수성과 가독성을 높이지만 학습 곡선이 높고 복잡한 쿼리에서 성능 저하가 있을 수 있음.
- **Hibernate**는 JPA의 구현체로, JPA의 장점에 더해 다양한 추가 기능을 제공하지만 학습 곡선이 더 높고 초기 설정이 복잡할 수 있음.
- **JDBC**는 SQL 쿼리를 사용해 데이터베이스와 직접 상호작용하며, 단순한 작업에는 적합하지만 코드가 장황해지고 유지보수성이 떨어짐.
이 표를 통해 JPA, Hibernate, JDBC의 차이점과 각각의 장단점을 쉽게 이해할 수 있을 거예요.
## 스프링으로 로그인/로그아웃 구현하기
- [ ] JWT, 스프링 시큐리티가 무엇이고 서로의 차이점, 장단점 정리하기
  
## JUnit이란?
- [ ] JUnit이 무엇인가?
  
## AWS로 서비스 배포하기
- [ ] AWS 배포에는 어떤 툴을 사용하는가?
- [ ] AWS에는 대표적으로 어떤 서비스가 있고 우리가 사용할만한 기능에는 무엇이 있는가?