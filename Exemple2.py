m = "Mage"           
p = "Paladin"
a = "Assassin"
bfe = "Bâton de feu"
bf = "Bâton de foudre"
be ="Bâton d'eau"
e = "Épee longue"
eb = "épée courte et bouclier"
l = "Lance"
d = "Dagues"
p = "Poison"
cl = "Couteaux de lancer"
f = "facile"
mo = "moyen"
dif = "difficile"
d = "Donjon"
f = "Forêt"
lab = "Labyrinthe"
choix_valides_mage = ["bfe", "bf", "be"]
choix_valides_paladin = ["e", "eb", "l"]
choix_valides_assassin = ["d", "p", "cl"]
Personnage = [m, p, a]
Arme = [bfe, bf, e, l, d, p, cl]
Personnage = input(f"Choisissez votre personnage {Personnage[0]} (m), Paladin (p), Assasin (a)\n: ")
Sexe = input(f"Choisissez le sexe votre personnage : Homme (h) ou Femme (f)\n: ")

if Personnage == "m":
    weapon_choice = input("Choisissez votre arme : Bâton de feu (bfe), Bâton d'eau (be) ou Bâton de foudre (bf)\n: ")
    Personage_choisi = m
    if weapon_choice == "bfe":
        arme_choisi = bfe
    elif weapon_choice == "bf":
        arme_choisi = bf
    elif weapon_choice == "be":
        arme_choisi = be

if Personnage == "p":
    weapon_choice = input("Choisissez votre arme : Épee longue (e), épée court et bouclier (eb) ou Lance (l)\n: ")
    Personage_choisi = p
    if weapon_choice == "e":
        arme_choisi = e
    elif weapon_choice == "l":
        arme_choisi = l
    elif weapon_choice == "eb":
        arme_choisi = eb

if Personnage == "a":
    while True:
        weapon_choice = input("Choisissez votre arme : Dagues (d), couteaux de lancer (cl) ou Poison (p)\n: ")
        Personage_choisi = a  # Ce n'est pas nécessaire ici, mais si tu veux l'utiliser plus tard

        # Vérification du choix de l'arme
        if weapon_choice == "d":
            arme_choisi = d
            if weapon_choice in choix_valides_assassin:
                print(f"Vous avez choisi l'option {arme_choisi}.")
                break  # Sortir de la boucle si le choix est valide
        elif weapon_choice == "p":
            arme_choisi = p
            if weapon_choice in choix_valides_assassin:
                print(f"Vous avez choisi l'option {arme_choisi}.")
                break  # Sortir de la boucle si le choix est valide
        elif weapon_choice == "cl":
            arme_choisi = cl
            if weapon_choice in choix_valides_assassin:
                print(f"Vous avez choisi l'option {arme_choisi}.")
                break  # Sortir de la boucle si le choix est valide
        else:
            print("Choix invalide. Essayez à nouveau.") 


Difficulté = input(f"Choisissez la difficulté que vous désirez : facile (f), moyen (mo) ou difficile (dif)\n: ")

if Difficulté == "f":
    niveau_requis = d
    print("Donjon")
if Difficulté == "mo":
    niveau_requis = f
    print("Forêt")
if Difficulté == "dif":
    niveau_requis = lab
    print("Labyrinthe")