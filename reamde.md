Affichage simple avec typer . C'est comme le print simple
## typer.echo('Text') 

les paramettres 
Quand on mets un paramettre une devient requit ainsi pour le lancer :
### python nom.py argument
Quand on mets un paramettre optionel on le lance :
### python nom.py --argument nomargument

Pour faire un argument par defaut requis
### txt : str = typer.Argument(...)
les 3 points veut dire que c'est obligatoire et on peut mettre du texte specifique 
### txt : str = typer.Argument(..., help="Message d'aide")
Pour mettre un valeur requis 
### txt : str = typer.Argument(txt, help="Message d'aide")
Si on veut rien mettre , c - a dire pas dargument requis ni de valeur par defaut onn mets None
### txt : str = typer.Argument(None, help="Message d'aide")
Les options rrequis
### txt : str = typer.Optional('...', help="Message d'aide")
Options pas requis, on peut les mettre au debut ou a la fin ce qui n'est pas le cas des options
### txt : str = typer.Argument(False, help="Message d'aide")
Demander des informations a l'utilsateur ou bien une confirmatiion:
### avec typer.prompt() et la fonction typer.confirm()
# prompt est equivalent de input 
 Le confirm on demande si il veut ou pas faire quelque chose 
 ```python
del = typer.confirm('Souhaitez vous suprimer ?')
    if not del:
        typer.echo('On annule operation')
        raise typer.Abort()
print('supression valider')
```
Pour eviter de faire tous cette instruction, on mets Abort=True a l'interieur de confirm
### typer.confirm('Souhaitez vous suprimer ?', abort=True)

Ajouter des commande
# Pour creer des commander  on doit creer une instance d'un app a partir de la classe Typer
## app = typer.Typer()
Pour utiliser les commandes on va utiliser des decorateurs devant la fonction

```python
@app.command('search') #nom de la commande
def search_py():
    main(delete=True,extension='txt)
# quand on affiche l'aide on aura une commande avec le nom de la fonction 

```
Modifier l'appaence du texte. 
# installer colorama
bold, fg (forgrawn) bg (background)
##
```python
prenom = typer.style('nom', bg=typer.colors.BLUE, fg=typer.colors.RED, bold=True, underline=True)
dim= True, blink=True (pour clignoter le text)

```

TOus faire sur une seule ligne
# typer.secho('mon',bg=typer.colors.BLUE, fg=typer.colors.RED)

Rajouter une barre de progression:
```python
def prenom = ['nom', 'age', 'sex', 'mama']
with typer.progressbar(prenom) as progress:
    for pre in progress:
        time.sleep(0.1) 
    

```

dire que paramettre est optionel 
# from typing import Optional
## direc: Optional[str] = typer.Argument(None, help='Message')
# sortir du script raise typer.Exit()

Pour lancer typer:
cette structer fait le que script sera executer que quand on lance le script
if __name__ == '__main__':
    typer.run(main)
    app()
# racoursi
### control alt shift J : pour selection tout les variable afin de modifier d'un coup
### control w pour selection un elmeent 
### control alt fleche du haut 

# Openai

```python
     import openai
#
# # importer les classes necessaries pour utiliser GPT
# from openai import GPT2Model, GPT2Tokenizer
#
# # pour utliser
# model = GPT2Model.from_pretrained("gpt2-medium")
# # utiliser le tokenize
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#
# # ecrire une boucle infinie pour mettre a user de discuter avec le chatbot . utiliser GPT-2 pour generer
# # une reponse en utilisant les fonctions ``model.generate` et `tokenize.decode`
#
# while True:
#     message = input('Vous : ')
#     reponse = model.generate(
#         prompt=message,
#         max_token=1024,
#         temperature=0.7,
#         top_p=0.9,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     reponse_text = tokenizer.decode(reponse.sample())
#     print(re ponse_text)

```
