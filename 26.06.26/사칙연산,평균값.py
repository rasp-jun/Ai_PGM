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





# list1 = list()
# list2 = []

# str1 = "abcd"
# str2 = ['a', 'b', 'c', 'd']

# t1 = tuple()
# t2 = ()
# t3 = tuple([1, 2, 3, 4])


# tup1 = (1) #tup1에 1을 할당하는 명령
# tup2 = (1,) # 1값을 가진 튜플

# set([1, 2, 3, 4, 5])

# dict1 = {1: "apple", "ba": "banana", 3: "cherry"}
# print(dict1[1]) # apple
# print(dict1["ba"]) # banana
# print(dict1[3]) # cherry

# stud1 = {"name": "홍길동", "age": 20, "address": "서울시 강남구"}
# print(stud1["name"]) # 홍길동
# print(stud1["age"]) # 20
# print(stud1["address"]) # 서울시 강남구




# money = int(input("현재 보유 금액 입력 : "))

# if money >= 20000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# print("Good Night")




# ent = 10000
# age = int(input("나이 입력 : "))

# if age >= 20:
#     ent = ent + ent * 0.1

# print(f"입장료 : {ent}원")




# score = int(input("점수 입력 : "))
# if score >= 90:
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# elif score >= 70:
#     print("C학점")
# elif score >= 60:
#     print("D학점")
# else:
#     print("F학점")


#4의배수는 맞고 100의배수는 아니지만 400의배수는 맞다

# year = int(input("연도 입력 : "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year}년은 윤년입니다.")
# else:
#     print(f"{year}년은 평년입니다.")


