import os
from datetime import timedelta

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f"sqlite:///{os.path.join(BASE_DIR, 'mesero_virtual_db.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_URL_APP = os.environ.get('BASE_URL_APP','http://localhost:5000')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi-clave_firmatokensqr')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'meseroclavefirmoTokensJWT')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)