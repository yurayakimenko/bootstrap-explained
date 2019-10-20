import configparser
import os

PROJECT_DIR = os.path.dirname(__file__)
CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(PROJECT_DIR, 'config/config.ini'))

DEBUG = True if CONFIG['settings']['debug'] == 'True' else False