p = True
q = False
r = True

if p and q and r:
    print("All true")
elif (p and q) or (q and r) or (p and r):
    print("Any two true")
elif p or q or r:
    print("Any one true")
else:
    print("None true")
