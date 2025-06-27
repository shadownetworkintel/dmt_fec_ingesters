CREATE TABLE vendor_metadata (
    recipient_name TEXT PRIMARY KEY,       -- matches Schedule B recipient_name
    state TEXT,                            -- from Schedule B or registry
    legal_entity_name TEXT,                -- official business name in registry
    incorporation_date DATE,
    entity_type TEXT,                      -- LLC, Corp, etc.
    registered_agent TEXT,
    status TEXT,                           -- Active, Inactive, etc.
    source_url TEXT,                       -- where you found the info
    notes TEXT,
    last_checked TIMESTAMP DEFAULT now()
);