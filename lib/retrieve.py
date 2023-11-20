from lib.IPMIConnector import IPMIConnector
from lib.database import DatabaseConnector


def retrieve():
    db = DatabaseConnector()
    if(db.check_if_exists()): 
        IPMIConnector().insert_data()
    else:
        DatabaseConnector().setup_database()
        IPMIConnector().insert_data()
