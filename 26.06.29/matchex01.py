score = int(input("Enter your grade: "))
match score:
    case score if score >= 90:
        print("Excellent!")
    case score if score >= 80:
        print("Good job!")
    case score if score >= 70:
        print("You can do better.")
    case score if score >= 60:
        print("You need to work harder.") 
    case _:
        print("Invalid grade.")

score = int(input("Enter your grade: "))
oneDigit = score // 10
match oneDigit:
    case 10 | 9:
        print("Excellent!")
    case 8:
        print("Good job!")
    case 7:
        print("You can do better.")
    case 6:
        print("You need to work harder.")
    case _:
        print("Invalid grade.")