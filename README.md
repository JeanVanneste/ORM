# Programme de gestion de bibliothèque

## Initialisation 
1. Installer mysql ou mariadb sur le serveur
```bash
sudo apt install mysql
```
2. Créer un utilisateur *admin* avec comme mot de passe *password*
```sql
create user 'admin'@'localhost' identified by 'password';
grant all on *.* TO 'admin'@'localhost';
```
3. Créer la base de donnée *library*
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