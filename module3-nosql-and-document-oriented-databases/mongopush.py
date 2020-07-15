import pymongo

client = pymongo.MongoClient("mongodb://beanbagthomas:<password>@cluster0-shard-00-00.yiqb7.mongodb.net:27017,cluster0-shard-00-01.yiqb7.mongodb.net:27017,cluster0-shard-00-02.yiqb7.mongodb.net:27017/test?ssl=true&replicaSet=atlas-12kh1k-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
"""

print(db.test.count_documents({'x' : 1}),'\n')

db.test.insert_one({'x': 1})
print(db.test.count_documents({'x' : 1}),'\n')


print(db.test.find_one({'x': 1}),'\n')

curs = db.test.find({'x' : 1})

print(list(curs),'\n')


byrnes_doc = {
    'animal': 'manatee',
    'color': 'green',
    'number': 7
}

daves_doc = {
    'animal': 'bat',
    'color': 'red',
    'number': 1000
}

sasanas_doc = {
    'animal': 'orca',
    'color': 'blue',
    'number': 9
}

tylers_doc = {
    'animal': 'hippogryph',
    'cities': ['New York', 'Houston']
}

walters_doc = {
    'color': 'chartreuse',
    'animal': 'platypus'
}

aarons_doc = {
    'inner_dict': {
        'x': 2,
        'y': -4,
        'z': 'banana'
    },
    'another_key': (2, 6, 3)
}

all_docs = [byrnes_doc, daves_doc, sasanas_doc, tylers_doc, walters_doc,
            aarons_doc]

db.test.insert_many(all_docs)

print(list(db.test.find()),'\n')

print(db.test.find_one({'color': 'green'}),'\n')

db.test.insert_one({
    'animal': 'tiger',
    'color': 'green',
    'city': 'Paris'
})

print(db.test.find_one({'color': 'green'}),'\n')

print(list(db.test.find({'color': 'green'})),'\n')

more_docs = []
for i in range(10):
  doc = {'even': i % 2 == 0}
  doc['value'] = i
  more_docs.append(doc)
  
print(more_docs)

db.test.insert_many(more_docs)

"""
#------------------------------------------------------
#assignment
#------------------------------------------------------
import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

all_docs2 = []
for character in characters:
    dictionary = {}
    print(character[0])
    dictionary.update( {'character_id' : character[0]})
    dictionary.update( {'name' : character[1]})
    dictionary.update( {'level' : character[2]})
    dictionary.update( {'exp' : character[3]})
    dictionary.update( {'hp' : character[4]})
    dictionary.update( {'strength' : character[5]})
    dictionary.update( {'intelligence' : character[6]})
    dictionary.update( {'dexterity' : character[7]})
    dictionary.update( {'wisdom' : character[8]})
    all_docs2.append(dictionary)

db.test.insert_many(all_docs2)


"""
MongoDB was different in its reliant on the insert one and insert many.
I think mongoDB was easier to be honest because I like not having to set up 
a table first with half SQL terms, I much more enjoyed creating a dictionary and sending it straight to mongo. 
I like its availabilty to kinda just jam in whatever. PostgreSQL was just too picky for me.
"""
