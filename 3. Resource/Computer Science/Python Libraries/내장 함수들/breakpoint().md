---
created: 2024-11-24
tags: 
aliases:
  - 중단점
  - break
reference:
---
`breakpoint()`는 Python의 디버거(`pdb` 모듈)를 활성화하여 코드 실행을 중단하고 현재 상태를 탐색하거나 디버깅할 수 있도록 합니다. 실행 중 디버깅 명령어를 입력해 코드의 흐름을 제어하고 변수 상태를 확인할 수 있습니다.

---

### **기본 디버거 명령어**

디버거 활성화 시 사용할 수 있는 주요 명령어는 다음과 같습니다:

#### **1. n (next)**

- 현재 줄을 실행하고 다음 줄로 이동합니다.
- 함수 호출이 포함된 줄일 경우, 함수 내부로 들어가지 않고 한 줄만 실행합니다.

#### **2. s (step)**

- 현재 줄을 실행하고, 함수 호출이 있는 경우 해당 함수 내부로 진입합니다.
- 함수 내부의 세부 동작을 확인하고 싶을 때 사용합니다.

#### **3. c (continue)**

- 디버거를 종료하지 않고, 다음 중단점(breakpoint)까지 실행을 계속합니다.

#### **4. l (list)**

- 현재 실행 중인 코드의 주변 줄을 표시합니다.
- 디버깅 위치를 확인하거나 코드를 검토할 때 유용합니다.

#### **5. p (print)**

- 특정 변수나 표현식의 값을 출력합니다.
- 사용 예:
    
    ```python
    p variable_name
    ```
    

#### **6. q (quit)**

- 디버거를 종료하고 프로그램 실행을 중단합니다.

#### **7. b (break)**

- 새 중단점을 설정합니다.
- 사용 예:
    
    ```python
    b 42  # 42번 줄에 중단점 설정
    b my_function  # 함수 이름으로 중단점 설정
    ```
    

#### **8. clear**

- 설정된 중단점을 삭제합니다.
- 사용 예:
    
    ```python
    clear 42  # 42번 줄의 중단점 삭제
    clear  # 모든 중단점 삭제
    ```
    

#### **9. h (help)**

- 사용 가능한 디버거 명령어를 표시합니다.
- 특정 명령어에 대한 도움말도 확인 가능:
    
    ```python
    h n  # 'n' 명령어에 대한 도움말
    ```
    

---

### **사용 예제**

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    x = 10
    y = 20
    breakpoint()  # 디버거 활성화
    result = add(x, y)
    print("Addition Result:", result)
    result = multiply(x, y)
    print("Multiplication Result:", result)

main()
```

#### 디버거 실행 중:

```plaintext
> test.py(12)main()
-> result = add(x, y)
(Pdb) n  # 다음 줄로 이동
(Pdb) p x  # x의 값 출력
10
(Pdb) s  # 함수 add 내부로 진입
> test.py(2)add()
-> return a + b
(Pdb) p a  # a의 값 출력
10
(Pdb) p b  # b의 값 출력
20
(Pdb) c  # 디버거 종료 후 계속 실행
```

---

### **요약**

`breakpoint()`는 실행 중 디버깅을 위해 코드 흐름을 제어하고 변수 상태를 탐색할 수 있는 도구입니다. 주요 명령어는 **`n`(다음 줄 실행), `s`(함수 내부 진입), `p`(변수 출력), `q`(종료)** 등입니다.