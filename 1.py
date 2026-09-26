age = 20
membership = False
vip_level = 6
print("Valid" if (age > 18) and (age <= 65) and (membership == True) and (vip_level > 5) else (print("Invalid")))