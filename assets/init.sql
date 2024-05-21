CREATE TABLE IF NOT EXISTS pc (
    id INTEGER PRIMARY KEY,
    os TEXT
);

CREATE TABLE IF NOT EXISTS cpu (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    product TEXT,
    serial TEXT,
    freq TEXT,
    cache TEXT,
    pcid INTEGER,
    FOREIGN KEY(pcid) REFERENCES pc(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS gpu (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    product TEXT,
    serial TEXT,
    freq TEXT,
    memory TEXT,
    pcid INTEGER,
    FOREIGN KEY(pcid) REFERENCES pc(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ram (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    serial TEXT,
    speed TEXT,
    size TEXT,
    type TEXT,
    pcid INTEGER,
    FOREIGN KEY(pcid) REFERENCES pc(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS disk (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    serial TEXT,
    size TEXT,
    type TEXT,
    pcid INTEGER,
    FOREIGN KEY(pcid) REFERENCES pc(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS motherboard (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    model TEXT
);

CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY,
    Key1 TEXT,
    Key2 TEXT,
    Key3 TEXT
);
