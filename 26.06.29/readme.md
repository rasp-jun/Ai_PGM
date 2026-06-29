# 🐍 Python 기초 문법 정리

Python에서 가장 많이 사용하는 기초 문법을 정리한 저장소입니다.

---

## 📚 목차

* 조건문 (if)
* 반복문 (while)
* 반복문 (for)
* 함수(Function)
* 입출력(Input / Output)
* 파일 읽기/쓰기(File I/O)

---

# 🔹 조건문 (if)

조건에 따라 코드를 실행할 때 사용합니다.

## 기본 문법

```python
if 조건식:
    실행문
```

### 예제

```python
age = 20

if age >= 19:
    print("성인입니다.")
```

---

## if - else

```python
if score >= 60:
    print("합격")
else:
    print("불합격")
```

---

## if - elif - else

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

---

## 비교 연산자

| 연산자 | 설명     |
| --- | ------ |
| ==  | 같다     |
| !=  | 다르다    |
| >   | 크다     |
| <   | 작다     |
| >=  | 크거나 같다 |
| <=  | 작거나 같다 |

---

## 논리 연산자

| 연산자 | 설명      |
| --- | ------- |
| and | 모두 참    |
| or  | 하나 이상 참 |
| not | 반대      |

---

# 🔁 while 반복문

조건이 참인 동안 계속 반복합니다.

## 기본 문법

```python
while 조건식:
    실행문
```

### 예제

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

출력

```
1
2
3
4
5
```

---

## break

반복 종료

```python
while True:
    cmd = input()

    if cmd == "exit":
        break
```

---

## continue

현재 반복만 건너뜁니다.

```python
num = 0

while num < 5:
    num += 1

    if num == 3:
        continue

    print(num)
```

출력

```
1
2
4
5
```

---

# 🔄 for 반복문

반복 가능한 객체를 순회합니다.

## 기본 문법

```python
for 변수 in 반복가능객체:
    실행문
```

---

## range()

```python
for i in range(5):
    print(i)
```

출력

```
0
1
2
3
4
```

---

## 시작, 종료

```python
for i in range(1, 6):
    print(i)
```

---

## 증가값 지정

```python
for i in range(0, 11, 2):
    print(i)
```

출력

```
0
2
4
6
8
10
```

---

## 리스트 반복

```python
fruits = ["사과", "바나나", "포도"]

for fruit in fruits:
    print(fruit)
```

---

## 문자열 반복

```python
for ch in "Python":
    print(ch)
```

---

## enumerate()

```python
fruits = ["사과", "바나나", "포도"]

for index, value in enumerate(fruits):
    print(index, value)
```

---

# ⚙ 함수(Function)

특정 기능을 하나로 묶은 코드입니다.

## 함수 정의

```python
def hello():
    print("Hello Python")
```

호출

```python
hello()
```

---

## 매개변수

```python
def hello(name):
    print(name)
```

호출

```python
hello("홍길동")
```

---

## 반환값(return)

```python
def add(a, b):
    return a + b
```

```python
result = add(10, 20)

print(result)
```

출력

```
30
```

---

## 기본 매개변수

```python
def hello(name="Python"):
    print(name)
```

---

## 여러 값 반환

```python
def calc(a, b):
    return a+b, a-b
```

```python
sum_value, sub_value = calc(10,5)
```

---

# ⌨ 입출력(Input / Output)

## 입력

```python
name = input("이름 입력 : ")
```

---

## 숫자 입력

```python
age = int(input("나이 입력 : "))
```

---

## 실수 입력

```python
height = float(input("키 입력 : "))
```

---

## 출력

```python
print("Hello Python")
```

---

## sep

```python
print("A", "B", "C", sep="-")
```

출력

```
A-B-C
```

---

## end

```python
print("Hello", end=" ")
print("Python")
```

출력

```
Hello Python
```

---

## f-string

```python
name = "Tom"
age = 20

print(f"이름 : {name}")
print(f"나이 : {age}")
```

---

# 📂 파일 읽기/쓰기

## 파일 열기

```python
open("파일명", "모드")
```

---

## 파일 모드

| 모드 | 설명           |
| -- | ------------ |
| r  | 읽기           |
| w  | 쓰기(기존 내용 삭제) |
| a  | 이어쓰기         |
| x  | 새 파일 생성      |
| rb | 바이너리 읽기      |
| wb | 바이너리 쓰기      |

---

## 파일 쓰기

```python
file = open("test.txt", "w")

file.write("Hello Python")

file.close()
```

---

## 파일 읽기

```python
file = open("test.txt", "r")

text = file.read()

print(text)

file.close()
```

---

## readline()

```python
file = open("test.txt")

line = file.readline()

print(line)

file.close()
```

---

## readlines()

```python
file = open("test.txt")

lines = file.readlines()

print(lines)

file.close()
```

---

## 한 줄씩 읽기

```python
with open("test.txt", "r") as file:
    for line in file:
        print(line)
```

---

## with 문

파일을 자동으로 닫아줍니다.

```python
with open("test.txt", "w") as file:
    file.write("Python")
```

---

# 📌 핵심 정리

| 문법          | 용도           |
| ----------- | ------------ |
| if          | 조건 실행        |
| while       | 조건 반복        |
| for         | 반복 가능한 객체 순회 |
| def         | 함수 정의        |
| return      | 값 반환         |
| input()     | 입력           |
| print()     | 출력           |
| open()      | 파일 열기        |
| read()      | 파일 전체 읽기     |
| write()     | 파일 쓰기        |
| with open() | 자동 파일 닫기     |

---

# 🚀 자주 사용하는 내장 함수

| 함수          | 설명        |
| ----------- | --------- |
| print()     | 출력        |
| input()     | 입력        |
| len()       | 길이        |
| range()     | 반복        |
| enumerate() | 인덱스와 값 반환 |
| int()       | 정수 변환     |
| float()     | 실수 변환     |
| str()       | 문자열 변환    |
| type()      | 자료형 확인    |
| open()      | 파일 열기     |

---

## 📖 학습 순서 추천

```
변수
   ↓
자료형
   ↓
if
   ↓
while
   ↓
for
   ↓
함수
   ↓
입출력
   ↓
파일 입출력
```

---

⭐ 이 저장소는 Python 기초 문법을 빠르게 복습하기 위한 요약 노트입니다.
