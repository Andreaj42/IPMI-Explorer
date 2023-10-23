from config.loader import load_variables

SCAN_INTERVAL = int(load_variables("SCAN_INTERVAL"))
IPMI_HOST = load_variables("IPMI_HOST")
IPMI_PORT = int(load_variables("IPMI_PORT"))
IPMI_USER = load_variables("IPMI_USER")
IPMI_PASSWORD = load_variables("IPMI_PASSWORD")
INFLUX_HOST = load_variables("INFLUX_HOST")
INFLUX_PORT = int(load_variables("INFLUX_PORT"))