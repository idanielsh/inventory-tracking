DROP TABLE IF EXISTS InventoryItems CASCADE;

CREATE TABLE InventoryItems (
    item_id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    item VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255) NOT NULL,
    stock INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMP,
    delete_note TEXT
);