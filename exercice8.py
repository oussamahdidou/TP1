M = 0
c = 0
for i in range(4):
    a = float(input("donner la note"))
    b = float(input("donner le coefficient"))
    M = M + a * b
    c = c + b
M = M / c
if M > 10:
    print(f"valider : {M}")
elif 7 < M < 10:
    print(f"rattrapage : {M}")
else:
    print(f"NV : {M}")
