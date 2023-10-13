import os


class Config(object):
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mon_projet.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
