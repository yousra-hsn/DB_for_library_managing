from datetime import date, timedelta
import matplotlib.pyplot as plt
# fonctions de service

def accueil():
    print("\n\n\nBienvenue au service de gestion de la bibliothèque NF18\n")
    print("Veuillez vous connecter en tant que membre ou adhérent\n")
    print("(0) Quitter\n(1) Membre\n(2) Adhérent\n")
    choixAccueil = int(input("Choisissez 0, 1 ou 2: "))
    while choixAccueil < 0 or choixAccueil > 2:
        choixAccueil = int(input("Saisie invalide, choisissez 0, 1 ou 2: "))
    if choixAccueil == 0:
        print("Vous avez choisi de quitter\n")
    return choixAccueil

def authentificationMembre(connexion):
    connecte = False
    print("\n********** Authentification Membre **********\n")
    login = input("Login: ")
    motDePasse = input("Mot de passe: ")
    cur = connexion.cursor()
    cur.execute("SELECT login, motDePasse FROM Membre WHERE login=%s AND motDePasse=%s", (login, motDePasse))
    resultat = cur.fetchall()
    while len(resultat) == 0:
        print("Login ou mot de passe incorrect, voulez-vous réessayer?\n(1) Réessayer\n(2) Quitter\n ")
        choix = int(input("Choisissez 1 ou 2: "))
        if choix == 2:
            return connecte
        else:
            login = input("Login: ")
            motDePasse = input("Mot de passe: ")
            cur.execute("SELECT login, motDePasse FROM Membre WHERE login=%s AND motDePasse=%s", (login, motDePasse))
            resultat = cur.fetchall()
    print("******* Authentification réussie *******\n")
    connecte = True
    return connecte

def authentificationAdherent(connexion):
    connecte = False
    print("\n********** Authentification Adhérent **********\n")
    login = input("Login: ")
    motDePasse = input("Mot de passe: ")
    cur = connexion.cursor()
    cur.execute("SELECT login, motDePasse, blacklist FROM Adherent WHERE login=%s AND motDePasse=%s", (login, motDePasse))
    resultat = cur.fetchall()
    while len(resultat) == 0:
        print("Login ou mot de passe incorrect, voulez-vous réessayer?\n(1) Réessayer\n(2) Quitter\n ")
        choix = int(input("Choisissez 1 ou 2: "))
        if choix == 2:
            return connecte
        else:
            login = input("Login: ")
            motDePasse = input("Mot de passe: ")
            cur.execute("SELECT login, motDePasse, blacklist FROM Adherent WHERE login=%s AND motDePasse=%s", (login, motDePasse))
            resultat = cur.fetchall()
    blacklist = resultat[0][2]
    if blacklist == True:
        print("Vous êtes blacklistés de la bibliothèque, vous ne pouvez pas y accéder\n")
    else:
        print("******* Authentification réussie *******\n")
        connecte = True
    return connecte

def menuMembre(connexion):
    choixAction = -1
    while choixAction != 0:
        print("\n********** Menu **********\n")
        print("Choisissez une action:\n(0) Déconnexion\n(1) Gestion des membres\n(2) Gestion des adherents\n(3) Gestion des ressources\n")
        print("(4) Gestion des exemplaires\n(5) Gestion des emprunts\n(6) Gestion des sanctions\n(7) Statistiques")
        choixAction = int(input("Choisissez entre 0 et 7: "))
        while choixAction < 0 and choixAction > 7:
            choixAction = int(input("Saisie invalide, choisissez entre 0 et 7: "))
        match choixAction:
            case 0:
                print("Vous avez choisi de vous déconnecter\n")
            case 1:
                choixGestion = -1
                while choixGestion != 0:
                    print("Choisissez une action:\n(0) Retour\n(1) Ajouter un membre\n(2) Afficher les membres\n(3) Modifier un membre")
                    choixGestion = int(input("Choisissez entre 0 et 3: "))
                    while choixGestion < 0 and choixGestion > 3:
                        choixGestion = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixGestion:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            ajouterMembre(connexion)
                        case 2:
                            afficherMembres(connexion)
                        case 3:
                            modifierMembre(connexion)
            case 2:
                choixGestion = -1
                while choixGestion != 0:
                    print("Choisissez une action:\n(0) Retour\n(1) Ajouter un adhérent\n(2) Afficher les adhérents\n(3) Modifier un adhérent")
                    choixGestion = int(input("Choisissez entre 0 et 3: "))
                    while choixGestion < 0 and choixGestion > 3:
                        choixGestion = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixGestion:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            ajouterAdherent(connexion)
                        case 2:
                            afficherAdherents(connexion)
                        case 3:
                            modifierAdherent(connexion)
            case 3:
                choixGestion = -1
                while choixGestion != 0:
                    print("Choisissez une action:\n(0) Retour\n(1) Ajouter une ressource\n(2) Afficher les ressources\n(3) Modifier une ressource")
                    choixGestion = int(input("Choisissez entre 0 et 3: "))
                    while choixGestion < 0 and choixGestion > 3:
                        choixGestion = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixGestion:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            ajouterRessource(connexion)
                        case 2:
                            print("Options d'affichage:\n(1) Toutes les ressources\n")
                            print("(2) Tous les livres\n(3) Toutes les oeuvres musicales\n(4) Tous les films")
                            choixAffichage = int(input("Choisissez entre 1 et 4:"))
                            while choixAffichage < 1 and choixAffichage > 4:
                                choixAffichage = int(input("Choisissez entre 1 et 4:"))
                            match choixAffichage:
                                case 1:
                                    afficherRessources(connexion)
                                case 2:
                                    afficherLivres(connexion)
                                case 3:
                                    afficherOeuvresMusicales(connexion)
                                case 4:
                                    afficherFilms(connexion)
                        case 3:
                            modifierRessource(connexion)
            case 4:
                choixGestion = -1
                while choixGestion != 0:
                    print(
                        "Choisissez une action:\n(0) Retour\n(1) Ajouter un exemplaire\n(2) Afficher les exemplaires d'une ressource\n(3) Modifier un exemplaire")
                    choixGestion = int(input("Choisissez entre 0 et 3: "))
                    while choixGestion < 0 and choixGestion > 3:
                        choixGestion = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixGestion:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            ajouterExemplaire(connexion)
                        case 2:
                            afficherExemplaires(connexion)
                        case 3:
                            modifierExemplaire(connexion)
            case 5:
                choixGestion = -1
                while choixGestion != 0:
                    print(
                        "Choisissez une action:\n(0) Retour\n(1) Ajouter un prêt\n(2) Afficher les prêts\n(3) Retourner un prêt")
                    choixGestion = int(input("Choisissez entre 0 et 3: "))
                    while choixGestion < 0 and choixGestion > 3:
                        choixGestion = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixGestion:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            ajouterPret(connexion)
                        case 2:
                            afficherPrets(connexion)
                        case 3:
                            retournerPret(connexion)
            case 6:
                choixGestion = -1
                while choixGestion != 0:
                    print(
                        "Choisissez une action:\n(0) Retour\n(1) Afficher les sanctions\n(2) Modifier une sanction")
                    choixGestion = int(input("Choisissez entre 0 et 3: "))
                    while choixGestion < 0 and choixGestion > 3:
                        choixGestion = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixGestion:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            afficherSanctions(connexion)
                        case 2:
                            modifierSanction(connexion)
            case 7:
                choixStat = -1
                while choixStat != 0:
                    print("Choisissez une catégorie:\n(0) Retour\n(1) Livres\n(2) Oeuvres musicales\n(3) Films")
                    choixStat = int(input("Choisissez entre 0 et 3: "))
                    while choixStat < 0 and choixStat > 3:
                        choixStat = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixStat:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            statLivre(connexion)
                        case 2:
                            statOeuvre(connexion)
                        case 3:
                            statFilm(connexion)

#Ajouter un membre dans la base de données
def ajouterMembre(connexion):
    print("Veuillez saisir les informations ci-dessous: ")
    login = input("Login: ")
    motDePasse = input("Mot de passe: ")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    adresse = input("Adresse: ")
    email = input("Email: ")
    cur = connexion.cursor()
    cur.execute("SELECT login FROM Membre WHERE login=%s", (login,))
    conditionCheck = cur.fetchall()
    if len(conditionCheck) != 0:
        print("Le membre existe déjà")
    else:
        cur.execute("INSERT INTO Membre VALUES (%s, %s, %s, %s, %s, %s)",
                    (login, motDePasse, nom, prenom, adresse, email))
        connexion.commit()
    print("Voulez-vous ajouter un autre membre?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterMembre(connexion)

#Afficher les membres de la bibliothèque
def afficherMembres(connexion):
    cur = connexion.cursor()
    cur.execute("SELECT nom, prenom, adresse, email FROM Membre")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("**************")
            print("Nom: ", i[0])
            print("Prénom: ", i[1])
            print("Adresse: ", i[2])
            print("Email: ", i[3], "\n")
    else:
        print("Aucun membre enregistré")

# Modifier les informations d'un membre
def modifierMembre(connexion):
    cur = connexion.cursor()
    login = input("Veuillez saisir le login du membre à modifier: ")
    cur.execute("SELECT login FROM Membre WHERE login = %s", (login,))
    conditionCheck = cur.fetchall()
    if len(conditionCheck) == 0:
        print("Le membre n'existe pas")
    else:
        print("Veuillez saisir les informations mises à jour: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        adresse = input("Adresse: ")
        email = input("Email: ")
        cur.execute("UPDATE Membre SET nom=%s, prenom=%s, adresse=%s, email=%s WHERE login=%s",
                    (nom, prenom, adresse, email, login))
        connexion.commit()

# Ajouter un adhérent dans la base de données
def ajouterAdherent(connexion):
    print("Veuillez saisir les informations ci-dessous: ")
    login = input("Login: ")
    motDePasse = input("Mot de passe: ")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    adresse = input("Adresse: ")
    email = input("Email: ")
    dateNaissance = date(input("Date de naissance : "))
    telephone = int(input("Numero de telephone : "))
    cur = connexion.cursor()
    cur.execute("SELECT login FROM Adherent WHERE login=%s", (login,))
    conditionCheck = cur.fetchall()
    if len(conditionCheck) != 0:
        print("L'adhérent existe déjà")
    else:
        cur.execute("INSERT INTO Adherent VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (login, motDePasse, nom, prenom, adresse, email, dateNaissance, telephone, True, False, True))
        connexion.commit()
    print("Voulez-vous ajouter un autre adhérent?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterAdherent(connexion)

# Afficher les informations sur les adhérents
def afficherAdherents(connexion):
    cur = connexion.cursor()
    cur.execute("SELECT nom, prenom, adresse, email, dateNaissance, telephone, adhesion, blacklist, droitPret FROM Adherent")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("**************")
            print("Nom: ", i[0])
            print("Prénom: ", i[1])
            print("Adresse: ", i[2])
            print("Email: ", i[3])
            print("Date de naissance: ", i[4])
            print("Numéro de telephone: ", str(i[5]))
            print("Est adhérent: ", i[6])
            print("Est blacklisté: ", i[7])
            print("A le droit d'emprunt: ", i[8], "\n")
    else:
        print("Aucun adhérent enregistré")

# Modifier les informations sur un adhérent
def modifierAdherent(connexion):
    cur = connexion.cursor()
    login = input("Veuillez saisir le login de l'adhérent à modifier: ")
    cur.execute("SELECT login FROM Adherent WHERE login = %s", (login,))
    conditionCheck = cur.fetchall()
    if len(conditionCheck) == 0:
        print("L'adhérent n'existe pas")
    else:
        choixModif = -1
        while choixModif != 0:
            print("Choisissez une option:\n(0) Retour")
            print("(1) Modifier les coordonnées\n(2) Modifier les statuts")
            choixModif = int(input("Choisissez entre 0 et 2: "))
            while choixModif < 0 and choixModif > 2:
                choixModif = int(input("Choisissez entre 0 et 2: "))
            if choixModif == 0:
                print("Vous avez choisi de quitter")
            elif choixModif == 1:
                print("Veuillez saisir les informations mises à jour: ")
                nom = input("Nom: ")
                prenom = input("Prénom: ")
                adresse = input("Adresse: ")
                email = input("Email: ")
                annee = int(input("Annee de naissance: "))
                mois = int(input("Mois de naissance: "))
                jour = int(input("Jour de naissance: "))
                dateN = date(annee,mois,jour)
                dateNaissance = dateN.strftime('%Y-%m-%d')
                telephone = int(input("Numéro de téléphone: "))

                cur.execute("UPDATE Adherent SET nom=%s, prenom=%s, adresse=%s, email=%s, dateNaissance=%s, telephone=%s WHERE login=%s",
                            (nom, prenom, adresse, email, dateNaissance, telephone, login))
                connexion.commit()
            else:
                adhesion = input("Est adhérent (True/False): ")
                blacklist = input("Est blacklisté (True/False): ")
                droitPret = input("A le droit d'emprunt (True/False): ")
                cur.execute(
                    "UPDATE Adherent SET adhesion=%s, blacklist=%s, droitPret=%s WHERE login=%s",
                    (adhesion, blacklist, droitPret, login))
                connexion.commit()
    print("Voulez-vous modifier un autre adhérent?")
    choixModif = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierAdherent(connexion)


def ajouterRessource(connexion):
    print("Type de ressource à ajouter?\n(1) Livre\n(2) Oeuvre musicale\n(3) Film\n(0) Quitter\n")
    choixType = int(input("Choisissez entre 0 et 3: "))
    while choixType < 0 and choixType > 3:
        choixType = int(input("Saisie invalide, choisissez entre 0 et 3: "))
    match choixType:
        case 1:
            ajouterLivre(connexion)
        case 2:
            ajouterOeuvreMusicale(connexion)
        case 3:
            ajouterFilm(connexion)
        case 0:
            print("Vous avez choisi de quitter")
            return
    choixAjout = int(input("Ajouter une autre ressource?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterRessource(connexion)

def ajouterLivre(connexion):
    cur = connexion.cursor()
    codeLivre = input("Code du livre: ")
    cur.execute("SELECT code FROM Livre WHERE code=%s", (codeLivre,))
    if len(cur.fetchall()) != 0:
        print("Le livre existe déjà")
    else:
        print("Veuillez saisir les informations ci-dessous: ")
        titre = input("Titre: ")
        dateApparition = input("Date d'apparition (AAAA-MM-JJ): ")
        editeur = input("Éditeur: ")
        genre = input("Genre: ")
        codeClassification = input("Code de classification: ")
        isbn = input("ISBN: ")
        resume = input("Résumé: ")
        langue = input("Langue: ")
        cur.execute("INSERT INTO Ressource VALUES (%s, %s, %s, %s, %s, %s)", (codeLivre, titre, dateApparition, editeur, genre, codeClassification))
        cur.execute("INSERT INTO Livre VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (codeLivre, titre, dateApparition, editeur, genre, codeClassification, isbn, resume, langue))
        connexion.commit()
    print("Voulez-vous ajouter un autre livre?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterLivre(connexion)

def ajouterOeuvreMusicale(connexion):
    cur = connexion.cursor()
    codeMusique = input("Code de l'oeuvre: ")
    cur.execute("SELECT code FROM OeuvreMusicale WHERE code=%s", (codeMusique,))
    if len(cur.fetchall()) != 0:
        print("L'oeuvre existe déjà")
    else:
        print("Veuillez saisir les informations ci-dessous: ")
        titre = input("Titre: ")
        dateApparition = input("Date d'apparition (AAAA-MM-JJ): ")
        editeur = input("Éditeur: ")
        genre = input("Genre: ")
        codeClassification = input("Code de classification: ")
        longueur = int(input("Durée en minutes: "))
        cur = connexion.cursor()
        cur.execute("INSERT INTO Ressource VALUES (%s, %s, %s, %s, %s, %s)",
                    (codeMusique, titre, dateApparition, editeur, genre, codeClassification))
        cur.execute("INSERT INTO OeuvreMusicale VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (codeMusique, titre, dateApparition, editeur, genre, codeClassification, longueur))
        connexion.commit()
    print("Voulez-vous ajouter une autre oeuvre musicale?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterOeuvreMusicale(connexion)

def ajouterFilm(connexion):
    cur = connexion.cursor()
    codeFilm = input("Code du film: ")
    cur.execute("SELECT code FROM Film WHERE code=%s", (codeFilm,))
    if len(cur.fetchall()) != 0:
        print("Le film existe déjà")
    else:
        print("Veuillez saisir les informations ci-dessous: ")
        titre = input("Titre: ")
        dateApparition = input("Date d'apparition (AAAA-MM-JJ): ")
        editeur = input("Éditeur: ")
        genre = input("Genre: ")
        codeClassification = input("Code de classification: ")
        langue = input("Langue: ")
        duree = int(input("Durée en minutes: "))
        synopsis = input("Synopsis: ")
        cur = connexion.cursor()
        cur.execute("INSERT INTO Ressource VALUES (%s, %s, %s, %s, %s, %s)",
                    (codeFilm, titre, dateApparition, editeur, genre, codeClassification))
        cur.execute("INSERT INTO Film VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (codeFilm, titre, dateApparition, editeur, genre, codeClassification, langue, duree, synopsis))
        connexion.commit()
    print("Voulez-vous ajouter un autre film?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterFilm(connexion)

#Afficher toutes les ressources de la bibliothèque
def afficherRessources(connexion):
    cur = connexion.cursor()
    cur.execute("SELECT * FROM Ressource")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("******* Code: ", i[0], " *******")
            print("Titre: ", i[1])
            print("Date d'apparition: ", i[2])
            print("Éditeur: ", i[3])
            print("Genre: ", i[4])
            print("Code de classification: ", i[5], "\n")
    else:
        print("Aucune ressource disponible")

# Modifier les informations d'une ressource
def modifierRessource(connexion):
    print("Type de ressource à modifier?\n(1) Livre\n(2) Oeuvre musicale\n(3) Film\n(0) Quitter\n")
    choixType = int(input("Choisissez entre 0 et 3: "))
    while choixType < 0 and choixType > 3:
        choixType = int(input("Saisie invalide, choisissez entre 0 et 3: "))
    match choixType:
        case 1:
            modifierLivre(connexion)
        case 2:
            modifierOeuvreMusicale(connexion)
        case 3:
            modifierFilm(connexion)
        case 0:
            print("Vous avez choisi de quitter")
            return
    choixModif = int(input("Modifier une autre ressource?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierRessource(connexion)

def modifierLivre(connexion):
    codeModif = input("Saisir le code du livre à modifier: ")
    cur = connexion.cursor()
    cur.execute("SELECT code FROM Livre WHERE code = %s", (codeModif,))
    row = cur.fetchone()
    if len(row) == 0:
        print("\nCe livre n'existe pas. ")
    else:
        print("Choisir un champ à modifier:\n(1) titre\n(2) date d'apparition\n(3) Éditeur\n(4) Genre\n(5) Code de classification\n(6) ISBN\n(7) Résumé\n(8) Langue\n(0) Annuler")
        choixChamp = int(input("Choisir entre 0 et 8: "))
        while choixChamp < 0 and choixChamp > 8:
            choixChamp = int(input("Saisie invalide, choisir entre 0 et 8: "))
        match choixChamp:
            case 1:
                nouveauTitre = input("Nouveau titre: ")
                cur.execute("UPDATE Ressource SET titre = %s WHERE code = %s", (nouveauTitre, codeModif))
                cur.execute("UPDATE Livre SET titre = %s WHERE code = %s", (nouveauTitre, codeModif))
            case 2:
                nouvelleDate = input("Nouvelle date d'apparition: ")
                cur.execute("UPDATE Ressource SET dateApparition = %s WHERE code = %s", (nouvelleDate, codeModif))
                cur.execute("UPDATE Livre SET dateApparition = %s WHERE code = %s", (nouvelleDate, codeModif))
            case 3:
                nouveauEditeur = input("Nouvel éditeur: ")
                cur.execute("UPDATE Ressource SET editeur = %s WHERE code = %s", (nouveauEditeur, codeModif))
                cur.execute("UPDATE Livre SET editeur = %s WHERE code = %s", (nouveauEditeur, codeModif))
            case 4:
                nouveauGenre = input("Nouveau genre: ")
                cur.execute("UPDATE Ressource SET genre = %s WHERE code = %s", (nouveauGenre, codeModif))
                cur.execute("UPDATE Livre SET genre = %s WHERE code = %s", (nouveauGenre, codeModif))
            case 5:
                nouveauCode = input("Nouveau code de classification: ")
                cur.execute("UPDATE Ressource SET codeClassification = %s WHERE code = %s", (nouveauCode, codeModif))
                cur.execute("UPDATE Livre SET codeClassification = %s WHERE code = %s", (nouveauCode, codeModif))
            case 6:
                isbn = input("Nouveau ISBN: ")
                cur.execute("UPDATE Livre SET isbn = %s WHERE code = %s", (isbn, codeModif))
            case 7:
                nouveauResume = input("Nouveau résumé: ")
                cur.execute("UPDATE Livre SET resume = %s WHERE code = %s", (nouveauResume, codeModif))
            case 8:
                nouvelleLangue = input("Nouvelle langue: ")
                cur.execute("UPDATE Livre SET langue = %s WHERE code = %s", (nouvelleLangue, codeModif))
            case 0:
                return
        connexion.commit()
    choixModif = int(input("Modifier un autre livre?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierLivre(connexion)

def modifierOeuvreMusicale(connexion):
    codeModif = input("Saisir le code de l'oeuvre à modifier: ")
    cur = connexion.cursor()
    cur.execute("SELECT code FROM OeuvreMusicale WHERE code = %s", (codeModif,))
    row = cur.fetchone()
    if len(row) == 0:
        print("\nCette oeuvre n'existe pas. ")
    else:
        print("Choisir un champ à modifier:\n(1) titre\n(2) date d'apparition\n(3) Éditeur\n(4) Genre\n(5) Code de classification\n(6) Longueur\n(0) Annuler")
        choixChamp = int(input("Choisir entre 0 et 6: "))
        while choixChamp < 0 and choixChamp > 8:
            choixChamp = int(input("Saisie invalide, choisir entre 0 et 6: "))
        match choixChamp:
            case 1:
                nouveauTitre = input("Nouveau titre: ")
                cur.execute("UPDATE Ressource SET titre = %s WHERE code = %s", (nouveauTitre, codeModif))
                cur.execute("UPDATE Oeuvre SET titre = %s WHERE code = %s", (nouveauTitre, codeModif))
            case 2:
                nouvelleDate = input("Nouvelle date d'apparition: ")
                cur.execute("UPDATE Ressource SET dateApparition = %s WHERE code = %s", (nouvelleDate, codeModif))
                cur.execute("UPDATE Oeuvre SET dateApparition = %s WHERE code = %s", (nouvelleDate, codeModif))
            case 3:
                nouveauEditeur = input("Nouvel éditeur: ")
                cur.execute("UPDATE Ressource SET editeur = %s WHERE code = %s", (nouveauEditeur, codeModif))
                cur.execute("UPDATE Oeuvre SET editeur = %s WHERE code = %s", (nouveauEditeur, codeModif))
            case 4:
                nouveauGenre = input("Nouveau genre: ")
                cur.execute("UPDATE Ressource SET genre = %s WHERE code = %s", (nouveauGenre, codeModif))
                cur.execute("UPDATE Oeuvre SET genre = %s WHERE code = %s", (nouveauGenre, codeModif))
            case 5:
                nouveauCode = input("Nouveau code de classification: ")
                cur.execute("UPDATE Ressource SET codeClassification = %s WHERE code = %s", (nouveauCode, codeModif))
                cur.execute("UPDATE Oeuvre SET codeClassification = %s WHERE code = %s", (nouveauCode, codeModif))
            case 6:
                nouvelleLongueur = int(input("Nouvelle durée (en minutes): "))
                cur.execute("UPDATE Oeuvre SET longueur = %s WHERE code = %s", (nouvelleLongueur, codeModif))
            case 0:
                return
        connexion.commit()
    choixModif = int(input("Modifier une autre oeuvre?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierOeuvreMusicale(connexion)

def modifierFilm(connexion):
    codeModif = input("Saisir le code du film à modifier: ")
    cur = connexion.cursor()
    cur.execute("SELECT code FROM Film WHERE code = %s", (codeModif,))
    row = cur.fetchone()
    if len(row) == 0:
        print("Ce film n'existe pas. ")
    else:
        print("Choisir un champ à modifier:\n(1) titre\n(2) date d'apparition\n(3) Éditeur\n(4) Genre\n(5) Code de classification\n(6) Langue\n(7) Durée\n(8) Synopsis\n(0) Annuler")
        choixChamp = int(input("Choisir entre 0 et 8: "))
        while choixChamp < 0 and choixChamp > 8:
            choixChamp = int(input("Saisie invalide, choisir entre 0 et 8: "))
        match choixChamp:
            case 1:
                nouveauTitre = input("Nouveau titre: ")
                cur.execute("UPDATE Ressource SET titre = %s WHERE code = %s", (nouveauTitre, codeModif))
                cur.execute("UPDATE Film SET titre = %s WHERE code = %s", (nouveauTitre, codeModif))
            case 2:
                nouvelleDate = input("Nouvelle date d'apparition: ")
                cur.execute("UPDATE Ressource SET dateApparition = %s WHERE code = %s", (nouvelleDate, codeModif))
                cur.execute("UPDATE Film SET dateApparition = %s WHERE code = %s", (nouvelleDate, codeModif))
            case 3:
                nouveauEditeur = input("Nouvel éditeur: ")
                cur.execute("UPDATE Ressource SET editeur = %s WHERE code = %s", (nouveauEditeur, codeModif))
                cur.execute("UPDATE Film SET editeur = %s WHERE code = %s", (nouveauEditeur, codeModif))
            case 4:
                nouveauGenre = input("Nouveau genre: ")
                cur.execute("UPDATE Ressource SET genre = %s WHERE code = %s", (nouveauGenre, codeModif))
                cur.execute("UPDATE Film SET genre = %s WHERE code = %s", (nouveauGenre, codeModif))
            case 5:
                nouveauCode = input("Nouveau code de classification: ")
                cur.execute("UPDATE Ressource SET codeClassification = %s WHERE code = %s", (nouveauCode, codeModif))
                cur.execute("UPDATE Film SET codeClassification = %s WHERE code = %s", (nouveauCode, codeModif))
            case 6:
                nouvelleLangue = input("Nouvelle langue: ")
                cur.execute("UPDATE Film SET langue = %s WHERE code = %s", (nouvelleLangue, codeModif))
            case 7:
                nouvelleDuree = int(input("Nouvelle durée (en minutes): "))
                cur.execute("UPDATE Film SET duree = %s WHERE code = %s", (nouvelleDuree, codeModif))
            case 8:
                nouveauSynopsis = input("Nouveau synopsis: ")
                cur.execute("UPDATE Film SET synopsis = %s WHERE code = %s", (nouveauSynopsis, codeModif))
            case 0:
                return
        connexion.commit()
    choixModif = int(input("Modifier un autre film?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierFilm(connexion)

# Ajouter un exemplaire
def ajouterExemplaire(connexion):
    cur = connexion.cursor()
    codeRessource = input("Veuillez saisir le code de la ressource: ")
    cur.execute("SELECT code FROM Ressource WHERE code = %s", (codeRessource,))
    result = cur.fetchall()
    if len(result) == 0:
        print("\nCette ressource n'existe pas. ")
    else:
        print("Veuillez saisir les informations: ")
        idExemplaire = input("Id exemplaire: ")
        etat = input("État de l'exemplaire (neuf, bon, abime, perdu): ")
        while etat not in ['neuf', 'bon', 'abime', 'perdu']:
            etat = input("État non reconnu; états possibles: neuf, bon, abime, perdu\nVotre choix: ")
        cur.execute("INSERT INTO Exemplaire VALUES (%s, %s, True, %s, NULL)", (idExemplaire, etat, codeRessource))
        connexion.commit()
    print("Voulez-vous ajouter un autre exemplaire?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterExemplaire(connexion)

# Afficher tous les exemplaires d'une ressource
def afficherExemplaires(connexion):
    cur = connexion.cursor()
    codeRessource = input("Veuillez saisir le code de la ressource: ")
    cur.execute("SELECT code FROM Ressource WHERE code = %s", (codeRessource,))
    result = cur.fetchall()
    if len(result) == 0:
        print("\nCette ressource n'existe pas. ")
    else:
        cur.execute("SELECT idExemplaire, etat, disponible, reserve FROM Exemplaire WHERE ressource = %s", (codeRessource,))
        result = cur.fetchall()
        for i in result:
            print("******* Id de l'exemplaire: ", i[0], " *******")
            print("État: ", i[1])
            print("Disponible: ", i[2])
            print("Réservé par l'adhérent: ", i[3], "\n")

def modifierExemplaire(connexion):
    cur = connexion.cursor()
    idExemplaire = input("Veuillez saisir l'ID' de l'exemplaire: ")
    cur.execute("SELECT idExemplaire FROM Exemplaire WHERE idExemplaire = %s", (idExemplaire,))
    if len(cur.fetchall()) == 0:
        print("L'exemplaire n'existe pas")
    else:
        print("Veuillez saisir les informations mises à jour:")
        etat = input("État de l'exemplaire (neuf, bon, abime, perdu): ")
        while etat not in ['neuf', 'bon', 'abime', 'perdu']:
            etat = input("État non reconnu; états possibles: neuf, bon, abime, perdu\nVotre choix: ")
        disponible = input("Disponible (True/False): ")
        while disponible not in ['True', 'False']:
            disponible = input("Disponible (True/False): ")
        ressource = input("Code de la ressource: ")
        ask_reserve = input("Est-il réservé par un adhérent? (oui/non) ")
        if ask_reserve == "oui":
            reserve = input("Id de l'adhérent ayant réservé (faire Entrée sinon): ")
            cur.execute("UPDATE Exemplaire SET etat=%s, disponible=%s, ressource=%s, reserve=%s",
                        (etat, disponible, ressource, reserve))
        else:
            cur.execute("UPDATE Exemplaire SET etat=%s, disponible=%s, ressource=%s",
                        (etat, disponible, ressource))
        connexion.commit()
    choixModif = int(input("Modifier un autre exemplaire?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierExemplaire(connexion)

def ajouterPret(connexion):
    login = input("Entrez le login de l'emprunteur: ")
    cur = connexion.cursor()
    cur.execute("select droitPret from Adherent where login=%s", (login,))
    if cur.fetchall()[0][0] == False:
        print("L'utilisateur ne peut pas emprunter")
    else:
        titreRessource = input("Entrez le nom de la ressource: ")
        cur.execute("select code from Ressource where titre=%s", (titreRessource,))
        codeRessource = cur.fetchall()[0][0]
        cur.execute("select idExemplaire, etat from Exemplaire where ressource= %s and disponible = %s and (etat = %s or etat = %s) and reserve IS NULL", (codeRessource, True, 'neuf', 'bon'))
        exemplaires = cur.fetchall()
        if len(exemplaires) == 0:
            print("Le document n'est pas disponible")
        else:
            print("Voici les exemplaires disponibles:\n")
            for i in exemplaires:
                print("Exemplaire", i[0], ", état: ", i[1])
            exemplaire = input("Id de l'exemplaire choisi: ")
            debut = input("Entrez la date de début du prêt (AAAA-MM-JJ): ")
            fin = input("Entrez la date de fin du prêt (AAAA-MM-JJ): ")
            id = input("Id du prêt: ")
            cur.execute("insert into Pret values (%s, %s, %s, NULL, NULL, %s, %s)", (id, debut, fin, exemplaire, login))
            cur.execute("update Exemplaire set disponible = False where idExemplaire=%s", (exemplaire,))
            connexion.commit()
    print("Voulez-vous ajouter un autre prêt?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterPret(connexion)

# Afficher les prêts en cours effectués par un adhérent
def afficherPrets(connexion):
    cur = connexion.cursor()
    login = input("Veuillez saisir le login de l'adhérent: ")
    cur.execute("SELECT login FROM Adherent WHERE login = %s", (login,))
    result = cur.fetchall()
    if len(result) == 0:
        print("\nCet adhérent n'existe pas. ")
    else:
        cur.execute("SELECT idPret, dateDebut, dateRetourPrevue, exemplaire FROM Pret WHERE adherent = %s AND dateRetourReelle IS NULL;",
                    (login,))
        result = cur.fetchall()
        for i in result:
            print("******* Id du prêt: ", i[0], " *******")
            print("Début de prêt: ", i[1])
            print("Date de retour prévue: ", i[2])
            print("Id de l'exemplaire: ", i[3], "\n")

# Retourner un prêt
def retournerPret(connexion):
    cur = connexion.cursor()
    idPret = input("Id du prêt: ")
    cur.execute("SELECT * FROM Pret WHERE idPret = %s", (idPret,))
    resultat = cur.fetchall()
    if len(resultat) == 0:
        print("Prêt non trouvé")
        return
    exemplaire = resultat[0][5]
    adherent = resultat[0][6]
    etatretour = input("État de retour de l'exemplaire (neuf, bon, abime, perdu): ")
    while etatretour not in ['neuf', 'bon', 'abime', 'perdu']:
        etatretour = input("État non reconnu; états possibles: neuf, bon, abime, perdu\nVotre choix: ")
    if etatretour == 'abime' or etatretour == 'perdu':
        print("L'utilisateur doit rembourser l'exemplaire' pour pouvoir à nouveau emprunter.")
        cur.execute("UPDATE Exemplaire SET disponible = False where idExemplaire = %s", (exemplaire,))
        cur.execute("UPDATE Exemplaire SET etat = %s where idExemplaire = %s", (etatretour, exemplaire))
        cur.execute("UPDATE Adherent SET droitPret = False WHERE login = %s", (adherent,))
        idsanction = input("Id de la sanction: ")
        if etatretour == 'abime':
            cur.execute("INSERT INTO Sanction VALUES (%s, 'deterioration', current_date, NULL, %s, %s)", (idsanction, adherent, resultat[0][0]))
        else:
            cur.execute("INSERT INTO Sanction VALUES (%s, 'perte', current_date, NULL, %s, %s)",
                        (idsanction, adherent, resultat[0][0]))
        connexion.commit()
    else:
        cur.execute("UPDATE Exemplaire SET disponible = True where idExemplaire = %s", (exemplaire,))
        connexion.commit()
        # gestion du retard

    cur.execute("UPDATE Pret SET etatRetour = %s", (etatretour,))
    cur.execute("UPDATE Pret SET dateRetourReelle = CURRENT_DATE")
    connexion.commit()
    cur.execute("SELECT * FROM Pret WHERE idPret = %s AND dateRetourReelle > dateRetourPrevue", (idPret,))
    resultat = cur.fetchall()
    if len(resultat) > 0:
        print("L'utilisateur a rendu le document en retard.")
        idsanction = input("Id de la sanction: ")
        dateRetour = resultat[0][3]
        datePrevue = resultat[0][2]
        d1 = date(int(dateRetour[0:4]), int(dateRetour[5:7]), int(dateRetour[8:10]))
        d0 = date(int(datePrevue[0:4]), int(datePrevue[5:7]), int(datePrevue[8:10]))
        delta = d1 - d0
        dureeretard = delta.days
        finsanction = date.today() + timedelta(days=dureeretard)
        finsanction = finsanction.strftime('%Y-%m-%d')
        cur.execute("INSERT INTO Sanction VALUES (%s, 'retard', current_date, %s, %s, %s)", (idsanction, finsanction, adherent, idPret))
        connexion.commit()

def ajouterContributeur(connexion):
    print("Veuillez saisir les informations ci-dessous: ")
    id = input("ID du contributeur: ")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    dateNaissance = input("Date de naissance (AAAA-MM-JJ): ")
    nationalite = input("Nationalité: ")
    cur = connexion.cursor()
    cur.execute("INSERT INTO COntributeur VALUES (%s, %s, %s, %s, %s)", (id, nom, prenom, dateNaissance, nationalite))
    print("Ajout réussi! Voulez-vous ajouter un autre contributeur?")
    choixAjout = int(input("(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixAjout < 0 and choixAjout > 1:
        choixAjout = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixAjout == 1:
        ajouterContributeur(connexion)

def blacklisterAdherent(connexion):
    cur = connexion.cursor()
    login = input("Entrer le login de l'adhérent: ")
    cur.execute("SELECT login FROM Adherent WHERE login = %s", (login,))
    resultat = cur.fetchall()
    if len(resultat) == 0:
        print("Cet adhérent n'existe pas. ")
        return
    else:
        cur.execute("UPDATE Adherent SET blacklist = True where login = %s", (login,))
        cur.execute("UPDATE Adherent SET adhesion = False where login = %s", (login,))
        cur.execute("UPDATE Adherent SET droitPret = False where login = %s", (login,))
        connexion.commit()

def undoBlacklisterAdherent(connexion):
    cur = connexion.cursor()
    login = input("Entrer le login de l'adhérent: ")
    cur.execute("SELECT login FROM Adherent WHERE login = %s", (login,))
    resultat = cur.fetchall()
    if len(resultat) == 0:
        print("Cet adhérent n'existe pas. ")
        return
    else:
        cur.execute("UPDATE Adherent SET blacklist = False where login = %s", (login,))
        connexion.commit()

def estAdherent(connexion, adherent):
    adhesion = False
    cur = connexion.cursor()
    cur.execute("Select login from Adherent where login=%s and adhesion = True", (adherent,))
    resultat = cur.fetchall()
    if len(resultat) > 0:
        adhesion = True
    return adhesion

def nombrePrets(connexion, adherent):
    cur = connexion.cursor()
    cur.execute("Select count (*) from Adherent inner join Pret on Adherent.login = Pret.adherent where dateRetourReelle > current_date and login=%s", (adherent,))
    resultat = cur.fetchall()
    return resultat[0]

def nombreSanctions(connexion, adherent):
    cur = connexion.cursor()
    cur.execute("Select count (*) from Adherent inner join Sanction on Adherent.login = Sanction.adherent where (DateFinSanction > current_date or DateFinSanction IS NULL) and login=%s", (adherent,))
    resultat = cur.fetchall()
    return resultat[0]

def peutEmprunter(connexion, adherent):
    emprunt = False
    cur = connexion.cursor()
    cur.execute("Select login from Adherent where login=%s and droitPret = True", (adherent,))
    resultat = cur.fetchall()
    if len(resultat) > 0:
        emprunt = True
    return emprunt

def changerDroitEmprunt(connexion, adherent, nouveauDroit):
    cur = connexion.cursor()
    cur.execute("update Adherent set droitPret = %s where login=%s", (nouveauDroit, adherent))
    connexion.commit()

#Afficher la disponibilité d'un titre de ressource, si pas disponible afficher sa date de retour prévue
def DisponibiliteEtDateRetourPrevue(connexion):
    cur = connexion.cursor()
    titre = input("Entrez le titre dont vous voulez avoir la disponibilité ou la date de retour :")
    cur.execute("SELECT R.titre, E.disponible, P.dateRetourPrevue FROM (Exemplaire E INNER JOIN Ressource R ON E.ressource = R.code) LEFT OUTER JOIN Pret P ON E.idExemplaire = P.exemplaire WHERE R.titre = %s ORDER BY idExemplaire", (titre,))



#Afficher tous les livres de la bibliothèque
def afficherLivres(connexion) :
    cur = connexion.cursor()
    cur.execute("SELECT * FROM Livre")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("******* Code: ", i[0], " *******")
            print("Titre: ", i[1])
            print("Date d'apparition: ", i[2])
            print("Éditeur: ", i[3])
            print("Genre: ", i[4])
            print("Code de classification: ", i[5])
            print("ISBN: ", i[6])
            print("Résumé: ", i[7])
            print("Langue: ", i[8], "\n")
    else:
        print("Aucun livre disponible")

#Afficher toutes les oeuvres musicales de la bibliothèque
def afficherOeuvresMusicales(connexion) :
    cur = connexion.cursor()
    cur.execute("SELECT * FROM OeuvreMusicale")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("******* Code: ", i[0], " *******")
            print("Titre: ", i[1])
            print("Date d'apparition: ", i[2])
            print("Éditeur: ", i[3])
            print("Genre: ", i[4])
            print("Code de classification: ", i[5])
            print("Durée en minutes: ", str(i[6]), "\n")
    else:
        print("Aucune oeuvre disponible")

#Afficher tous les films de la bibliothèque
def afficherFilms(connexion):
    cur = connexion.cursor()
    cur.execute("SELECT * FROM Film")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("******* Code: ", i[0], " *******")
            print("Titre: ", i[1])
            print("Date d'apparition: ", i[2])
            print("Éditeur: ", i[3])
            print("Genre: ", i[4])
            print("Code de classification: ", i[5])
            print("Langue: ", i[6])
            print("Durée en minutes: ", str(i[7]))
            print("Synopsis: ", i[8], "\n")
    else:
        print("Aucun film disponible")

#Afficher tous les contributeurs
def afficherContributeurs(connexion):
    cur = connexion.cursor()
    cur.execute("SELECT * FROM Contributeur")
    resultat = cur.fetchall()
    if len(resultat) > 0:
        for i in resultat:
            print("******* Id: ", i[0], " *******")
            print("Nom: ", i[1])
            print("Prénom: ", i[2])
            print("Date de naissance: ", i[3])
            print("Nationalité: ", i[4], "\n")
    else:
        print("Aucun contributeur enregistré")



def ajouterAuteur(connexion):
    cur = connexion.cursor()
    print("Saisie des informations:\n")
    contributeur = input("Auteur (idContributeur): ")
    cur.execute("SELECT idContributeur FROM Contributeur WHERE idContributeur = %s", (contributeur,))
    resultatA = cur.fetchall()
    if len(resultatA) == 0:
        print("Ce contributeur n'existe pas. ")
        return
    livre = input("Livre (code du Livre): ")
    cur.execute("SELECT code FROM Livre WHERE code = %s", (livre,))
    resultatL = cur.fetchall()
    if len(resultatL) == 0:
        print("Ce livre n'existe pas. ")
        return
    cur.execute("INSERT INTO AEcrit VALUES (%s, %s)", (contributeur, livre))
    connexion.commit()

# Ajouter un compositeur
def ajouterCompositeur(connexion):
    cur = connexion.cursor()
    print("Saisie des informations:\n")
    contributeur = input("Compositeur (idContributeur): ")
    cur.execute("SELECT idContributeur FROM Contributeur WHERE idContributeur = %s", (contributeur,))
    resultatC = cur.fetchall()
    if len(resultatC) == 0:
        print("Ce contributeur n'existe pas. ")
        return
    oeuvre = input("Oeuvre (code de l'oeuvre): ")
    cur.execute("SELECT code FROM OeuvreMusicale WHERE code = %s", (oeuvre,))
    resultatO = cur.fetchall()
    if len(resultatO) == 0:
        print("Cet oeuvre n'existe pas. ")
        return
    cur.execute("INSERT INTO ACompose VALUES (%s, %s)", (contributeur, oeuvre))
    connexion.commit()

# Ajouter un interprete
def ajouterInterprete(connexion):
    cur = connexion.cursor()
    print("Saisie des informations:\n")
    contributeur = input("Interprète (idContributeur): ")
    cur.execute("SELECT idContributeur FROM Contributeur WHERE idContributeur = %s", (contributeur,))
    resultatI = cur.fetchall()
    if len(resultatI) == 0:
        print("Ce contributeur n'existe pas. ")
        return
    oeuvre = input("Oeuvre (code de l'oeuvre): ")
    cur.execute("SELECT code FROM OeuvreMusicale WHERE code = %s", (oeuvre,))
    resultatO = cur.fetchall()
    if len(resultatO) == 0:
        print("Cet oeuvre n'existe pas. ")
        return
    cur.execute("INSERT INTO AInterprete VALUES (%s, %s)", (contributeur, oeuvre))
    connexion.commit()

# Ajouter un realisateur
def ajouterRealisateur(connexion):
    cur = connexion.cursor()
    print("Saisie des informations:\n")
    contributeur = input("Réalisateur (idContributeur): ")
    cur.execute("SELECT idContributeur FROM Contributeur WHERE idContributeur = %s", (contributeur,))
    resultatR = cur.fetchall()
    if len(resultatR) == 0:
        print("Ce contributeur n'existe pas. ")
        return
    film = input("Film (code du film): ")
    cur.execute("SELECT code FROM Film WHERE code = %s", (film,))
    resultatF = cur.fetchall()
    if len(resultatF) == 0:
        print("Ce film n'existe pas. ")
        return
    cur.execute("INSERT INTO ARealise VALUES (%s, %s)", (contributeur, film))
    connexion.commit()


# Ajouter un acteur
def ajouterActeur(connexion):
    cur = connexion.cursor()
    print("Saisie des informations:\n")
    contributeur = input("Acteur (idContributeur): ")
    cur.execute("SELECT idContributeur FROM Contributeur WHERE idContributeur = %s", (contributeur,))
    resultatA = cur.fetchall()
    if len(resultatA) == 0:
        print("Ce contributeur n'existe pas. ")
        return
    film = input("Film (code du film): ")
    cur.execute("SELECT code FROM Film WHERE code = %s", (film,))
    resultatF = cur.fetchall()
    if len(resultatF) == 0:
        print("Ce film n'existe pas. ")
        return
    cur.execute("INSERT INTO AJoueDans VALUES (%s, %s)", (contributeur, film))
    connexion.commit()

def afficherSanctions(connexion):
    cur = connexion.cursor()
    login = input("Veuillez saisir le login de l'adhérent: ")
    cur.execute("SELECT login FROM Adherent WHERE login = %s", (login,))
    result = cur.fetchall()
    if len(result) == 0:
        print("\nCet adhérent n'existe pas. ")
    else:
        cur.execute(
            "SELECT * FROM Sanction WHERE adherent = %s;",
            (login,))
        result = cur.fetchall()
        for i in result:
            print("******* Id de la sanction: ", i[0], " *******")
            print("Motif: ", i[1])
            print("Début de sanction: ", i[2])
            print("Fin de sanction: ", i[3])
            print("Id de l'adhérent: ", i[4])
            print("Id du prêt: ", i[5], "\n")

def modifierSanction(connexion):
    cur = connexion.cursor()
    idSanction = input("Id de la sanction: ")
    cur.execute("SELECT * FROM Sanction WHERE idSanction = %s", (idSanction,))
    resultat = cur.fetchall()
    if len(resultat) == 0:
        print("Sanction non trouvée")
        return
    print("Choisir un champ à modifier:\n(1) motif\n(2) date de début de sanction\n(3) Date de fin de sanction\n(4) Id de l'adhérent\n(5) Id du pret\n(0) Annuler")
    choixChamp = int(input("Choisir entre 0 et 5: "))
    while choixChamp < 0 and choixChamp > 5:
        choixChamp = int(input("Saisie invalide, choisir entre 0 et 5: "))
    match choixChamp:
        case 1:
            nouveauMotif = input("Nouveau motif: ")
            cur.execute("UPDATE Sanction SET motif = %s WHERE idSanction = %s", (nouveauMotif, idSanction))
        case 2:
            dateDebut = input("Nouvelle date de début: ")
            cur.execute("UPDATE Sanction SET dateDebut = %s WHERE idSanction = %s", (dateDebut, idSanction))
        case 3:
            dateFin = input("Nouvelle date de fin: ")
            cur.execute("UPDATE Sanction SET dateFin = %s WHERE idSanction = %s", (dateFin, idSanction))
        case 4:
            nouveauAdherent = input("Nouveau id d'adhérent: ")
            cur.execute("UPDATE Sanction SET adherent = %s WHERE idSanction = %s", (nouveauAdherent, idSanction))
        case 5:
            nouveauPret = input("Nouveau id du pret: ")
            cur.execute("UPDATE Sanction SET pret = %s WHERE idSanction = %s", (nouveauPret, idSanction))
        case 0:
            return
    connexion.commit()
    choixModif = int(input("Modifier une autre sanction?\n(0) Non\n(1) Oui\nChoisissez 0 ou 1: "))
    while choixModif < 0 and choixModif > 1:
        choixModif = int(input("Saisie invalide, choisissez 0 ou 1: "))
    if choixModif == 1:
        modifierSanction(connexion)


def statLivre(connexion):
    cur = connexion.cursor()
    cur.execute("select titre,ressource,count from Livre LEFT JOIN (select ressource, count(*) from exemplaire INNER JOIN pret ON exemplaire.idexemplaire = pret.exemplaire group by ressource) as foo on Livre.code=foo.ressource;")
    result = cur.fetchall()
    abscisses = []
    titres = []
    valeurs = []
    n = len(result)
    c = 1
    while c <= n:
        abscisses.append(c)
        c+=1
    for i in result:
        titre = i[0]
        if i[2] == None:
            nombre = 0
        else:
            nombre = i[2]
        titres.append(titre)
        valeurs.append(nombre)
    plt.bar(abscisses, valeurs, tick_label=titres,
            width=0.8, color=['red', 'green', 'blue'])
    plt.xlabel('Livres empruntés')
    plt.ylabel("Nombre d'emprunts")
    plt.title("Graphique illustrant le nombre d'emprunts par livre")
    plt.show()

def statOeuvre(connexion):
    cur = connexion.cursor()
    cur.execute("select titre,ressource,count from OeuvreMusicale LEFT JOIN (select ressource, count(*) from exemplaire INNER JOIN pret ON exemplaire.idexemplaire = pret.exemplaire group by ressource) as foo on OeuvreMusicale.code=foo.ressource;")
    result = cur.fetchall()
    abscisses = []
    titres = []
    valeurs = []
    n = len(result)
    c = 1
    while c <= n:
        abscisses.append(c)
        c+=1
    for i in result:
        titre = i[0]
        if i[2] == None:
            nombre = 0
        else:
            nombre = i[2]
        titres.append(titre)
        valeurs.append(nombre)
    plt.bar(abscisses, valeurs, tick_label=titres,
            width=0.8, color=['red', 'green', 'blue'])
    plt.xlabel('Oeuvres musicales empruntées')
    plt.ylabel("Nombre d'emprunts")
    plt.title("Graphique illustrant le nombre d'emprunts par oeuvre")
    plt.show()

def statFilm(connexion):
    cur = connexion.cursor()
    cur.execute("select titre,ressource,count from Film LEFT JOIN (select ressource, count(*) from exemplaire INNER JOIN pret ON exemplaire.idexemplaire = pret.exemplaire group by ressource) as foo on Film.code=foo.ressource;")
    result = cur.fetchall()
    abscisses = []
    titres = []
    valeurs = []
    n = len(result)
    c = 1
    while c <= n:
        abscisses.append(c)
        c+=1
    for i in result:
        titre = i[0]
        if i[2] == None:
            nombre = 0
        else:
            nombre = i[2]
        titres.append(titre)
        valeurs.append(nombre)
    plt.bar(abscisses, valeurs, tick_label=titres,
            width=0.8, color=['red', 'green', 'blue'])
    plt.xlabel('Films empruntés')
    plt.ylabel("Nombre d'emprunts")
    plt.title("Graphique illustrant le nombre d'emprunts par film")
    plt.show()

def menuAdherent(connexion,login):
    choixAction = -1
    while choixAction != 0:
        print("\n********** Menu **********\n")
        print("Choisissez une action:\n(0) Déconnexion\n(1) Afficher informations personnelles\n(2) Afficher emprunts\n(3) Statistiques\n")
        choixAction = int(input("Choisissez entre 0 et 3: "))
        while choixAction < 0 and choixAction > 3:
            choixAction = int(input("Saisie invalide, choisissez entre 0 et 3: "))
        match choixAction:
            case 0:
                print("Vous avez choisi de vous déconnecter\n")
            case 1:
                consulterInfo(connexion,login)
            case 2:
                consulterEmprunt(connexion,login)
            case 3:
                choixStat = -1
                while choixStat != 0:
                    print("Choisissez une catégorie:\n(0) Retour\n(1) Livres\n(2) Oeuvres musicales\n(3) Films")
                    choixStat = int(input("Choisissez entre 0 et 3: "))
                    while choixStat < 0 and choixStat > 3:
                        choixStat = int(input("Saisie invalide, choisissez entre 0 et 3: "))
                    match choixStat:
                        case 0:
                            print("Vous avez choisi de quitter\n")
                        case 1:
                            statLivre(connexion)
                        case 2:
                            statOeuvre(connexion)
                        case 3:
                            statFilm(connexion)

def consulterInfo(connexion,login):
    cur = connexion.cursor()
    cur.execute("SELECT * FROM Adherent WHERE login = %s", (login,))
    result = cur.fetchall()[0]
    if len(result) == 0:
        print("Erreur")
    else:
        print("******* Informations personnelles *******\n")
        print("Login: ", result[0])
        print("Mot de passe: ", result[1])
        print("Nom: ", result[2])
        print("Prenom: ", result[3])
        print("Adresse: ", result[4])
        print("Email: ", result[5])
        print("Date de naissance: ", result[6])
        print("Numero de telephone: ", result[7])
        print("Est adherent: oui")
        print("Est blackliste: non")
        if result[10] == False:
            print("A le droit d'emprunt: non")
        else:
            print("A le droit d'emprunt: oui")


def consulterEmprunt(connexion,login):
    cur = connexion.cursor()
    cur.execute("SELECT idPret, dateDebut, dateRetourPrevue, dateRetourReelle, titre FROM Pret INNER JOIN (Exemplaire INNER JOIN Ressource ON Exemplaire.ressource = Ressource.code) ON Exemplaire.idExemplaire = Pret.exemplaire WHERE Pret.adherent = %s", (login,))
    result = cur.fetchall()
    if len(result) == 0:
        print("Erreur")
    else:
        for i in result:
            print("********************\n")
            print("Id du pret: ", i[0])
            print("Debut de pret: ", i[1])
            print("Date retour prevue: ", i[2])
            print("Date retour reelle: ", i[3])
            print("Titre de la ressource: ", i[4])
