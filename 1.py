num = int(input("lol"))
if (num > 0):
    print("Positive even" if (num % 2 == 0) else "Positive odd")
else:
    print("Negative and large" if (num < -100) else "Negative and small")