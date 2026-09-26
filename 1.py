a = 153
temp = a
sum = 0
while a > 0:
    d = a % 10
    a = a//10
    sum += d**3
print("True" if sum == a else print("False"))