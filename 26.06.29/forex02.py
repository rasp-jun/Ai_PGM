# number = int(input("Enter a number: "))
# for i in range(1, number+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# number = int(input("Enter a number"))
# for  i  in range(1, number+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

    
# 우측정렬
# number = int(input("Enter a number"))
# for  i  in range(1, number+1):
#     for j in range(number - i):
#         print(" ", end="")
#     for j in range(i):
#          print("*", end="")
#     print()



# 중앙 정렬 1357
# number = int(input("Enter a number"))
# for  i  in range(1, number+1):
#     if i % 2 != 0:
#         for j in range((number - i) // 2):
#             print(" ", end="")
#         for j in range(i):
#             print("*", end="")
#         print()

# 중앙 정렬 1357531
# number = int(input("Enter a number"))
# for  i  in range(1, number + 1, 2):
#     for j in range((number - i) // 2):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
# for  i  in range(number - 2, 0, -2):
#     for j in range((number - i) // 2):
#         print(" ", end="")
#     for j in range(i):    
#         print("*", end="")
#     print()
