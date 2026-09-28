i = 1
list = []
pos_count = 0
neg_count = 0
while i > 0:
    In = int(input("Enter Number"))
    if In == 999:
        break
    if In >= 0:
        pos_count += 1
    elif In < 0:
        neg_count += 1
    list.append(In)
print(f"{pos_count} positive numbers were entered and {neg_count} negative numbers were entered")