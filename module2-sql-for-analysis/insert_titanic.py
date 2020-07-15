
import psycopg2
#import pandas

dbname = 'oxnndimc'
user = 'oxnndimc'  # ElephantSQL chooses to reuse dbname and username
password = 'ac62NvUdHTIbBcDEjAvg3pOA2Swm1xaV'
host = 'ruby.db.elephantsql.com'  # Port is default 5432

pg_conn = psycopg2.connect(dbname= dbname, user= user, password= password, host= host)
pg_curs = pg_conn.cursor()

#----------------------------------------------------------------------------
# Following section is tutorial, and not assignment related
#----------------------------------------------------------------------------

'''
create_table_statement = """
CREATE TABLE test_table2 (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_conn.commit()


#now to insert


insert_statement = """
INSERT INTO test_table2 (name, data) VALUES
(
    'a row name',
    null
),
(
    'another row name with JSON this time',
    '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
)
"""

pg_curs.execute(insert_statement)
pg_conn.commit()


query = 'SELECT * FROM test_table2;'
pg_curs.execute(query)
print(pg_curs.fetchall())
'''

#----------------------------------------------------------------------------
# Objective one
#----------------------------------------------------------------------------
#delete double quotes on top and bottom to operate code


import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

#make create statement for PostgreSQL that captures these types
create_character_table = '''
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
'''
#uncomment to save table and insert
'''

pg_curs = pg_conn.cursor()
pg_curs.execute(create_character_table)
pg_conn.commit()


for character in characters:
    insert_character = '''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES ''' + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

'''

pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
print(pg_curs.fetchall())
pg_conn.commit()



#----------------------------------------------------------------------------
# Objective two
#----------------------------------------------------------------------------
import sqlite3
import pandas as pd

df = pd.read_csv("titanic.csv")
df.rename(columns={'Siblings/Spouses Aboard':'Siblings_Spouses_Aboard',
                          'Parents/Children Aboard':'Parents_Children_Aboard'}, 
                 inplace=True)
    #Just run single line below once
#conn = df.to_sql('titanic', con=sqlite3.connect("titanic.sqlite3"))

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()


sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

get_table = 'SELECT * FROM titanic;'
table = sl_curs.execute(get_table).fetchall()

print(sl_curs.execute('PRAGMA table_info(titanic);').fetchall())

#make create statement for PostgreSQL that captures these types

create_titanic_table = '''
CREATE TABLE titanic6 (
    index INT,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare REAL
);
'''

#uncomment to save table and insert


pg_curs = pg_conn.cursor()
pg_curs.execute(create_titanic_table)
pg_conn.commit()


for row in table:
    insert_row = '''
    INSERT INTO titanic6
    (index, Survived, Pclass, Name, Sex, Age,
     Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES ''' + str(row[0:]) + ";"
    pg_curs.execute(insert_row)



pg_curs.execute('SELECT * FROM titanic6 LIMIT 5;')
print(pg_curs.fetchall())
pg_conn.commit()
#TODO: change names of passengers to work in insert