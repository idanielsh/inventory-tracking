from datetime import datetime
from typing import List
import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.sql import null
from sqlalchemy.sql.elements import Null


from app.api.inventory_items.network import CreateInventoryItemParams, UpdateInventoryItemInfo, UpdateInventoryItemStock
from app.database.database import DatabaseSession, Session
from app.entities.inventory_item import InventoryItemRecord, InventoryItem
from app.api.inventory_items.api_utils import validate_record_exists, validate_record_valid

router = APIRouter(dependencies=[])


@router.get("/", response_model=List[InventoryItem])
def get_all_inventory_items(all_items: bool = False, 
    db: Session = Depends(DatabaseSession)) -> List[InventoryItem]:
    if all_items:
        records = db.query(InventoryItemRecord)
    else:
        records = db.query(InventoryItemRecord).filter_by(deleted_at=None)

    return [InventoryItem.from_orm(record) for record in records.all()]


@router.get("/{item_id}", response_model=InventoryItem)
def get_inventory_item(item_id: uuid.UUID, 
    db: Session = Depends(DatabaseSession)) -> InventoryItem:

    record = db.query(InventoryItemRecord).get(item_id)
    validate_record_exists(record)

    return InventoryItem.from_orm(record)


@router.post("/", response_model=InventoryItem)
def create_inventory_item(
    params: CreateInventoryItemParams,
    db: Session = Depends(DatabaseSession)) -> InventoryItem:

    record = InventoryItemRecord(
        **params.dict()
    )
    validate_record_valid(record)

    db.add(record)
    db.commit()
    db.refresh(record)
    return InventoryItem.from_orm(record)


@router.put("/", response_model=InventoryItem)
def update_inventory_item_params(
    params: UpdateInventoryItemInfo,
    db: Session = Depends(DatabaseSession)) -> InventoryItem:
    
    record = db.query(InventoryItemRecord).with_for_update().get(params.item_id)
    validate_record_exists(record)

    if params.item:
        record.item = params.item
    if params.manufacturer:
        record.manufacturer = params.manufacturer
    if params.stock:
        record.stock = params.stock

    validate_record_valid(record)
    
    db.commit()
    db.refresh(record)

    return InventoryItem.from_orm(record)


@router.patch("/", response_model=InventoryItem)
def update_inventory_item_params(
    params: UpdateInventoryItemStock,
    db: Session = Depends(DatabaseSession)):

    temp_inventory_item = UpdateInventoryItemInfo()
    temp_inventory_item.item_id = params.item_id
    temp_inventory_item.stock = params.stock

    return update_inventory_item_params(temp_inventory_item)


@router.delete("/", response_model=InventoryItem)
def delete_inventory_item(
    item_id: uuid.UUID,
    delete_message: str = None,
    db: Session = Depends(DatabaseSession)):

    record = db.query(InventoryItemRecord).with_for_update().get(item_id)
    validate_record_exists(record)

    record.deleted_at = datetime.now()
    record.delete_note = delete_message

    db.commit()
    db.refresh(record)

    return InventoryItem.from_orm(record)


@router.delete("/undo", response_model=InventoryItem)
def undo_delete_inventory_item(
    item_id: uuid.UUID,
    db: Session = Depends(DatabaseSession)):

    record = db.query(InventoryItemRecord).with_for_update().get(item_id)
    print(record, item_id)
    validate_record_exists(record)

    record.deleted_at = None
    record.delete_note = None

    db.commit()
    db.refresh(record)

    return InventoryItem.from_orm(record)

