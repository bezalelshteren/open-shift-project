from fastapi import FastAPI
import uvicorn
import mysql.connector

"""
Connects to a SQL database using pyodbc
"""

app = FastAPI()

@app.get("/get_from_sql")
def get_airplanes():
    mydb = mysql.connector.connect(
        host="mysql-service",
        user="root",
        password="1234",
        database="testdb"
    )
    cursor = mydb.cursor()
    query = "SELECT * FROM users;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return result


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8004)
