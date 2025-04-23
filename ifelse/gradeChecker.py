# 🎓 Problem 3: Grade Checker
# Ask the user for a number between 0 and 100 and print the grade:


# Marks	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# < 60	F



a=int(input("enter the marks : "))

if a>=90 :
    print("you got an A grade")
elif a>80 and a<89 :
    print("you got B grade")
elif  a>70 and a<79 :
    print("you got C grade")
elif  a>60 and a<69 :
    print("you got D grade")
elif a < 60 :
    print("you got F grade")