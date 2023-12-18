# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '21264686'))
    API_HASH = str(getenv('API_HASH', '395da72fd0c2022db5a8fccc5d28be5b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6981185660:AAGcTvIBZ4hbDtER0ZkX60snMETB4Jr_plI'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001826781136'))
    PORT = int(getenv('PORT', '80'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '20.24.189.224'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5049494041").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'BongoBondhuSheikhMujiburRahman'))
    if 'DYNO' in environ:
        ON_HEROKU = False
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '20.24.189.224:80')) if not ON_HEROKU or getenv('FQDN', '20.24.189.224:80') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Tomashsheg28383:9l6TQCDpZjndzlrh@cluster0.ibjitcd.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'BongoBondhu_bots'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
