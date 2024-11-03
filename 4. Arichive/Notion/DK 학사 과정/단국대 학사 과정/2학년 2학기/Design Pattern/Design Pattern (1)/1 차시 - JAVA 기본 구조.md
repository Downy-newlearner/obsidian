```Java
public class MyClass{
	public static void main(String[] args)
	{
		System.out.println("Hello world");
	}
}
```
- 키워드가 아닌 것
    
    - MyClass, args, main, System.out.println, “Hello World.” 문자열, String
    
      
    
- public은 왜 쓰냐?
    - 외부 에서 접근 할 수 있도록 해주는 접근제한자
  
- class는 무슨 소리냐?
    - 클래스를 선언 하기 위한 구문
    - 인스턴스는 변수처럼 사용하기 위함
    - 오브젝트 클래스는 define 한다.
    - 사용을 위해선 declare를 해야한다.
  
- static은 무슨 소리인가?
    - 정적으로 만든다.
    - 선언하기 전에 메모리에 생긴다.
  
- 메소드를 static으로 만들면 declare 하지 않아도 존재하게 되고 사용할 수 있다.
- 클래스의 종속도 하나만 만들어진다.
  
- void
    - 리턴 값을 정의하지 않겠다.
  
- String[]
    - String 타입의 배열
    - 그러나 String은 키워드가 아니다.
  
- System.out.println()
    - System 패키지에 out 클래스의 println 매소드를 사용
  
- 라이브러리는 매소드만 있는 것 이므로 클래스 라이브러리라는 말이 맞다.
  
### 객체 생성
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
  
### Attribute와 리턴 값
- class 변수
  
### 암기 1.
```Java
public class OurClass{
	private String myName;
	public void setMyName(String name)
	{
		myName = name;
	}
	public String whoAmI()
	{
		return myName;
	}
}
public class OurMain{
	public static void main(String[] args)
	{
		OurClass hi = new OurClass();
		hi.setMyName("Im");
		System.out.println("Hello" + hi.whoAmI() + "!");
	}
}
```
  
### 다형성
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
  
### Primitive Type vs. Reference Type + overload
Integral type : int, short, long, byte
Floating type : float, double
Textual type : char
Logical type : boolean
- 실제 사용하는 메모리 공간을 잡아먹는다.
- 객체 생성 없이 바로 쓸 수 있는 자료형
  
```Java
public class Man{
	private int age = 0;
	public void setAge(int age){
		this.age  = age;
	}
}
Man kim = new Man();
kim.setAge(3);
```
  
  
## Memory and Variables
변수의 4요소
- Name
- Reference
- Type
- Value
  
- L-value vs. R-value
    - L : Reference (주소값)
    - R : value! 내부적인
  
### Memory leak, Dangling pointer
값에 주소값이 들어가면 레퍼런스 타입 변수 이다.
  
memory leak : 생성된 메모리로 부터 갈 수 있는 방법이 없어짐
dangling pointer : 다른 곳에서 동일한 장소를 지정
  
### Call by Value vs. Call by Reference
- 값 타입의 전달은 복사되므로 원본이 변경되지 않는다.
- 레퍼런스 타입은 주소가 복사되므로 원본이 변경된다.