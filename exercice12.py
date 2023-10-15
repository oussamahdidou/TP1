grade = input("Entrez le grade de l'employé (A, B, C, D ou E) : ")

heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))

tarif_horaire = 0
prime = 0

if grade == "A":
    tarif_horaire = 200
    prime = 1000 * (heures_travaillees // 20)
elif grade == "B":
    tarif_horaire = 150
    prime = 800 * (heures_travaillees // 20)
elif grade == "C":
    tarif_horaire = 120
    prime = 500 * (heures_travaillees // 15)
elif grade == "D":
    tarif_horaire = 100
    prime = 350 * (heures_travaillees // 15)
elif grade == "E":
    tarif_horaire = 80
    prime = 100 * (heures_travaillees // 10)
else:
    print("Grade invalide")
    exit()

salaire = (tarif_horaire * heures_travaillees) + prime


print("Le salaire de l'employé est : {} dh".format(salaire))
