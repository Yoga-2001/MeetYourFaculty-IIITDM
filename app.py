from flask import Flask, render_template, request, jsonify, flash, redirect, session, abort
from pymysql import connect

app = Flask(__name__)

def dbconnect(sql):
   result = []
   db = connect(host='remotemysql.com', database='qTmJH8lRK0', user='qTmJH8lRK0', password='74MQEDNu42')
   cursor = db.cursor()
   cursor.execute(sql)
   db.commit()
   for i in cursor.fetchall():
      result.append(i)
   cursor.close()
   return result

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/slots')
def slots():
   sql = "select * from monday"
   res = dbconnect(sql)
   print(res)
   return str(res)

if __name__ == '__main__':
   app.run()