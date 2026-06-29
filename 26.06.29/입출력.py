# print("=== 간단한 계산기 ===")

# num1 = float(input(" 첫 번째 숫자를 입력하세요:"))
# num2 = float(input(" 두 번째 숫자를 입력하세요:"))

# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")

# if num2 != 0:
#     print(f"{num1} / {num2} = {num1 / num2}")
# else:
#     print("0으로 나눌 수 없습니다")

# newfile.py
# f = open("새파일.txt", 'w')
# f.close()


# # newfile2.py
# f = open("C:/doit/새파일.txt", 'w')
# f.close()


# write_data.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()
