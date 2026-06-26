# print("=== [문제 1] 사칙연산 프로그램 ===")

# # input()으로 받은 값은 '문자(str)'이므로 int()를 이용해 '정수'로 변환합니다.
# num1 = int(input("첫 번째 정수를 입력하세요: "))
# num2 = int(input("두 번째 정수를 입력하세요: "))

# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")

# # 나눗셈할 때 분모가 0이면 에러가 나므로 조건문으로 방어해 줍니다.
# if num2 != 0:
#     print(f"{num1} / {num2} = {num1 / num2}")
# else:
#     print("0으로 나눌 수 없습니다.")



# num1 = int(input("첫 번째 정수를 입력하세요: "))
# num2 = int(input("두 번째 정수를 입력하세요: "))
# num3 = int(input("세 번째 정수를 입력하세요: "))
# num4 = int(input("네 번째 정수를 입력하세요: "))
# num5 = int(input("다섯 번째 정수를 입력하세요: "))
# number = [num1, num2, num3, num4, num5]
# print(f"sum = {sum(number)}")
# print(f"average = {sum(number)/len(number)}")
# print(f"maximum = {max(number)}")
# print(f"minimum = {min(number)}")

# fruits = []
# fruits = input("Enter a fruits: ")
# fruits.append(fruits)
# fruits = input("Enter a fruits: ")
# fruits.append(fruits)
# fruits = input("Enter a fruits: ")
# fruits.append(fruits)
# fruits = input("Enter a fruits: ")
# fruits.append(fruits)
# fruits = input("Enter a fruits: ")
# fruits.append(fruits)
# print(fruits)
# print(fruits[0])
# print(fruits[-1])