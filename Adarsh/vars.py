# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('21264686'))
    API_HASH = str(getenv('395da72fd0c2022db5a8fccc5d28be5b'))
    BOT_TOKEN = str(getenv('6981185660:AAGcTvIBZ4hbDtER0ZkX60snMETB4Jr_plI'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('-1001826781136'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('20.24.189.224', ''))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("5049494041", "").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('Filetolink'))
    OWNER_USERNAME = str(getenv('BongoBondhuSheikhMujiburRahman'))
    if 'DYNO' in environ:
        ON_HEROKU = False
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('20.24.189.224', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('mongodb+srv://Tomashsheg28383:9l6TQCDpZjndzlrh@cluster0.ibjitcd.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('BongoBondhu_bots', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
