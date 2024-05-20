CREATE TABLE IF NOT EXISTS pc (
    id INTEGER PRIMARY KEY,
    os TEXT
)

CREATE TABLE IF NOT EXISTS cpu (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    product TEXT,
    freq TEXT,
    cache TEXT,
    pcid INTEGER,
    FOREIGN KEY(pcid) REFERENCES pc(id) ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS gpu (
    id INTEGER PRIMARY KEY,
    vendor TEXT,
    product TEXT,
    freq TEXT,
    memory TEXT,
    pcid INTEGER,
    FOREIGN KEY(pcid) REFERENCES pc(id) ON DELETE CASCADE
)


