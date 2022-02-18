upto = int(input("Find prime numbers upto : "))

count = 1
for num in range(2, upto + 1):
    i = 2
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;
    if(i != num):
        count = count + 1
print(count)
