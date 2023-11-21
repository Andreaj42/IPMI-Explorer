from config.loader import load_variables

SCAN_INTERVAL = int(load_variables("SCAN_INTERVAL"))
IPMI_HOST = load_variables("IPMI_HOST")
IPMI_PORT = int(load_variables("IPMI_PORT"))
IPMI_USER = load_variables("IPMI_USER")
IPMI_PASSWORD = load_variables("IPMI_PASSWORD")
DB_HOST = load_variables("DB_HOST")
DB_PORT = int(load_variables("DB_PORT"))
DB_USER = load_variables("DB_USER")
DB_PASSWORD = load_variables("DB_PASSWORD")
SERVER_NAME = load_variables("SERVER_NAME")