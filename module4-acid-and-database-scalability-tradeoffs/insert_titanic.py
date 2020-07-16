
import psycopg2
#import pandas

dbname = 'oxnndimc'
user = 'oxnndimc'  # ElephantSQL chooses to reuse dbname and username
password = 'ac62NvUdHTIbBcDEjAvg3pOA2Swm1xaV'
host = 'ruby.db.elephantsql.com'  # Port is default 5432

pg_conn = psycopg2.connect(dbname= dbname, user= user, password= password, host= host)
pg_curs = pg_conn.cursor()

#----------------------------------------------------------------------------
# Objective two
#----------------------------------------------------------------------------
import sqlite3
import pandas as pd

df = pd.read_csv("titanic.csv")
df.rename(columns={'Siblings/Spouses Aboard':'Siblings_Spouses_Aboard',
                          'Parents/Children Aboard':'Parents_Children_Aboard'}, 
                 inplace=True)

df['Name'] = df['Name'].str.replace("'", "")
    #Just run single line below once
#conn = df.to_sql('titanic', con=sqlite3.connect("titanic.sqlite3"))

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()


sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

get_table = 'SELECT * FROM titanic;'
table = sl_curs.execute(get_table).fetchall()

#print(sl_curs.execute('PRAGMA table_info(titanic);').fetchall())

#make create statement for PostgreSQL that captures these types
"""
create_titanic_table = '''
CREATE TABLE titanicmod4 (
    index SERIAL PRIMARY KEY,
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
    INSERT INTO titanicmod4
    (index, Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES ''' + str(row[0:]) + ";"
    pg_curs.execute(insert_row)

pg_curs.execute('SELECT * FROM titanicmod4 LIMIT 5;')
print(pg_curs.fetchall())
pg_conn.commit()
"""

survive_or_die = """SELECT COUNT(Survived) FROM titanic
                    GROUP BY Survived;"""
print("passengers who died and survived:", curs.execute(survive_or_die).fetchall())


in_each_pclass = """SELECT COUNT(Pclass) FROM titanic
                    GROUP BY Pclass;"""
print("How many passengers were in each class? 1-3", curs.execute(in_each_pclass).fetchall())

surv_each_pclass = """SELECT pclass, SUM(survived)
                    FROM titanic
                    GROUP BY pclass;
                    """
print("How many passengers survived/died within each class?", curs.execute(surv_each_pclass).fetchall())

avg_age_surv = """SELECT Survived, AVG(Age)
                    FROM titanic
                    GROUP BY Survived;
                    """
print("What was the average age of survivors vs nonsurvivors?", curs.execute(avg_age_surv).fetchall())

avg_age_pclass = """SELECT Pclass, AVG(Age)
                    FROM titanic
                    GROUP BY Pclass;
                    """
print("What was the average age of each passenger class?", curs.execute(avg_age_pclass).fetchall())

avg_fare_pclass = """SELECT Pclass, AVG(Fare)
                        FROM titanic
                        GROUP BY Pclass;
                    """
avg_fare_surv = """SELECT Survived, AVG(Fare)
                        FROM titanic
                        GROUP BY Survived;
                    """
print("What was the average fare by passenger class?", curs.execute(avg_fare_pclass).fetchall())
print("What was the average fare by survival?", curs.execute(avg_fare_surv).fetchall())

avg_sib_pclass = """SELECT Pclass, AVG(Siblings_Spouses_Aboard)
                        FROM titanic
                        GROUP BY Pclass;
                    """
avg_sib_surv = """SELECT Survived, AVG(Siblings_Spouses_Aboard)
                        FROM titanic
                        GROUP BY Survived;
                    """
print("How many siblings/spouses aboard on average, by passenger class?", curs.execute(avg_sib_pclass).fetchall())
print("How many siblings/spouses aboard on average, by survival? ", curs.execute(avg_sib_surv).fetchall())


dupl_name = """SELECT Name, COUNT(Name) 
                    FROM titanic
                    GROUP BY Name
                    HAVING COUNT(Name) > 1
                    """

print("Do any passengers have the same name? ", curs.execute(dupl_name).fetchall())