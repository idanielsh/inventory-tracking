from typing import Optional
from pydantic import BaseModel
import uuid

class CreateInventoryItemParams(BaseModel):
    """
        This class parses the parameters sent in the POST request body when 
        creating a new Inventory Item
    """
    item: str
    manufacturer: str
    stock: int

class UpdateInventoryItemStock(BaseModel):
    """
        This class parses the parameters sent in the PATCH request body when 
        updating the inventory quantity
    """
    item_id: uuid.UUID
    stock: int

class UpdateInventoryItemInfo(BaseModel):
    """
        This class parses the parameters sent in the PUT request body when 
        updating the parameters of an inventory item
    """
    item_id: uuid.UUID
    item: Optional[str]
    manufacturer: Optional[str]
    stock: Optional[int]

