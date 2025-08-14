from fastapi import FastAPI
import requests
import uvicorn
import mysql.conector

app = FastAPI()


class DAL:
    def __init__(self):
        self.user = ""
        self.password = ""
        self.database = ""

    def connection_to_SQL(self):


@app.get("/get_from_sql")
def predict_all(request):
