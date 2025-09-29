numbers = [2, 3, 4, 5, 6, 7, 8, 9, 23, 45, 67, 89]
for num in numbers:
    if num < 2:
        print(f"{num} is not prime")
        continue
    is_prime = True
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

