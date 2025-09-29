numbers=[23,24,68,72,29,25,26,27,77,49,]
count = 0

for i in range(len(numbers)) :

    if ( numbers[i] % 2 == 1 ) :
        count = count + 1

print(count)