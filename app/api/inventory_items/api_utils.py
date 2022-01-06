from fastapi import HTTPException, status

def validate_record_exists(record):
    """
    Checks that the record is in the database and was not deleted
    """
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This inventory item could not be found")

def validate_record_valid(record):
    """
    Checks that the record has a positive value for stock
    """
    if record.stock < 0:
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail="Quantity of inventory must be positive")
