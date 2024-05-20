# FOR TESTING NEW FUNCTIONS ONLY
# This script must be deleted when the final
# product is finished.
import os, sys

def get_db_path():
    if getattr(sys, 'frozen', False):
        # Compiled executable
        base_path = os.path.dirname(sys.executable)
    else:
        # Python script
        base_path = os.path.dirname(os.path.abspath(__file__))

    db_path = os.path.join(base_path, '..', '..', 'assets', 'inventory.db')

    db_path = os.path.abspath(db_path)
    
    return db_path

if __name__ == "__main__":
    print(get_db_path())
    input()
