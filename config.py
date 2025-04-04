class Config:
    SECRET_KEY = 'Tjd1fB1cQATaY9m2WAwfFxMuCHeCzw1PQ464wFO_i40'
    
    # Updated with full hostname, port, and SSL
    DATABASE_URL = 'postgresql://root:z59AS7H0sJJmytOuccSxP3YV4vFIevjO@dpg-cvnqa3buibrs73ac7lgg-a.oregon-postgres.render.com:5432/contact_db_asda?sslmode=require'
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'ZQeDOsFytKpJPlwUmapCcmVRhInyePv7AC0x2tvIUdKx4BhoPmIL6NB12CdSgu0EhdJN_yNYMloyTjCzbd6jZQ'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}