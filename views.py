from tinydb import TinyDB

from models import name_validation, prenom_validation, phone_validation, naissance_validation, groupe_sanguin, \
    poids_validation, taille_validation, mail, password_generate, password_secretaire

db = TinyDB('data.json', indent=4)
CLIENT = db.table('Client')
SECRETAIRE = db.table('Secretaire')
MEDECIN = db.table('Medecin')


def inscription():
    nom = name_validation()
    prenom = prenom_validation()
    numero = phone_validation()
    naissance = naissance_validation()
    groupe_s = groupe_sanguin()
    poids = poids_validation()
    taille = taille_validation()
    email = mail()
    password = password_generate()

    CLIENT.insert(
        {'nom': nom, 'prenom': prenom, 'numero': numero, 'date-naissance': naissance,
         'groupe-sanguin': groupe_s,
         'poids': poids, 'taille': taille, 'email': email, 'password': password})


def secretaire_inscription():
    nom = name_validation()
    prenom = prenom_validation()
    numero = phone_validation()
    email = mail()
    password = password_secretaire()
    SECRETAIRE.insert(
        {'nom': nom, 'prenom': prenom, 'numero': numero, 'email': email, 'password': password})


def medecin_inscription():
    nom = name_validation()
    prenom = prenom_validation()
    numero = phone_validation()
    email = mail()
    password = password_secretaire()

    MEDECIN.insert(
        {'nom': nom, 'prenom': prenom, 'numero': numero, 'email': email, 'password': password})

