prix_total = float(input("Quel est le prix total ? $"))
pourcentage_pourboire = float(input("Combien de pourcentage de pourboire voulez vous donner ? 10 , 12 , 15 : "))
nombre = float(input("Combien de personnes partagent le repas ? "))

print("Voici le prix par personne $" + str((prix_total + (pourcentage_pourboire * prix_total))/nombre))



