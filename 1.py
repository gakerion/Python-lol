n = 10
a,b = 0,1
i = 0
while i < 10:
    result = a + b
    print(f"Result = {result}")
    a = b
    b = result
    i += 1