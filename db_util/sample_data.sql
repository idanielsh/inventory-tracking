INSERT INTO InventoryItems 
    (item, manufacturer, stock)
    VALUES (
        'Monitor',
        'Dell',
        13
    );

INSERT INTO InventoryItems 
    (item, manufacturer, stock)
    VALUES (
        'MacBook Pro',
        'Apple',
        100
    );
    
INSERT INTO InventoryItems 
    (item, manufacturer, stock)
    VALUES (
        'Charger',
        'Apple',
        143
    );
    
INSERT INTO InventoryItems 
    (item, manufacturer, stock)
    VALUES (
        'MacBook Air',
        'Apple',
        28
    );
    
INSERT INTO InventoryItems 
    (item, manufacturer, stock, deleted_at, delete_note)
    VALUES (
        'Surface Pro 3',
        'Microsoft',
        0,
        now() + '1 week'::interval,
        'Old sold inventory of Surface Pro 3''s that were sold to another company' 
    );