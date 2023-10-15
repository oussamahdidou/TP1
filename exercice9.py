totalttc = 0
for i in range(2):
    nom_produit = input(f"le nom du produit {i+1} : ")
    prix_unitaire = float(input("prix unitaire : "))
    quantite = int(input("quantite de produit"))
    print(f"le prix ht de produit {nom_produit} est : {quantite*prix_unitaire}")
    totalttc += (quantite * prix_unitaire) * 1.2
print(f"total ttc : {totalttc}")
