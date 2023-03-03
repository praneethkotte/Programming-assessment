import sqlite3
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:    
    @app.route('/')
    def index():
        # open the connection to the database
        conn = sqlite3.connect('datausa.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from country_details")
        rows = cur.fetchall()
        conn.close()
        return render_template('index.html', rows=rows)
except ExceptionType:
    print("Not able to form the table")

finally:
    if __name__=='__main__':
        app.run(host='0.0.0.0', debug=True)