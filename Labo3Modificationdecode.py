m = "Mage"           
p = "Paladin"
a = "Assassin"
bfe = "Bâton de feu"
bf = "Bâton de foudre"
e = "Épee longue"
l = "Lance"
d = "Dagues"
p = "Poison"
d = "Donjon"
f = "Forêt"
Personnage = [m, p, a]
Arme = [bfe, bf, e, l, d, p]
Personnage = input(f"Choisissez votre personnage {Personnage[0]} (m), Paladin (p), Assasin (a)\n: ")

if Personnage == "m":
    weapon_choice = input("Choissisez votre arme : Bâton de feu (bfe)  ou Bâton de foudre (bf)\n: ")
    Personage_choisi = m
    if weapon_choice == "bfe":
        arme_choisi = bfe
    elif weapon_choice == "bf":
        arme_choisi = bf

if Personnage == "p":
    weapon_choice = input("Choissisez votre arme : Épee longue (e) ou Lance (l)\n: ")
    Personage_choisi = p
    if weapon_choice == "e":
        arme_choisi = e
    elif weapon_choice == "l":
        arme_choisi = l
if Personnage == "a":
    weapon_choice = input("Choissisez votre arme : Dagues (d) ou Poison (p)\n: ")
    Personage_choisi = a
    if weapon_choice == "d":
        arme_choisi = d
    elif weapon_choice == "p":
        arme_choisi = p

Niveau = input("Choisissez votre niveau entre Donjon (d) et Forêt (f)\n: ")
