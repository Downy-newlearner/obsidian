Trust : 신뢰의 정도를 나타냄(확실한 답을 피할 때 사용)
Secure : 0 or 1(100% 또는 0%)
---
### 개요
**보안의 정의**
**보안의 종류**
정보 보안
컴퓨터 보안
사이버 보안
셋이 같은 용어이다.
  
# 1. Data, Information, Information System
---
p.7~8
범용 컴퓨터
데스크탑, 랩탑, 태블릿
특수 컴퓨터
임베디드 디바이스: 냉장고, 라우터, 로봇청소기, AP
  
기본적으로 컴퓨터는 데이터, 정보를 자동으로 처리한다.
---
p. 9
컴퓨터의 오퍼랜드는 데이터,정보이다.
**데이터**
날것, 조직화되어있지 않은 것, 처리가 안 된 것.
처리의 입력(Input to a Process)
**정보**
유의미한것, 조직화되어있는 것, 처리가 되어있는것
처리의 출력(Output of a Process)
  
데이터와 정보는 가장 중요한 자산이다. 그러므로 안전하게 지킬 필요가 있다.
---
  
p. 11 12 13 14 15 Terminology
  
**IT**
기본적으로 네트워크를 고려하여 구축된 기술이다.
데이터나 정보를 자동화된 수집, 관리, 조작, 이동하는데 사용되는 장비 또는 시스템이 IT에 필요한 요소들이다.
컴퓨터, 보조 장비(프린터, 키보드 등), 소프트웨어, 펌웨어, 서비스 등을 포함한다.(핵심은 컴퓨터)
컴퓨터 시스템이나 네트워크를 개발하고 사용하는 기술
  
![[Source/Untitled 56.png|Untitled 56.png]]
  
**System**
체제 또는 장비, 모든 될 수 있다.
기본적으로 어떤 집합이다.
시스템이 되기 위해서는 어떠한 질서가 필요하다.
  
**SDLC(Software Development Life Cycle)**
소프트웨어 개발 수명 주기
요구사항 분석 → 설계 → 구현 → 테스팅 → 배포
  
**IT System**
자원과 절차의 집합이다.
  
**Information System**
IT Sytem과 같은 말이다.
처리 유지 관리 배포를 위해 구성된 자원의 집합.
자원이란 HW 자원, SW 자원, Data 자원, Communication 자원, 인적 자원 등을 모두 포함한다.
  
---
# 2. Security(Computer Security, Cyber Security)
---
p.17 18 19
**Security**
위험이 없는 상태(free from danger(threat/risk/vulnerability))
  
**보안의 필수적인 목적(CIA)**
**Confidentiality(비밀성, 기밀성)**
정보는 권한아래 접근 가능해야한다.
정보 유출은 기밀성을 공격한다.
  
**Integrity(무결성)**
데이터는 변조되지 않고, 오염되지 않아야한다.
변조는 무결성을 공격한다.
  
**Availability(가용성)**
필요할 때 데이터나 시스템에 접근할 수 있어야한다.
데이터/서버 이중화로 실현할 수 있다.
디도스는 가용성을 공격한다.
  
**추가 컨셉**
**Identification&Authentication(식별&인증)**
기기 식별: IP, MAC, Port
사람 식별: ID, E-mail
인증은 내가 나라는 것을 증명하는 것을 말한다.
예를들어 지문, Password이 있다.
위조는 인증을 공격한다.
**Accountability(책임 추적성)**
유저을 추적해서 행동에 책임을 물을 수 있도록 하는 것
예를들어 로깅이 있다.
**Privacy(프라이버시)**