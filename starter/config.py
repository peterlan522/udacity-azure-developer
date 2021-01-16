import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'my-sql-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'my-sql-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'myadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Whateverpwd123'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'anotherstorageaccount11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'Ch0N27Gh6qzUlekl5TxakgZ6s42zRQ0IgvSKoqD8zpEhhzL4Za1SVN/OBKejBUn9QATWwaIrbjkBcFx+LqhWmg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'image'
