from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe5\x17\xc2\x9d\x0c1!\x90\x0c\xde\x1d\xcb\xccV\xd96'
