import csv
import sqlite3

# connecting the database
conn = sqlite3.connect('datausa.db')
cur = conn.cursor()

#setting up the countries I want
countries = ["United States"]
 

#not repeating the values even if we rerun the same file after droping the data
cur.execute('DROP TABLE IF EXISTS country_details')
cur.execute('DROP TABLE IF EXISTS Meta_details')
print("tables dropped successfully");
# create table
cur.execute(
    'CREATE TABLE country_details ( ID INTEGER PRIMARY KEY AUTOINCREMENT, Country_Code TEXT NOT NULL,INDICATOR_CODE TEXT NOT NULL)')
cur.execute(
    'CREATE TABLE Meta_details ( ID INTEGER PRIMARY KEY AUTOINCREMENT, INDICATOR_CODE TEXT NOT NULL, INDICATOR_NAME TEXT NOT NULL,SOURCE_NOTE TEXT NOT NULL)')
print("tables created successfully");

#importing the content of file into the data base
with open('datasets/API_USA_DS2_en_csv_v2_4782210.csv',
          newline='') as f:
    reader = csv.reader(f, delimiter=",")
    for i in range(1,6):
        next(reader)  # skip the first five lines
    for row in reader:
        print(row)
        Country_Code = row[1]
        INDICATOR_CODE = row[3]

        cur.execute('INSERT INTO country_details VALUES(NULL,?,?)',
                    (Country_Code, INDICATOR_CODE))
        conn.commit()

with open('datasets/Metadata_Indicator_API_USA_DS2_en_csv_v2_4782210.csv',
          newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip the header line
    for row in reader:
        print(row)
        
        INDICATOR_CODE = row[0]
        INDICATOR_NAME = row[1]
        SOURCE_NOTE = row[2]

        cur.execute('INSERT INTO Meta_details VALUES (NULL,?,?,?)',
                    (INDICATOR_CODE, INDICATOR_NAME, SOURCE_NOTE))
        conn.commit()
print("data parsed successfully");
conn.close()
