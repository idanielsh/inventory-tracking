from fastapi import FastAPI
from datetime import datetime

from app.api.inventory_items import inventory_items

app = FastAPI()

deps = []
app.include_router(inventory_items.router, prefix='/api/inventory_items', dependencies=deps)


@app.get("/")
def root():
    return {"Server Time": datetime.now()}

