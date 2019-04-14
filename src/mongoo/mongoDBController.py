'''
@ Class to create Mongo Connection
@
@
'''
import lib.pymongo.__init__ as pymongo

class MongoConnection :
    def __init__(self,connectOption) :
        self.url = connectOption.get("url")
        self.dbName = connectOption.get("dbName1")
        self.collectionName = connectOption.get("collectionName").get("rainfall")
        (self.connection, self.collection) = (None, None)
    def __del__(self) :
        (self.url, self.dbName, self.collectionName) = (None,None,None)
        (self.connection, self.collection) = (None,None)
        
    def start(self) :
        try:
            self.connection = pymongo.MongoClient(self.url)
            self.collection = self.connection[self.dbName][self.collectionName]
            print('established mongo connection')
        except Exception:
            print("Server not available: ", Exception)

    def end(self) :
        try:
            if(self.connection) :
                self.connection.close()
                self.collection = None
                print('closed mongo Connection')
        except Exception:
            print("Mongo Closed Problem: ", Exception)



'''
@ Class for Opertion in MongoDB
@
@
'''
import src.mongoo.config as config

class MongoRequest   :
    # @constructor
    def __init__(self,mongoCollection)  :
        self.mongoCollection = mongoCollection
        # print('\n\n\ncollection: ', self.mongoCollection)
        self.data = None
        self.sms = None

    # @destructor
    def __del__(self) :
        (self.mongoCollection, self.data, self.sms) = (None, None, None)
        
    ##
    # @method: store data in mongodb
    # @return 
    ##
    def postData(self, sheetData)    :
        (length, count, maxLimit,record) = (len(sheetData), 0, 1000,None)
        try:
            print('Total data: ',length)
            print('....data insert/update start....')
            for i in range(0, length)  :
                # print(("rainfall"+str(i)), sheetData[i].region.upper(), sheetData[i].year, sheetData[i].month.upper(), sheetData[i].data)           
                (fQuery,uQuery,iQuery) = config.postQuery(("rainfall"+str(i)), sheetData[i].region.upper(), sheetData[i].year, sheetData[i].month.upper(), sheetData[i].data)
                # print(fQuery,'\n',uQuery,'\n',iQuery)

                record = self.mongoCollection.find_one(fQuery)
                if(record is not None)  :
                    record = self.mongoCollection.update_one(fQuery,uQuery)
                else :
                    record = self.mongoCollection.insert_one(iQuery)

                if(record is not None)  :
                    # print(record)
                    count += 1
                    record = None
                if(count>0 and count%maxLimit==0)   :
                    print("..."+str(count)+" data inserted/update......")
            self.sms="\n----Insert "+str(count)+" Data Successfully----\n\n"
        except  Exception:
            print(Exception)
            return 'Faild To Mongo Connection'




def __main__(connectOption,requestType, dataQuery) :
    mPath = 'src/mongoo/mongoDBController.py'

    db = MongoConnection(connectOption)
    # establishded connection
    db.start()

    # -------------------------------------------
    ob = MongoRequest(db.collection)
    if(requestType == 'POST')   :
        ob.postData(dataQuery)
        return ob.sms
    else :
        return 'method not define : '+mPath
    # -------------------------------------------
    # closed connection
    db.end()
