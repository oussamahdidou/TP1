distance = float(input("saisir la distance"))
temps = float(input("saisir le temps en minute"))
if temps == 0:
    temps = 1
print(f"la vitesse en m\s est : {distance/((temps/60)*3.6)}")
