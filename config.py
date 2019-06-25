class Config(object):
    SECRET_KEY = 'SOME SECRET STRING'
    MONGODB_DB = 'contacts_app'
    # TODO: change mongodb host to docker in prod
    MONGODB_HOST = '192.168.56.101'
    MONGODB_PORT = 27017
