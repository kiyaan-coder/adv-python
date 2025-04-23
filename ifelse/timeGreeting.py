# 🕒 Problem 4: Time Greeting
# Ask the user for the current hour (0–23) and print a greeting:

# 0–11: Good morning

# 12–17: Good afternoon

# 18–23: Good evening

# Anything else: Invalid input




a=int(input("enter the current hour :  "))

if a > 0 and a < 12 :
    print("Good morining")
elif a > 12 and a <= 17 :
     print("good afternoon")
else : 
    print("good evning")