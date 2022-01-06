import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.inventory_items.network import CreateInventoryItemParams, UpdateInventoryItemInfo, UpdateInventoryItemStock

from app.database.database import DatabaseSession, Session
from app.entities.inventory_item import InventoryItemRecord, InventoryItem

router = APIRouter(dependencies=[])

@router.get("/")
def get_all_inventory_items(db: Session = Depends(DatabaseSession)):
    records = db.query(InventoryItemRecord).filter_by(deleted_at=None)

    return [InventoryItem.from_orm(record) for record in records.all()]

@router.get("/{item_id}")
def get_inventory_item(item_id: uuid.UUID, 
    db: Session = Depends(DatabaseSession)):
    pass


@router.post("/")
def create_inventory_item(
    params: CreateInventoryItemParams,
    db: Session = Depends(DatabaseSession)):

    pass

@router.put("/")
def update_inventory_item_params(
    params: UpdateInventoryItemInfo,
    db: Session = Depends(DatabaseSession)):
    
    pass

@router.patch("/")
def update_inventory_item_params(
    params: UpdateInventoryItemStock,
    db: Session = Depends(DatabaseSession)):

    pass

@router.delete("/")
def delete_inventory_item(
    item_id: uuid.UUID,
    delete_message: str = None,
    db: Session = Depends(DatabaseSession)):

    pass

@router.delete("/undo")
def undo_delete_inventory_item(
    item_id: uuid.UUID,
    db: Session = Depends(DatabaseSession)):

    pass
