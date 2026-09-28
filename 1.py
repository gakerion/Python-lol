n = 10
a,b = 0,1
print(f"Result = {a}\nResult ={b}")
for i in range(2,n):
    result = a + b
    print(f"Result = {result}")
    a = b
    b = result
