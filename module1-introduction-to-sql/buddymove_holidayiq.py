import pandas as pd
import sqlite3
df = pd.read_csv("buddymove_holidayiq.csv")
    #Just run once
#conn = df.to_sql('review', con=sqlite3.connect("buddymove_holidayiq.sqlite3"))
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

print('Objective one:')
count_rows = 'SELECT COUNT(*) FROM review;'
print("count of rows:", curs.execute(count_rows).fetchall())

print('Objective two:')
count_rows = (f"SELECT COUNT(*) "
                f"FROM review "
                f"where Nature = (select Nature from review where Nature > 100) AND "
                f"Shopping = (select Shopping from review where Shopping > 100) "
            )
print("count of >100 for Nature & Shopping:", curs.execute(count_rows).fetchall())