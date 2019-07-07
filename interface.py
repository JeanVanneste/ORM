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

if __name__ == "__main__":
    
    while (True):
        print("1. Créer un éditeur")
        print("2. Créer une collection")
        print("3. Créer un auteur")

        option = input()

        if (option == "1") : create_editor()
        elif (option == "2") : create_collection()
        elif (option == "3") : create_author()
        else: 
            print("Option invalide")
            break