import os

class Config:
    SECRET_KEY = 'Tjd1fB1cQATaY9m2WAwfFxMuCHeCzw1PQ464wFO_i40'

    DATABASE_URL= 'postgresql://root:rL0HhK3RVJZdxDr16YNhoJbN4jVgoYyJ@dpg-cvmnepe3jp1c73dv6ab0-a/test_contact_manger'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'ZQeDOsFytKpJPlwUmapCcmVRhInyePv7AC0x2tvIUdKx4BhoPmIL6NB12CdSgu0EhdJN_yNYMloyTjCzbd6jZQ'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}