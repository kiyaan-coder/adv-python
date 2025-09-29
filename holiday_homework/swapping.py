#using extra variables
a = 5
b = 10
print("Before swapping : a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping : a =", a, ", b =", b)
 
 #python way
x = 15
y = 20
print("\nBefore swapping : x =", x, ", y =", y)
x, y = y, x
print("After swapping : x =", x, ", y =", y)

#no extra variables
m = 25
n = 30
print("\nBefore swapping : m =", m, ", n =", n)
m = m + n
n = m - n
m = m - n
print("After swapping : m =", m, ", n =", n)

 