import psycopg2
from fonc import *

def connexion(serveur, user, nomDB, motDePasse, port):
    conn = None

    try:
        # connection au serveur PostgreSQL
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=serveur,
            database=nomDB,
            user=user,
            password=motDePasse,
            port=port)

        # création du curseur
        cur = conn.cursor()

        # exécution d'une requête
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # affichage de la version de la BDD PostgreSQL
        db_version = cur.fetchone()
        print(db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('Connection successful.')
            return conn


def main():
    '''host = input("Entrez le nom du serveur: ")
    usr = input("Entrez le nom d'utilisateur: ")
    mdp = input("Entrez le mot de passe: ")
    db = input("Entrez le nom de la base de données: ")
    p = input("Entrez le port: ")'''
    conn = connexion("tuxa.sme.utc", "nf18a018", "dbnf18a018", "b3qzDGeP", "5432")

    choixAccueil = accueil()
    while choixAccueil != 0:
        if choixAccueil == 1:
            print("login pour membre: fontmar")
            print("mot de passe pour fontmar: 1893FMart")
            connexionMembre = authentificationMembre(conn)
            if connexionMembre == True:
                menuMembre(conn)
        elif choixAccueil == 2:
            print("login pour adherent: hasyou")
            print("mot de passe pour hasyou: effnk")
            connexionAdherent = authentificationAdherent(conn)
            if connexionAdherent != None:
                menuAdherent(conn,connexionAdherent)
        choixAccueil = accueil()

    conn.close()
    return 0

main()
