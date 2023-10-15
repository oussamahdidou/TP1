poid = float(input("donner le poid"))
taille = float(input("donner le taille en maitre"))
imc = poid / pow(taille, 2)
if imc > 40:
    interpretation = "Obésité morbide ou massive"
elif 35 <= imc <= 40:
    interpretation = "Obésité sévère"
elif 30 <= imc < 35:
    interpretation = "Obésité modérée"
elif 25 <= imc < 30:
    interpretation = "Surpoids"
elif 18.5 <= imc < 25:
    interpretation = "Corpulence normale"
elif 16.5 <= imc < 18.5:
    interpretation = "Maigreur"
else:
    interpretation = "Famine"

# Afficher l'interprétation
print("Interprétation de l'IMC :", interpretation)
