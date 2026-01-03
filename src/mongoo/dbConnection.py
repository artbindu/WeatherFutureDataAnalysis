'''
@ Class to create Mongo Connection
'''
import pymongo.__init__ as pymongo
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

'''
@ class to established mongo-connection
'''
class MongoConnection :
    # @constructors
    def __init__(self,dbConfig,collectionOriginalName) :
        self.url = dbConfig.get("url")
        self.dbName = dbConfig.get("dbName")
        self.collectionName = dbConfig.get("collectionName").get(collectionOriginalName)
        self.timeouts = dbConfig.get("timeouts", {
            "serverSelectionTimeoutMS": dbConfig.get("serverSelectionTimeoutMS"),
            "connectTimeoutMS": dbConfig.get("connectTimeoutMS"),
            "socketTimeoutMS": dbConfig.get("socketTimeoutMS")
        })
        (self.connection, self.collection) = (None, None)
        self.line = '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

    # @destructors
    def __del__(self) :
        (self.url, self.dbName, self.collectionName) = (None,None,None)
        (self.connection, self.collection) = (None,None)

    # @db_start_connection
    def start(self) :
        try:
            # Add mongodb:// prefix if not present
            url = self.url if self.url.startswith('mongodb://') else f'mongodb://{self.url}'
            
            # Connect with timeout settings from config
            self.connection = pymongo.MongoClient(
                url,
                **self.timeouts
            )
            
            # Test the connection
            self.connection.admin.command('ping')
            
            self.collection = self.connection[self.dbName][self.collectionName]
            print(self.line+'     established mongo connection'+self.line)
        except ServerSelectionTimeoutError as e:
            print(f"MongoDB Server not available: {str(e)}")
            print("Please ensure MongoDB is running on", self.url)
        except ConnectionFailure as e:
            print(f"MongoDB Connection failed: {str(e)}")
        except Exception as e:
            print(f"MongoDB Connection error: {str(e)}")

    # @db_close_connection
    def end(self) :
        try:
            if(self.connection) :
                self.connection.close()
                self.collection = None
                print(self.line+'\tclosed mongo Connection'+self.line)
        except Exception as e:
            print(f"MongoDB Close error: {str(e)}")