
while 1 > 0:
    choice = input("Enter your choice")
    if choice == "exit":
        print("Exiting")
        break
    a = int(input("num1"))
    b = int(input("num2"))
    if choice == "add":
        print(a+b)
    if choice == "subtract":
        print(a-b)
    if choice == "multiply":
        print(a*b)
    if choice == "divide":
        print(a/b)
        