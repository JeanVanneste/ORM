import ORM

def create_editor():
    editorName = input("Quel est le nom de l'éditeur ?\n")
    fondationYear = input("En quelle année l'éditeur a-t-il était créé ?\n")
    print(editorName + " " + fondationYear)
    ORM.editor_create(editorName, fondationYear)

def create_collection():
    collectionName = input("Comment s'appelle la collection ?\n")
    editor = input("Quel est l'éditeur de la collection ?\n")
    print (collectionName + " créé par " + editor)
    ORM.collection_create(collectionName, editor)

if __name__ == "__main__":
    print("1. Créer un éditeur")
    print("2. Créer une collection")

    option = input()

    if (option == "1") : create_editor()
    elif (option == "2") : create_collection()
    else : print("Option invalide")