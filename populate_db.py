import ORM

ORM.author_create('Nicolas', 'Dupuy')
ORM.editor_create('First', 2001)
ORM.collection_create('First', 'First')
ORM.book_create('Les 100 meilleurs albums de rock', '978-2-7540-1144-0', 2010, 'First', 'Nicolas', 'Dupuy')
ORM.collection_create('For Dummies', 'First')
ORM.author_create('Mark', 'Phillips')
ORM.author_create('Jon', 'Chappell')
ORM.book_create("La guitare pour les nuls", '2-75400-124-7', 2005, 'For Dummies', 'Mark', 'Phillips')
ORM.book_add_author('La guitare pour les nuls', 'Jon', 'Chappell')
ORM.book_create('Le Rock pour les nuls', '978-2-7540-0819-8', 2009, 'For Dummies', 'Nicolas', 'Dupuy')