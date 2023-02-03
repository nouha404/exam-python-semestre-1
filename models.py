import json
import os
import time
from datetime import datetime, timedelta
from random import sample

import typer
from rich import print
from rich.console import Console
from rich.progress import track
from rich.table import Table
from tinydb import TinyDB, where

# pour une meilleur affichage
console = Console()


def name_validation():
    nom = input('nom : ')
    while len(nom) < 3:
        nom = input('Invalide \nnom : ')
    return nom


def service_validation():
    service = input('nom du Service : ')
    while len(service) < 3:
        service = input('Invalide \nnom : ')
    return service


def prenom_validation():
    prenom = input('prenom : ')
    while len(prenom) < 3:
        prenom = input('Invalide \nprenom : ')
    return prenom


def phone_validation():
    phone_number = input('numero : ')
    only_indicator_valid = ['77', '78', '70', '75', '76']

    while len(phone_number) != 9 or phone_number[0:2] not in only_indicator_valid:
        phone_number = input('Numero invalide\nnumero : ')
    return phone_number


def naissance_validation():
    jour = input('date de naissance format jj/mm/aaaa\njour : ')
    mois = input('mois : ')
    annee = input('annee : ')

    while not (
            mois <= '12' and (len(jour) < 1 or len(mois) < 1 or len(annee) == 4) and annee <= '2022' and jour <= '31'):
        typer.secho('Invalid', fg=typer.colors.RED, bg=typer.colors.BLACK)
        jour = input('jour : ')
        mois = input('mois : ')
        annee = input('annee : ')
    age = 2022 - int(annee)

    naissance_information = {
        'naissance': f'{jour}/{mois}/{annee}',
        'age': age
    }
    return naissance_information['naissance']


def groupe_sanguin():
    GROUP = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    group_sang = input(f"groupe sanguin [A+, A-, B+, B-, O+, O-, AB+, AB-] : ")
    while group_sang.lower() not in str(GROUP).lower():
        group_sang = input(f"Invalide\ngroupe sanguin [A+, A-, B+, B-, O+, O-, AB+, AB-] : ")
    return group_sang


def poids_validation():
    poids = input('poids : ')
    while not poids.isdigit():
        poids = input('Invalide \npoids : ')
    return poids


def taille_validation():
    taille = input('taille : ')
    while not taille.isdigit():
        taille = input('Invalide \ntaille : ')
    return taille


def mail():
    email = input('email : ')
    while not email.endswith('@gmail.com'):
        email = input('Invalide\nemail : ')
    return email


def password_generate():
    PASS = []
    WORD = '1234567890abcdefghijklmnopqrstuvwxyz{]@#_-'
    PASS.extend(sample(WORD, 8))
    password = ''.join(PASS)
    return password


def password_secretaire():
    password = input('mot de passe : ')
    while not password or len(password) <= 7:
        password = input('Invalide 8 caracateres minimum\nmot de passe : ')
    return password


db = TinyDB('data.json', indent=4)
Client = db.table('Client')
Admin = db.table('admin')
Secretaire = db.table('Secretaire')
MEDECIN = db.table('Medecin')


def change_user_password():
    # JE lui demande de modifier son mot de passe
    info_updating = input("Modifier le mot de passe d'un utilisateur : ")
    # Son nom actuel dans la base de donnée
    info_verification = input("Entrez le prenom actuel de l'utilisateur : ")
    # Je recupere la table client
    for item in Client:
        # Je recupere le nom dans la db
        NAME_IN_CLIENT_TABLE = item.get('prenom')
        if info_verification.lower() == NAME_IN_CLIENT_TABLE:
            # modifier les infos
            Client.update({'password': info_updating}, where('prenom') == NAME_IN_CLIENT_TABLE)
            return print('Mot de passe modifier avec success')


def admin_login():
    login = input('Login : ')
    password = input('Password : ')
    # login_combination = f'{login}{password[-1]}{password[-2]}'
    # premier insersion des infos dans la db
    # Admin.insert({'login': login_combination, 'password': password})
    for item in Admin:
        ADMIN_NAME_IN_TABLE = item.get('login')
        ADMIN_PASSWORD_IN_TABLE = item.get('password')
        while login != ADMIN_NAME_IN_TABLE or password != ADMIN_PASSWORD_IN_TABLE:
            typer.secho('Indentifiant invalid', fg=typer.colors.RED, bg=typer.colors.BLACK)
            login = input('Login : ')
            password = input('Password : ')
        else:
            print('Success\n')
            time.sleep(1)
            os.system('cls')


CLIENT_INF0 = []


def client_login():
    email = input('email : ')
    password = input('Password : ')

    for item in Client:
        CLIENT_EMAIL_IN_TABLE = item.get('email')
        CLIENT_PASSWORD_IN_TABLE = item.get('password')
        # recuperer la table a traveers email dans une liste
        if email == CLIENT_EMAIL_IN_TABLE and password == CLIENT_PASSWORD_IN_TABLE:
            CLIENT_INF0.append(item)

    for item in CLIENT_INF0:
        if email == item['email']:
            typer.secho(f"Success bienvenue {item['prenom']} {item['nom']}", fg=typer.colors.BRIGHT_GREEN)
            time.sleep(0.3)
            os.system('cls')
            # initialisation de la date et l'heure
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y")
            hour_string = now.strftime("%H:%M:%S")
            while True:
                def afficher_rv():
                    if 'date-rendez-vous' in item:
                        print(f"Mes rendez-vous {item['date-rendez-vous']}")
                    else:
                        print("Vous n'avez pas encore de rendez-vous")

                typer.secho(
                    f"a- Prendre Rendez-vous\nb- Afficher rendez prochain\nc- Telecharger l'ordonnace\nd- Disconnect\ne-Prendre rendez-vous demain 10h",
                    fg=typer.colors.BRIGHT_MAGENTA)
                CHOIX_CLIENT = input("Service client : ")
                match CHOIX_CLIENT:
                    case 'a':
                        os.system('cls')
                        table = Table('Date rendez-vous', 'Heure rendez-vous')
                        table.add_row(dt_string, hour_string)
                        console.print(table)
                        Client.upsert({"date-rendez-vous": dt_string, 'heure-rendez-vous': hour_string},
                                      where('email') == item['email'])
                    case 'b':
                        afficher_rv()
                    case 'c':
                        telecharger_ordonnance()
                    case 'd':
                        break
                    case 'e':
                        Client.upsert({"date-rendez-vous": date_demain(), 'heure-rendez-vous': '10h:45'},
                                      where('email') == item['email'])
                        typer.secho('Le rendez-vous a été prise...', fg=typer.colors.BRIGHT_RED)


def telecharger_ordonnance():
    email = input('validez votre mail : ')

    for item in track(Client, description="Verification des informations..."):
        time.sleep(0.5)
        if 'ordonnance' in item:
            if email == item['email']:
                ORDONNANCE_NAME = f"{item['nom']}{item['prenom']}.json"
                with open(ORDONNANCE_NAME, 'w') as f:
                    data = item['ordonnance']
                    json.dump(data, f, indent=4)
            else:
                typer.secho("\nVeillez prendre un rendez-vous\n", fg=typer.colors.BRIGHT_RED,
                                   bg=typer.colors.BRIGHT_BLACK)

    typer.secho('\nOrdonnance telecharger avec succes\n', fg=typer.colors.BRIGHT_GREEN)


# Je l'ai declarer a l'exterieur pour l'importer et tester si sa longueur == 0
SECRETAIRE_INF0 = []


def secretaire_login():
    email = input('email : ')
    password = input('Password : ')

    for item in Secretaire:
        SECRETAIRE_EMAIL_IN_TABLE = item.get('email')
        SECRETAIRE_PASSWORD_IN_TABLE = item.get('password')
        # recuperer la table a traveers email dans une liste
        if email == SECRETAIRE_EMAIL_IN_TABLE and password == SECRETAIRE_PASSWORD_IN_TABLE:
            SECRETAIRE_INF0.append(item)

    for item in SECRETAIRE_INF0:
        if email == item['email']:
            typer.secho(f"Success bienvenue {item['prenom']} {item['nom']}", fg=typer.colors.GREEN)
            time.sleep(2)
            os.system('cls')


def user_printer():
    typer.secho(f"{'*' * 75} CLIENT {'*' * 75}", fg=typer.colors.BRIGHT_GREEN)
    # Faire un progress bar
    for _ in track(range(100), description="Chargement de tous les utilisateurs..."):
        time.sleep(0.02)

    table = Table('NOM', 'PRENOM', 'EMAIL', 'DATE-NAISSANCE', 'GROUPE-SANGUIN', 'POIDS', 'TAILLE', 'SERVICE',
                  'DATE-RENDEZ-VOUS', 'HEURE RENDEZ-VOUS')
    for item in Client:
        table.add_row(item.get('nom', 'pas assigné'),
                      item.get('prenom', 'pas assigné'),
                      item.get('email', 'pas assigné'),
                      item.get('date-naissance', 'pas assigné'),
                      item.get('groupe-sanguin', 'pas assigné'),
                      item.get('poids', 'pas assigné'),
                      item.get('taille', 'pas assigné'),
                      item.get('service', 'pas assigné'),
                      item.get('date-rendez-vous', 'pas assigné'),
                      item.get('heure-rendez-vous', 'pas assigné'),
                      )
    console.print(table)
    typer.secho(f"{'*' * 75} SECRETAIRE {'*' * 75}", fg=typer.colors.BRIGHT_RED)
    for item in Secretaire:
        table.add_row(item.get('nom', 'pas assigné'),
                      item.get('prenom', 'pas assigné'),
                      item.get('email', 'pas assigné'),
                      item.get('date-naissance', 'pas assigné'),
                      item.get('groupe-sanguin', 'pas assigné'),
                      item.get('poids', 'pas assigné'),
                      item.get('taille', 'pas assigné'),
                      item.get('service', 'pas assigné'),
                      item.get('date-rendez-vous', 'pas assigné'),
                      item.get('heure-rendez-vous', 'pas assigné'),
                      )
    console.print(table)
    typer.secho(f"{'*' * 75} MEDECIN {'*' * 75}", fg=typer.colors.BRIGHT_YELLOW)
    for item in MEDECIN:
        table.add_row(item.get('nom', 'pas assigné'),
                      item.get('prenom', 'pas assigné'),
                      item.get('email', 'pas assigné'),
                      )
    console.print(table)
    typer.secho('Chargement terminés.', fg=typer.colors.BRIGHT_MAGENTA)


def lister_rendez_vous():
    len_client = 0
    table = Table('Nom', 'Prenom', 'Numero', 'Date-naissance', 'Groupe-sanguin', 'Poids', 'Taille', 'Email',
                  'Date-rendez-vous', 'Heure rendez-vous')
    for item in Client:
        if 'date-rendez-vous' in item:
            len_client += 1
            table.add_row(f"{str(item['nom']).strip('{}')}", f"{str(item['prenom']).strip('{}')}",
                          f"{str(item['numero']).strip('{}')}", f"{str(item['date-naissance']).strip('{}')}",
                          f"{str(item['groupe-sanguin']).strip('{}')}", f"{str(item['poids']).strip('{}')}",
                          f"{str(item['taille']).strip('{}')}", f"{str(item['email']).strip('{}')}",
                          f"{str(item['date-rendez-vous']).strip('{}')}",
                          f"{str(item['heure-rendez-vous']).strip('{}')}")
    console.print(table)
    typer.secho(f'Que {len_client} clients ayant des rendez vous', fg=typer.colors.BRIGHT_RED)


def creer_rendez_vous():
    typer.secho(f'Creer une rendez pour un client : ', fg=typer.colors.BRIGHT_BLUE)
    email = mail()
    numero = phone_validation()
    service = service_validation()
    # inserer le service quand il ya date de rendez vous sinon on insere la date et l'heure
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    hour_string = now.strftime("%H:%M:%S")

    for _ in track(range(100), description="Creation du rendez vous"):
        time.sleep(0.02)
    for item in Client:
        if item['email'] == email and item['numero'] == numero:
            Client.upsert({"date-rendez-vous": dt_string, 'heure-rendez-vous': hour_string, 'service': service},
                          where('numero') == item['numero'])
        # else:
        #     print(f"Cet individu n'existe pas...")


MEDECIN_INF0 = []


def medecin_login():
    email = mail()
    password = input('Password : ')

    for item in MEDECIN:
        MEDECIN_EMAIL_IN_TABLE = item.get('email')
        MEDECIN_PASSWORD_IN_TABLE = item.get('password')
        # recuperer la table a traveers email dans une liste
        if email == MEDECIN_EMAIL_IN_TABLE and password == MEDECIN_PASSWORD_IN_TABLE:
            MEDECIN_INF0.append(item)

    for item in MEDECIN_INF0:
        if email == item['email']:
            typer.secho(f"Success bienvenue {item['prenom']} {item['nom']}", fg=typer.colors.BRIGHT_GREEN)
            time.sleep(2)
            os.system('cls')


def modification_service():
    email = input('email du Client : ')
    numero = input('Numero du Client : ')
    new_service = input('Nouveau Service : ')
    for item in track(Client, description="Modification du service"):
        time.sleep(0.01)
        if email == item['email'] and numero == item['numero']:
            Client.update({'service': new_service}, where('service') == item['service'])
            typer.secho(f"Le service de {item['prenom']} a été modifié en {new_service}", fg=typer.colors.BRIGHT_GREEN)


def creer_service():
    email = input('email du Client : ')
    numero = input('Numero du Client : ')
    new_service = input('Service : ')
    for _ in track(range(100), description="Creation du service"):
        time.sleep(0.03)
    for item in Client:
        if email == item['email'] and numero == item['numero']:
            Client.upsert({'service': new_service}, where('email') == item['email'])
        typer.secho(f"Le service de {item['prenom']} a été creer en {new_service}", fg=typer.colors.BRIGHT_GREEN)


def affection_medecin():
    client_mail = input('Email du Client : ')
    mail_medecin = input('Email du Medecin : ')

    for item in MEDECIN:
        if item['email'] == mail_medecin:
            for clt in Client:
                if client_mail == clt['email']:
                    Client.upsert({'Medecin-affecter': {'nom': item['nom'], 'prenom': item['prenom'],
                                                        'mail': item['email'], 'numero': item['numero']}, },
                                  where('email') == clt['email'])


def lister_mes_affection():
    # recupere les information si le mail du medecin dans MEDECIN_INFO est egale a celle du mail de la table client
    medecin_mail = typer.prompt('Validez votre mail')
    table = Table('NOM', 'PRENOM', 'EMAIL', 'DATE-NAISSANCE', 'GROUPE-SANGUIN', 'POIDS', 'TAILLE', 'SERVICE')
    for item in Client:
        if 'Medecin-affecter' in item:
            medecin_mail_in_client = item.get('Medecin-affecter').get('mail')
            if medecin_mail in medecin_mail_in_client:
                # item.get(clé, "valeur")  si la clé n'est pas présente dans le dictionnaire ca renvoie l'autre valeur.
                table.add_row(item.get('nom', 'pas assigné'),
                              item.get('prenom', 'pas assigné'),
                              item.get('email', 'pas assigné'),
                              item.get('date-naissance', 'pas assigné'),
                              item.get('groupe-sanguin', 'pas assigné'),
                              item.get('poids', 'pas assigné'),
                              item.get('taille', 'pas assigné'),
                              item.get('service', 'pas assigné'))
    console.print(table)


def prescrire_ordonnnace():
    ARRAY_MEDOC = []
    email = input('mail du Client : ')
    numero = input('Numero du Client : ')
    medicament = input('Nom du Medicament : ')
    while medicament != '5':
        typer.secho('Appuisez sur 5 pour quitter...\n', fg=typer.colors.RED)
        medicament = input('Nom du Medicament : ')
        ARRAY_MEDOC.append(medicament)
        if medicament == '5':
            break
    for item in Client:
        if email == item['email'] and numero == item['numero']:
            Client.upsert({'ordonnance': ARRAY_MEDOC}, where('email') == item['email'])
            return typer.secho(f"{len(ARRAY_MEDOC)} medicament ont été bien prescrit a {item['nom']} {item['prenom']}",
                               fg=typer.colors.BRIGHT_GREEN)


# Rajoue demander par le prof
def date_demain():
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    # retourn la date de demain
    return tomorrow.date().strftime("%Y-%m-%d")

# print(date_demain())
