# FOR TESTING NEW FUNCTIONS ONLY
# This script must be deleted when the final
# product is finished.
#from utils import get_ordered_data
from db_handler import db_insert_single

def test():
    data = {
        "Key1": "single4",
        "Key2": "single5",
        "Key3": "single6"
    }
    db_insert_single("test", data)
    text = "Data inserted. Please verify."
    return text

if __name__ == "__main__":
    print(test())
    input()
