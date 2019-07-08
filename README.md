# Programme de gestion de bibliothèque

## Initialisation 
1. Installer mysql ou mariadb sur le serveur
```bash
sudo apt install mysql
```
2. Créer un utilisateur *admin* avec comme mot de passe *password* (Si vous souhaitez utiliser un autre profil, il suffit de modifier *config_db.json*)
```sql
create user 'admin'@'localhost' identified by 'password';
grant all on *.* TO 'admin'@'localhost';
```
3. Créer la base de donnée *library* (ou autre à préciser dans *config_db.json*)
```sql
create database library;
```
4. Installer les bibliothèques python requise 
```bash
pip3 install -r requirement.txt
```
5. Créer le schéma avec *library.sql* ou le script *populate_db.py*
```bash
mysql -p library < library.sql
```
ou
```bash
python3 populate_db.py
```

## Utilisation
Le script *interface.py* permet de rajouter facilement de nouveaux éléments à la base de données. Il faut cependant faire attention à bien rajouter les éléments dans l'ordre.

Pour créer un collection, son éditeur doit exister dans la db. Pour créer un livre, sa collection et au moins un auteur doivent exister dans la db.

Un livre peut avoir plusieurs auteurs et un auteur peut avoir écrit plusieurs livres.

On ne peut indiquer qu'un seul auteur à la création d'un livre mais il est possible d'ajouter les auteurs restants par la suite.

 ## Fonctionnement 
  - Le fichier **database.py** décrit la structure de la base de donnée. Elle permet de recréer les tables si celles sont inexistante dans la base de donnée et de créer les contraintes de clés étrangère. Elle mappe aussi les objets de l'application au données contenues dans la base.
  - Le fichier **ORM.py** contient les différentes fonctions pour créer et interagir avec la base de données.
  - Le fichier **populate_db.py** utilise *ORM.py* pour remplir quelques lignes des tables. 
  - Le fichier **interface.py** est un script permettant un remplissage *user-friendly* de la base de données