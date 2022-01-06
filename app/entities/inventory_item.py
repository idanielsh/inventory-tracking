from typing import Optional
from app.database.database import Base
from datetime import datetime

import uuid
from sqlalchemy import Column, String, Integer, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.functions import now
from pydantic import BaseModel



class InventoryItemRecord(Base):
    __tablename__ = 'inventoryitems'
    __table_args__ = (
        CheckConstraint('stock >= 0'),
    )

    item_id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    item = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    delete_note = Column(String, nullable=True)


class InventoryItem(BaseModel):
    item_id: uuid.UUID
    item: str
    manufacturer: str
    stock: int
    created_at: datetime
    deleted_at: Optional[datetime]
    delete_note: Optional[str]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True