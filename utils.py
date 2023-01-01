import dotenv
import os
from config import config_homemachine, config_warmachine, config_common


def get_config():
    dotenv.load_dotenv(override=True)
    if os.environ.get('LOCATION') == 'home':
        config_user = config_homemachine
    elif os.environ.get('LOCATION') == 'vds':
        config_user = config_warmachine
    else:
        config_user = config_common
    return config_user
