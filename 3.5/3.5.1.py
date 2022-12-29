import pandas as pd
import sqlite3

conn = sqlite3.connect('3.5.1.sqlite')
c = conn.cursor()
df = pd.read_csv('currencies.csv')
df = df.to_sql('currencies', conn, if_exists='replace', index=False)
conn.commit()