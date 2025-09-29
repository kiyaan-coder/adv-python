numbers = [123,32,22,3,1,2,123,123]
sum = 0
for i in range(len(numbers)) :

    if (numbers[i]%2 == 0) :
        sum = sum + numbers[i]
print(sum)