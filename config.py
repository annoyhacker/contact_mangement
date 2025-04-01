import os

class Config:
    SECRET_KEY = 'Tjd1fB1cQATaY9m2WAwfFxMuCHeCzw1PQ464wFO_i40'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:ADMIN@localhost/contact_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'ZQeDOsFytKpJPlwUmapCcmVRhInyePv7AC0x2tvIUdKx4BhoPmIL6NB12CdSgu0EhdJN_yNYMloyTjCzbd6jZQ'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}