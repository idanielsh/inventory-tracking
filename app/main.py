from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()


@app.get("/")
def root():
    return {"Server Time": datetime.now()}
