a = int(input("donner le temp en secondes"))
heure = int(a / 3600)
a = a - heure * 3600
minute = int(a / 60)
seconde = a - minute * 60
print(f"le temps est {heure} heure {minute} minute {seconde} seconde ")
