import requests
import sqlite3
import csv

url = "https://storage.googleapis.com/play_public/supported_devices.csv"


con = sqlite3.connect('android_market_names.db')
cur = con.cursor()
cur.execute(
    'DROP TABLE IF EXISTS marketnames;')
cur.execute(
    'CREATE TABLE marketnames(retail_branding text,market_name text,device text,model text);')

with requests.get(url) as r:
    reader = csv.reader(r.content.decode('utf16').split('\n'))
    # skip first row with names
    for row in list(reader)[1:-1]:
        if row:
            cur.execute(
                'INSERT INTO marketnames(retail_branding,market_name,device,model) VALUES (?, ?, ?, ?);', row)

cur.execute('select count(*) from marketnames;')
print('Database size:')
print(cur.fetchone())

con.commit()
con.close()
