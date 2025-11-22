a= int(input("enter the value :"))

if a % 5 == 0 and a % 3 ==0  :
    print("the entered number is divisable by 5 and 3")
elif a % 5 == 0:
    print("the entered number is divisable by 5")
elif a % 3 == 0 :
    print("the entered value is divisable by 3")
else :
    print("the entered value is not divisable by 5 and 3")
