'''
@ Class to create Mongo Connection
@
@
'''
import pymongo.__init__ as pymongo
'''
@ class to established mongo-connection
'''
class MongoConnection :
    # @constructors
    def __init__(self,dbConfig,collectionOriginalName) :
        self.url = dbConfig.get("url")
        self.dbName = dbConfig.get("dbName1")
        self.collectionName = dbConfig.get("collectionName").get(collectionOriginalName)
        (self.connection, self.collection) = (None, None)
    # @destructors
    def __del__(self) :
        (self.url, self.dbName, self.collectionName) = (None,None,None)
        (self.connection, self.collection) = (None,None)
    # @db_start_connection
    def start(self) :
        try:
            self.connection = pymongo.MongoClient(self.url)
            self.collection = self.connection[self.dbName][self.collectionName]
            print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nestablished mongo connection\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        except Exception:
            print("Server not available: ", Exception)
    # @db_close_connection
    def end(self) :
        try:
            if(self.connection) :
                self.connection.close()
                self.collection = None
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nclosed mongo Connection\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        except Exception:
            print("Mongo Closed Problem: ", Exception)