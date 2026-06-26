
# # 키보드로부터 입력 받는 함수 input

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"You entered: {a} and {b}")
# print(f"a + b = {(a) + (b)}")
# print(f"a - b = {(a) - (b)}")
# print(f"a * b = {(a) * (b)}")
# print(f"a / b = {(a) / (b)}")

# 리스트 자료형

# a = []
# b = [1, 2, 3]
# c = ['Life', 'is', 'too', 'short']
# d = [1, 2, 'Life', 'is']
# e = [1, 2, ['Life', 'is']]

    # 1번 문제 코드
print("=== 1. 사칙연산 프로그램 ===")

# 두 정수 입력받기
num1 = int(input("3: "))
num2 = int(input("9: "))

# 사칙연산 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# 0으로 나누는 경우 예외 처리
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")