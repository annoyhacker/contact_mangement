class Config:
    SECRET_KEY = 'Tjd1fB1cQATaY9m2WAwfFxMuCHeCzw1PQ464wFO_i40'
    
    # Updated with full hostname, port, and SSL
    DATABASE_URL = 'postgresql://root:4kZbymLdxzHN4LrP33ePnN3u9ebe9iQq@dpg-d0ip5l3e5dus739r78e0-a.oregon-postgres.render.com/test_contactdb'
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'ZQeDOsFytKpJPlwUmapCcmVRhInyePv7AC0x2tvIUdKx4BhoPmIL6NB12CdSgu0EhdJN_yNYMloyTjCzbd6jZQ'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}