import sqlite3

def liste_personnage():
    connexion = sqlite3.connect('powerapp/marvel.db')
    curseur = connexion.cursor()
    sql = 'SELECT * FROM personnage ORDER BY puissance DESC '
    curseur.execute(sql)
    personnages = curseur.fetchall()

    for p in personnages:
        print(p)
    return personnages