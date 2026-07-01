# calculator2.py
# result1 = 0
# result2 = 0

# def add1(num):  #계산기1
#     global result1
#     result1 += num
#     return result1

# def add2(num):  #계산기2
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

number = int(input("Enter a number to caculate its factorial: "))
factorial = 1


print(f"{number}! = ", end="")
for i in range(number, 0, -1):
    print(i, end="")
    if i != 1:
        print(" x ", end="")

for i in range(number, 0, -1):
    factorial *= i

    print(f"{factorial}")