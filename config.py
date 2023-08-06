from enum import StrEnum
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

ENVIRONMENT = os.environ["ENVIRONMENT"]

class Environemnt(StrEnum):
    DEVELOPMENT="development"
    PRODUCTION="production"

class DevelopmentConfig(object):
    ENVIRONMENT=os.environ["ENVIRONMENT"]
    WEBHOOK_VERIFY_TOKEN = os.environ["WEBHOOK_VERIFY_TOKEN"]
    WEBHOOK_MODE = os.environ["WEBHOOK_MODE"]
    HOST=os.environ["HOST"]
    PORT=os.environ["PORT"]

class ProductionConfig(object):
    ENVIRONMENT=os.environ["ENVIRONMENT"]
    WEBHOOK_VERIFY_TOKEN = os.environ["WEBHOOK_VERIFY_TOKEN"]
    WEBHOOK_MODE = os.environ["WEBHOOK_MODE"]
    HOST=os.environ["HOST"]
    PORT=os.environ["PORT"]
    
def load_config():
    match ENVIRONMENT:
        case Environemnt.DEVELOPMENT:
            return DevelopmentConfig
        case Environemnt.PRODUCTION:
            return ProductionConfig
        case _:
            return DevelopmentConfig