import configparser
config=configparser.ConfigParser()
config.read('conf/application.conf')

"""
MYSQL 
"""

host=config.get("MYSQL","host")
port=config.get("MYSQL",'port')
user=config.get("MYSQL","user")
password=config.get("MYSQL","password")
database=config.get("MYSQL","database")

# name_str=config.get("Names","name")
# print(name_str)




configu=configparser.ConfigParser()
configu.read('conf/application.conf')

"""
LOG Config
"""

LOG_LEVEL = configu.get('LOG', 'log_level', fallback="INFO")
LOG_BASEPATH = configu.get('LOG', 'base_path', fallback="logs/")
LOG_FILE_NAME = LOG_BASEPATH + configu.get('LOG', 'file_name', fallback='connected-worker')
LOG_HANDLERS = configu.get('LOG', 'handlers')
LOGGER_NAME = configu.get('LOG', 'logger_name')

# print(LOGGER_NAME)
