# 90-100  -> A
#  80-90  -> B
#  70-80  -> C
#  60-70 -> D
#  50-60 -> E
#  <50  -> fail

grade=int(input("enter your grade :  "))

if grade >= 90 :
    print("your grade is a")

elif grade>80 :
    print ("your grade is b")

elif grade >70 :
    print("your grade is c")

elif grade >60 :
    print("your grade is d")   

elif grade >50:
    print("your grade is e")
    
else:
    print("you are a failure")
