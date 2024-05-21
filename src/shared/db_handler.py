import os, sqlite3
from utils import get_ordered_data, get_assets_path, read_text_file

## Database connection management => START
def open_connection(db_name='inventory.db'):
    db_path = os.path.join(get_assets_path(), db_name)
    conn = sqlite3.connect(db_path)
    return conn

def close_connection(connection):
    connection.commit()
    connection.close()
## Database connection management => END

## Database inicialization => START
def init_db():
    connection = open_connection() # Uses default db name
    run_sql_script('init.sql', connection)
    close_connection(connection)
## Database inicialization => END

## Run SQL scripts => START
def run_sql_script(sql_name, connection):
    sql_path = os.path.join(get_assets_path(), sql_name)
    cursor = connection.cursor()
    cursor.executescript(read_text_file(sql_path))
## Run SQL scripts => END

## Direct SQL administration => START
### INSERT => START
def db_insert_single(table, data_dict):
    connection = open_connection()
    cursor = connection.cursor()
    keys = tuple(data_dict.keys())
    sql_instruction = f"INSERT INTO {table} {keys} VALUES ({''.join('?, ' for x in range(len(keys) - 1))}?)"
    cursor.execute(sql_instruction, tuple(data_dict[key] for key in keys))
    close_connection(connection)

def db_insert_massive(table, data_matrix_dict):
    connection = open_connection()
    cursor = connection.cursor()
    keys, data = get_ordered_data(data_matrix_dict)
    sql_instruction = f"INSERT INTO {table} {keys} VALUES ({''.join('?, ' for x in range(len(keys) - 1))}?)"
    cursor.executemany(sql_instruction, data)
    close_connection(connection)
### INSERT => END
## Direct SQL administration => END
