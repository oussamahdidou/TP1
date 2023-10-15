a = float(input("donner a : "))
b = float(input("donner b : "))
c = str(input("donner une operation : "))
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("b=0 impossible division")
else:
    print("operation inconnue")
