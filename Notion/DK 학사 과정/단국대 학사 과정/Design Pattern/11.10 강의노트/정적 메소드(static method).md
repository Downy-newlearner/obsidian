1. 인스턴스 생성 없이 호출이 가능하다.
    
    (인스턴스 생성 후 호출도 가능하지만 지양하고있다.)
    
    ```Java
    public class Test {
    	public static void sm() {        
    		System.out.println("this is static method!");    
    	}     
    
    	public void m() {        
    		System.out.println("this is non-static method!");    
    	}
    } 
    public class Main {    
    	public static void main(String[] args) {        
    		Test.sm(); // O        
    		Test.m(); // X         
    		
    		Test test = new Test();        
    		test.sm(); // X        
    		test.m(); // O    
    	}
    }
    ```
    
    위처럼 가능한 이유는 말 그대로 “정적”이기 떄문에, 클래스가 메모리에 올라갈 때 정적 메소드가 자동적으로 생성된다.
    
    그렇기에 인스턴스를 생성하지 않고, 클래스만으로 메소드를 호출할 수 있는 것이다.
    
      
    
2. 유틸리티 관련 함수를 만드는데 유용하게 사용된다.
    
    넓은 범위에 걸쳐 사용할 수 있는 실용적인 프로그램, 또는 시스템에 따르는 소프트웨어를 유틸리티 프로그램이라고 한다.