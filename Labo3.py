x = "Mage"
y = "Paladin"
z = "Assassin"
a = "Bâton de feu"
b = "Bâton de foudre"
Personnage = [x, y, z]
c = "Épee longue"
d = "Lance"
e = "Dagues"
f = "Poison"
g = "Donjon"
h = "Foret"
Personnage = input(f"Choisissez votre personnage {Personnage[0]} (x), {y} (y), {z} (z)\n:")
if Personnage == x:(a or b)

if Personnage == y:(c or d)

if Personnage == z:(e or f)

Arme = input("Choisissez votre arme ")
Niveau = input("Choisissez votre niveau")

"""Je pourrais modifier le code en faisant en sorte de pouvoir choisir les armes qui sont désignées à chaque personnage. 
Le mage aurait le choix entre le bâton de feu et le bâton de glace et le paladin aurait le choix entre l'épée longue et la lance.
L'assassin aurait le choix entre les dagues et le poison. De cette façon les autres personnages n'auraient pas accès aux armes des 
autres personnages.Je pourrait renommé les variables pour leurs données un nom plus unique à chacune d'elle. Je pourrais faire comme 
avec le choix de personnage et désigné la touche entre parenthèses que l'utilisateiur doit faire pour faire son choix."""