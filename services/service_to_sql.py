from MySQLdb import connect
from fastapi import FastAPI
import requests
import uvicorn
# from pyodbc import connect
import  mysql.connector


"""
Connects to a SQL database using pyodbc
"""

mydb = mysql.connector.connect(
  host="mysql-app",
  user="dXNlcg==",
  password="cGFzc3dvcmQ="
)
mycursor = mydb.cursor()

mycursor.execute("select * from yyyy")
print(mydb)
for x in mycursor:
  print(x)

app = FastAPI()

BASE_URL = "http://mysql:8004"

class DAL:
    def __init__(self):
        self.user = "dXNlcg=="
        self.password = "cGFzc3dvcmQ="
        self.database = ""

    def connection_to_SQL(self):
        mydb = mysql.connector.connect(
            host="mysql-app",
            user="dXNlcg==",
            password="cGFzc3dvcmQ="
        )





@app.get("/get_from_sql")
def predict_all(request):
    conn = connect(
        user="dXNlcg==",
        password="cGFzc3dvcmQ=",
        host='localhost',
        database='travel')

    # mycursor = mydb.cursor()
    cursor = conn.cursor()
    query = 'SELECT plane_id, plane, max_weight FROM airplanes'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    print(mydb)
    return result.json()

conn = connect(
        user="dXNlcg==",
        password="cGFzc3dvcmQ=",
        host='localhost',
        database='travel')

cursor = conn.cursor()
query = ('SELECT plane_id, plane, max_weight FROM airplanes '
         'WHERE max_weight > 100000 '
         'ORDER BY max_weight DESC')
cursor.execute(query)
result = cursor.fetchall()

# print the results in each row
for r in result:
    print(r)

# close the cursor and database connection
cursor.close()
conn.close()

# catch exception and print error message

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8004,reload=True)
