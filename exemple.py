choix_valides = ["1", "2", "3"]

while True:
    # Afficher les choix
    print("Veuillez choisir une option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

    # Demander à l'utilisateur de faire un choix
    choix = input("Entrez votre choix: ")

    # Vérifier si le choix est valide
    if choix in choix_valides:
        print(f"Vous avez choisi l'option {choix}.")
        break  # Sortir de la boucle si le choix est valide
    else:
        print("Choix invalide. Essayez à nouveau.")  # Si le choix est invalide, recommencer
