mage = "Mage"
paladin = "Paladin"
assassin = "Assassin"
batonfeu = "Bâton de feu"
batonfoudre = "Bâton de foudre"
batoneau = "Bâton d'eau"
epeelongue = "Épée longue"
epeebouclier = "Épée courte et bouclier"
lance = "Lance"
dagues = "Dagues"
poison = "Poison"
couteaulance = "Couteaux de lancer"
facile = "Facile"
moyen = "Moyen"
difficile = "Difficile"
donjon = "Donjon"
foret = "Forêt"
labyrinthe = "Labyrinthe"
homme = "Homme"
femme = "Femme"

# Choix valides pour chaque catégorie
choix_valides_mage = ["Bâton de feu", "Bâton de foudre", "Bâton d'eau"]
choix_valides_paladin = ["Épée longue", "Épée courte et bouclier", "Lance"]
choix_valides_assassin = ["Dagues", "Poison", "Couteaux de lancer"]
choix_valides_difficulte = ["Facile", "Moyen", "Difficile"]

# Demande du personnage 
Personnage = input(f"Choisissez votre personnage : {mage}, {paladin}, {assassin}\n: ")
while Personnage not in [mage, paladin, assassin]:
    print("Choix invalide. Essayez à nouveau.")
    Personnage = input(f"Choisissez votre personnage : {mage}, {paladin}, {assassin}\n: ")
# Demande du sexe
Sexe = input(f"Choisissez le sexe de votre personnage : {homme} ou {femme}\n: ")
while Sexe not in [homme, femme]:
    print("Choix de sexe invalide. Essayez à nouveau.")
    Sexe = input(f"Choisissez le sexe de votre personnage : {homme} ou {femme}\n: ")

# Choix de l'arme
if Personnage == mage:
    weapon_choice = input("Choisissez votre arme : Bâton de feu, Bâton d'eau ou Bâton de foudre\n: ")
    while weapon_choice not in choix_valides_mage:
        print("Choix invalide. Essayez à nouveau.")
        weapon_choice = input("Choisissez votre arme : Bâton de feu, Bâton d'eau ou Bâton de foudre\n: ")
    arme_choisi = weapon_choice

elif Personnage == paladin:
    weapon_choice = input("Choisissez votre arme : Épée longue, Épée courte et bouclier ou Lance\n: ")
    while weapon_choice not in choix_valides_paladin:
        print("Choix invalide. Essayez à nouveau.")
        weapon_choice = input("Choisissez votre arme : Épée longue, Épée courte et bouclier ou Lance\n: ")
    arme_choisi = weapon_choice

elif Personnage == assassin:
    weapon_choice = input("Choisissez votre arme : Dagues, Couteaux de lancer ou Poison\n: ")
    while weapon_choice not in choix_valides_assassin:
        print("Choix invalide. Essayez à nouveau.")
        weapon_choice = input("Choisissez votre arme : Dagues, Couteaux de lancer ou Poison\n: ")
    arme_choisi = weapon_choice

# Choix de la difficulté 
Difficulté = input(f"Choisissez la difficulté que vous désirez : {facile}, {moyen}, {difficile}\n: ")
while Difficulté not in choix_valides_difficulte:
    print("Choix de difficulté invalide. Essayez à nouveau.")
    Difficulté = input(f"Choisissez la difficulté que vous désirez : {facile}, {moyen}, {difficile}\n: ")

# Attribution du niveau en fonction de la difficulté choisi
if Difficulté == facile:
    niveau_requis = donjon
elif Difficulté == moyen:
    niveau_requis = foret
elif Difficulté == difficile:
    niveau_requis = labyrinthe

# Affichage du récapitulatif du personnage
print("\nRÉCAPITULATIF DU PERSONNAGE :")
print(f"Personnage choisi : {Personnage}")
print(f"Sexe choisi : {Sexe}")
print(f"Arme choisie : {arme_choisi}")
print(f"Difficulté choisie : {Difficulté} - Niveau : {niveau_requis}")