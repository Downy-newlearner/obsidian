  
- 디자인 패턴은 객체 지향 다음 이야기다.
    - ‘데이터 간의 관계가 어떻냐’는 이야기.
  
- 자바의 Control Structures
    - if
    - if, else
    - if, else if, esle if, … , else
    - switch case
    - while
    - do while
    - for
  
- 접근 지정자
    
    ![[Source/Untitled 140.png|Untitled 140.png]]
    
    - protected의 포인트는 다른 패키지에 본인의 자식 클래스가 있다면 그 클래스에서만 접근 가능하고, 해당 패키지의 다른 클래스에서는 접근할 수 없다는 점이다. (즉 다른 패키지에선 본인의 자식 클래스만 이 멤버에 접근할 수 있다.)
    - private를 하면 동일 클래스에서만 접근할 수 있으므로, 같은 패키지의 자식 클래스에서도 접근할 수 없다.
  
- JAVA 파일의 구성
    - 필드: 클래스에 포함된 변수(인스턴스 변수, 클래스 변수)
    - 생성자
    - 메소드
  
- String은 참조형 데이터 타입이다.
  
- 변수의 4요소
    - Name
    - Reference
    - Type
    - Value
  
- L-value vs. R-value
    - L : Reference (주소값)
    - R : value (주소 안의 실제 값)
  
- Memory Leak
    - 컴퓨터 프로그램이 필요하지 않은 메모리를 계속 점유하고 있는 현상.
    - Java는 Garbage Collector로 해결한다.
  
- Dangling Pointer
    - 다른 포인터에서 동일한 주소를 지목하는 것이다.
    - Java는 malloc이 아닌 new로 해결한다.
  
### 객체 생성
- 코드(암기 3)
    
    ```Java
    public class MyClass{
    	public void greeting(){
    		System.out.println("Hello World!");
    	}
    }
    
    public class MyMain{
    	public static void main(String[] args)
    	{
    		MyClass hello = new MyClass();
    		hello.greeting();
    	}
    }
    ```
    
- MyClass hello까지가 declare, new MyClass()를 construct 한다.
- hello 객체에 greeting()이라는 메세지를 sending 한다.
  
### 다형성
- 코드(암기2)
    
    ```Java
    public interface Pet{
    	public void makeSound();
    }
    
    public class Dog implements Pet{
    	public void makeSound(){
    		bark();
    	}
    
    	public void bark(){
    		System.out.println("멍멍");
    	}
    }
    
    public class Cat implements Pet{
    		public void makeSound(){
    		meow();
    	}
    
    	public void meow(){
    		System.out.println("야옹");
    	}
    }
    
    public class PetMain{
    	public static void main(String[] args)
    	{
    		Pet myPet;
    		myPet = new Dog();
    		myPet.makeSound();
    		myPet = new Cat();
    		myPet.makeSound();
    	}
    }
    ```
    
- 오버 로딩 : 과적재, 같은 이름이더라도 파라미터의 차이로 구분 가능
- 오버 라이딩 : 부모의 매서드를 재정의
    - 안 좋은 징조, 코드의 재사용을 안함
    - 상속은 코드의 재사용을 하려고 하는 것이기 때문에
## 객체 지향
추상화 캡슐화 모듈화 계층
객체 지향의 의의는 코드를 재사용해서 구조화된 체계를 만들 수 있다는 것이다.
→ 좋은 코드를 상속하여 계속 사용
  
  
## 원시 타입(Primitive) vs. 참조 타입(Reference) 자료형
자바에서 데이터 타입은 크게 두 가지로 나눌 수 있다.
Primitive type(원시 타입)과 Reference type(참조 타입)이다.
  
1. 원시 타입
    - 정수, 실수, 문자, 논리 리터럴 등의 ==실제 데이터== 값을 저장하는 타입.
    - int, long, double, float, boolean …
    - 사용하기 전에 선언되어야한다.
    - 스택 메모리에 저장된다.
    - 객체 생성 없이 바로 사용할 수 있다.
  
1. 참조 타입
    
    - 주소를 저장하여 메모리 번지 값을 통해 객체를 참조하는 타입이다.
    - Integer, Long, Double, Byte, Char …
    - 원시 타입을 제외한 타입들이다.
        - 문자열, 배열, 열거, 클래스, 인터페이스
    - ==‘실제 객체’==는 ==힙 메모리==에 저장되고, ==참조타입 변수==는 ==스택 메모리==에 ‘실제 객체’들의 ==주소==를 저장한다.
    
      
    
  
## Terms
- 좋은 코드란?
    
    - 적응할 수 있는 코드이다.
    
      
    
- 패러다임
    
    - 같은 것을 봐도 생각하는 관점에 따라서 완전히 다르게 보일 수 있는 것
    - 패러다임이 변하는 것을 패러다임 시프트라고 한다.
    - 객체 지향은 패러다임 시프트이다.
    
      
    
- 인스턴스
    
    - 클래스를 통해 생성된 객체이다.
    - 즉, 인스턴스화되어 구체적인 실체를 갖게 된 객체
    - 힙 메모리의 독립적인 공간에 저장된다
    
      
    
- 객체
    
    - 자료형이 클래스 타입인 변수
    
      
    
- 필드
    - ==클래스에 포함된 변수이다.==
        1. 인스턴스 변수
            
            인스턴스가 가지는 속성을 저장하기 위한 변수이다.
            
            ‘new 생성자()’ 를 통해 인스턴스가 생성될 때 만들어진다.
            
            동일한 클래스로부터 생성된 인스턴스들이라고 할지라도 객체의 고유한 개별성을 가진다.
            
        2. 클래스 변수
            
            인스턴스 변수와는 다르게 공통된 저장공간을 공유한다.
            
            한 클래스로부터 생성되는 모든 인스턴스들이 특정한 값을 공유해야하는 경우에 static 키워드를 사용하여 선언하게 된다.
            
              
            
- Attribute(속성)
    
    - Attribute는 클래스의 속성을 의미한다.
    - 즉, 필드를 의미한다.
    - 객체는 class의 attribute를 상속하는 것이다.
    
      
    
- Is-a, Has-a
    
    - is-a 관계는 Inheritance, 즉 상속이다.
    - 상속은 일반 클래스를 구체화 하는 상황에서 사용한다.
    - 상속을 하면 하위 클래스가 상위 클래스에 종속된다.
    
      
    
    - has-a 관계는 association, 즉 포함이다.
    - 포함 관계는 다른 클래스의 기능(변수나 메서드)를 받아들여 사용한다.
    - 예시로, 옵저버 패턴에서 옵저버들이 subject 인스턴스를 받아들여 사용한다.
        - 옵저버가 subject과 association 관계가 생김으로서, subject의 정보들(temparature, humidity, pressure, 이외 여러 메서드들)을 받아오고 사용할 수 있다.