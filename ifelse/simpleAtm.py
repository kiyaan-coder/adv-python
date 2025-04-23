# 💰 Problem 5: Simple ATM Simulator
# Ask the user their balance and how much they want to withdraw.

# If withdrawal is less than or equal to balance, show the new balance.

# If not, print “Insufficient funds”.


balance = int(input("enter the blance : "))
withdraw = int(input("enter the ammount you want to withdraw :  "))

if balance >= withdraw :
    print("this is the blance left :  ",balance - withdraw)
else :
    print("Insufficient funds")