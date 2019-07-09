import ORM

def create_editor():
    editorName = input("Quel est le nom de l'éditeur ?\n")
    fondationYear = input("En quelle année l'éditeur a-t-il était créé ?\n")
    print(editorName + " " + fondationYear + " ajouté")
    ORM.editor_create(editorName, fondationYear)

def create_collection():
    collectionName = input("Comment s'appelle la collection ?\n")
    editor = input("Quel est l'éditeur de la collection ?\n")
    print (collectionName + " créé par " + editor + " ajoutée")
    ORM.collection_create(collectionName, editor)

def create_author():
    authorFirstName = input("Quel est le prénom de l'auteur/autrice ?\n")
    authorLastName = input("Quel est le nom de l'auteur/autrice ?\n")
    print(authorFirstName + " " + authorLastName + " ajouté·e")
    ORM.author_create(authorFirstName, authorLastName)

def create_book():
    title = input("Quel est le titre du livre?\n")
    isbn = input("Quel est le code ISBN du livre ?\n")
    authorFirstName = input("Quel est le prénom du premier auteur ?\n")
    authorLastName = input("Quel est le nom du premier auteur ?\n")
    publicationYear = input("En quelle année le livre a-t-il été publié ?\n")
    collection = input("À quelle collection le livre appartient-il ?\n")
    print(title + " ajouté")
    ORM.book_create(title, isbn, publicationYear, collection, authorFirstName, authorLastName)

def add_author():
    title = input("Titre du livre :\n")
    firstName = input("Prénom de l'auteur :\n")
    lastName = input("Nom de l'auteur :\n")
    ORM.book_add_author(title, firstName, lastName)

if __name__ == "__main__":

    while (True):
        print("1. Créer un éditeur")
        print("2. Créer une collection")
        print("3. Créer un auteur")
        print("4. Créer un livre")
        print("5. Ajouter un auteur à un livre")
        option = input()

        if (option == "1") : create_editor()
        elif (option == "2") : create_collection()
        elif (option == "3") : create_author()
        elif (option == "4") : create_book()
        elif (option == "5") : add_author()
        else: 
            print("Option invalide")
            print("Au revoir")
            break