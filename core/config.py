import imp
from starlette.config import Config

config = Config(".env")

EE_DATABASE_URL="postgresql://root:root@localhost:32700/employment_exchange"

DATABASE_URL = config("EE_DATABASE_URL", cast = str, default="")



ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="4c6fb866b97ce09de8d7f1f2f0b8cf455ca5ad933a53d684752a07435fb44c5d")