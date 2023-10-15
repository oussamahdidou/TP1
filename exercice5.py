a = int(input("saisir un nombre"))
if a % 2 == 0:
    print("le nombre est paire")
elif a % 2 != 0 and a % 3 == 0:
    print("le nombre n`est pas pair mais divisible par 3")
else:
    print("le nombre n`est ni pair ni divisible par 3")
