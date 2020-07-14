import pandas as pd
import sqlite3
df = pd.read_csv("buddymove_holidayiq.csv")
df.to_sql('review', con=sqlite3.Connection)
conn = sqlite3.connect('review')
curs = conn.cursor()
#I will finish this part 2 tomorrow