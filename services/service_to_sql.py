from fastapi import FastAPI
import uvicorn
import mysql.connector


"""
Connects to a SQL database using pyodbc
"""


app = FastAPI()


@app.get("/get_from_sql")
def predict_all(request):
    mydb = mysql.connector.connect(
        host="mysql-app",
        user="bezalel",
        password="1234"
    )
    cursor = mydb.cursor()
    query = 'SELECT plane_id, plane, max_weight FROM airplanes'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    print(mydb)
    cursor.close()
    mydb.close()

    return result.json()


if __name__ == '__main__':
    uvicorn.run(app, host="mysql", port=8004)
