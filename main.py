import os
import time

import typer

from models import admin_login, change_user_password, client_login, user_printer, \
    lister_rendez_vous, secretaire_login, SECRETAIRE_INF0, MEDECIN_INF0, CLIENT_INF0, creer_rendez_vous, \
    medecin_login, modification_service, affection_medecin, \
    lister_mes_affection, prescrire_ordonnnace, creer_service
from views import inscription, secretaire_inscription, medecin_inscription

while True:
    typer.secho(f"client secretaire medecin admin Quitter\n 1        2          3      4      5 ",
                fg=typer.colors.BRIGHT_BLUE, bg=typer.colors.BLACK)
    CHOIX = typer.prompt('Faite votre choix  ')
    os.system('cls')
    typer.secho(f"""--------------------------------------------------
                        Connexion
--------------------------------------------------""")
    match CHOIX:
        case '1':
            client_login()
            if len(CLIENT_INF0) == 0:
                print('Vous avez été bloqué ')
                time.sleep(2)
                os.system('cls')
            else:
                # Menu a afficher
                continue
        case '2':
            os.system('cls')
            secretaire_login()
            if len(SECRETAIRE_INF0) == 0:
                typer.secho('Vous avez été bloqué ', fg=typer.colors.RED, bg=typer.colors.BLACK)
                time.sleep(2)
                os.system('cls')

            elif len(SECRETAIRE_INF0) != 0:
                while True:
                    typer.secho("a- Creer rendez-vous\nb- Modifiez rendez-vous\nc- Lister rendez vous\ne- Disconnect",
                                fg=typer.colors.BRIGHT_MAGENTA)
                    CHOIX_SECRETAIRE = typer.prompt("Service Secretaire ")

                    if CHOIX_SECRETAIRE.lower() == 'a':
                        creer_rendez_vous()

                    elif CHOIX_SECRETAIRE.lower() == 'b':
                        typer.secho("1- Modifier service\n2 - Affecter a un medecin\n3- Creer un service",
                                    fg=typer.colors.MAGENTA)
                        CHOIX_MODIFICATION = typer.prompt("Votre choix : ")

                        match CHOIX_MODIFICATION:
                            case '1':
                                modification_service()
                                # modifier le nom d'une service
                            case '2':
                                affection_medecin()
                            case '3':
                                creer_service()

                    elif CHOIX_SECRETAIRE.lower() == 'c':
                        lister_rendez_vous()
                    elif CHOIX_SECRETAIRE.lower() == 'e':
                        break
        case '3':
            os.system('cls')
            medecin_login()
            if len(MEDECIN_INF0) == 0:
                typer.secho('Vous avez été bloqué ', fg=typer.colors.RED, bold=True)
                time.sleep(2)
                os.system('cls')
            elif len(MEDECIN_INF0) != 0:
                while True:
                    typer.secho("a- Lister les clients affecter a moi\nb- Prescrire une ordonnance\nc-Disconnect",
                                fg=typer.colors.BRIGHT_GREEN)
                    CHOIX_MEDECIN = typer.prompt("Service Medecin ")
                    match CHOIX_MEDECIN.lower():
                        case 'a':
                            os.system('cls')
                            lister_mes_affection()
                            # typer.secho("Vous avez été bloqué", fg=typer.colors.BRIGHT_RED)

                        case 'b':
                            prescrire_ordonnnace()
                        case 'c':
                            break

        case '4':
            admin_login()
            while True:
                typer.secho(
                    f"a - Lister Utilisateurs \nb - Ajouter utilisateurs\nc - Modifier Utilisateurs\nd - Disconnect\n",
                    fg=typer.colors.BRIGHT_RED)
                CHOIX_ADMIN = typer.prompt("Service admin ")
                os.system('cls')

                match CHOIX_ADMIN:
                    case 'a':
                        os.system('cls')
                        user_printer()
                    case 'b':
                        os.system('cls')
                        typer.secho('u - Ajouter Utilisateurs\ns - Ajouter Secretaire\nm - Ajouter Medecin',
                                    fg=typer.colors.BRIGHT_BLACK, bg=typer.colors.BRIGHT_WHITE, blank=True)
                        CHOIX_USER_ADD = typer.prompt("Votre choix ")
                        if CHOIX_USER_ADD.lower() == 'u':
                            inscription()
                            typer.secho("L'utilisateurs a été ajoutée", fg=typer.colors.BRIGHT_GREEN)
                        elif CHOIX_USER_ADD.lower() == 's':
                            secretaire_inscription()
                            typer.secho("Le secretaire a été ajoutée", fg=typer.colors.BRIGHT_GREEN)
                        elif CHOIX_USER_ADD.lower() == 'm':
                            medecin_inscription()
                            typer.secho("Le medecin a été ajoutée", fg=typer.colors.BRIGHT_GREEN)
                        time.sleep(3)
                        os.system('cls')
                    case 'c':
                        change_user_password()
                        time.sleep(3)
                        os.system('cls')
                    case 'd':
                        break
        case '5':
            typer.secho('Aurevoir ! ', fg=typer.colors.RED)
            break
