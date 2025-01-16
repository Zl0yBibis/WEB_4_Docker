from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class WarehouseDB(BaseModel):
    id: int
    location: str

class ItemDB(BaseModel):
    id: int
    name: str

WAREHOUSE_DB = [
    WarehouseDB(id=1, location="Кукуево 13"),
    WarehouseDB(id=2, location="Кузнецово 3А"),
    WarehouseDB(id=3, location="Эзотерическая 42"),
]

ITEM_DB = [
    ItemDB(id=1, name="Диван Скуф"),
    ItemDB(id=2, name="Стол Стоялов"),
    ItemDB(id=3, name="Кресло Хакерман"),
]

@app.get("/")
async def root():
    return {"message": "Работа CRUD"}

@app.get("/warehouses", response_model=List[WarehouseDB])
def get_warehouses():
    return WAREHOUSE_DB

@app.get("/warehouses/{warehouse_id}", response_model=WarehouseDB)
def get_warehouse(warehouse_id: int):
    for warehouse in WAREHOUSE_DB:
        if warehouse.id == warehouse_id:
            return warehouse
    raise HTTPException(status_code=404, detail="Склад не найден")

@app.post("/warehouses", response_model=WarehouseDB)
def create_warehouse(warehouse: WarehouseDB):
    WAREHOUSE_DB.append(warehouse)
    return warehouse

@app.put("/warehouses/{warehouse_id}", response_model=WarehouseDB)
def update_warehouse(warehouse_id: int, warehouse: WarehouseDB):
    for idx, w in enumerate(WAREHOUSE_DB):
        if w.id == warehouse_id:
            WAREHOUSE_DB[idx] = warehouse
            return warehouse
    raise HTTPException(status_code=404, detail="Склад не найден")

@app.delete("/warehouses/{warehouse_id}")
def delete_warehouse(warehouse_id: int):
    for idx, w in enumerate(WAREHOUSE_DB):
        if w.id == warehouse_id:
            del WAREHOUSE_DB[idx]
            return {"detail": "Warehouse deleted"}
    raise HTTPException(status_code=404, detail="Склад не найден")

@app.get("/items", response_model=List[ItemDB])
def get_items():
    return ITEM_DB

@app.get("/items/{item_id}", response_model=ItemDB)
def get_item(item_id: int):
    for item in ITEM_DB:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Предмет не найден")

@app.post("/items", response_model=ItemDB)
def create_item(item: ItemDB):
    ITEM_DB.append(item)
    return item

@app.put("/items/{item_id}", response_model=ItemDB)
def update_item(item_id: int, item: ItemDB):
    for idx, it in enumerate(ITEM_DB):
        if it.id == item_id:
            ITEM_DB[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Предмет не найден")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, it in enumerate(ITEM_DB):
        if it.id == item_id:
            del ITEM_DB[idx]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Предмет не найден")
