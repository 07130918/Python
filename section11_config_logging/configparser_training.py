"""
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
port = 80

[db_server]
host = 127.0.0.1
port = 3306
"""
import configparser

config = configparser.ConfigParser()
print(config)
