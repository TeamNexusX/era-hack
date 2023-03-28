import os

class Config(object):
    SECRET_KEY='qc8BhapYxRGr5gLrX-x2K9bbGXHtmhlgiPhK1PT_w6,EMvTv3n'

    SQLALCHEMY_DATABASE_URI='postgresql://admin:admin@database:5432/db'    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    JSONIFY_PRETTYPRINT_REGULAR = False
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False