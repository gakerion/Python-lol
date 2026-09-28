n = 30
for i in range(1,n):
    prime = True
    for j in range (2, i-1):
        if (i % j == 0):
            prime = False
            break
    if prime == True:
        print(i)