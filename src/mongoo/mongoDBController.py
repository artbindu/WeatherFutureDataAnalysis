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
    ##
    # @method: fetch data from mongodb
    ##
    def deleteData(self)    :
        mongoQuery = config.deleteQuery()
        self.data = self.mongoCollection.remove()
        # print(self.data)
        if(self.data['ok'] == 1.0 and self.data['n'] > 0) :
            self.sms = ('successfully clear ',self.data['n'],' from collection: ')
        else :
            self.sms = ('empty collection')

    ##
    # @method: fetch specific data from mongodb
    # @calling 'custom'
    # @mongoQuery: JSON type
    # @return mongoQuery data in array format [[region,year,month,data],[],[],...]
    ##
    def getData(self, mongoQuery)   :
        self.data = self.mongoCollection.find(mongoQuery)
        count = self.data.count()
        if(count==0) :
            self.data = None
        else :
            arrData = self.convertJson2Array()
            (self.data, self.sms) = (arrData, "get data successfully")
    ##
    # @ use to convert mongoJSON data to array list
    ##
    def convertJson2Array(self) :
        array = []
        temp = ['REGION','YEAR','MONTH','DATA']
        array.append(temp)
        for x in self.data :
            if(len(x)>0) :
                temp = []
                temp.append(x['REGION'])
                temp.append(x['YEAR'])
                temp.append(x['MONTH'])
                temp.append(x['DATA'])
            array.append(temp)
        if(len(array)>1) :
            return array
        else :
            return None

"""
@ Main function 
@
@
"""
def __main__(connectOption,requestType, dataQuery=None) :
    mPath = 'src/mongoo/mongoDBController.py'
    try :
        db = MongoConnection(connectOption)
        # establishded connection
        db.start()

        # -------------------------------------------
        try :
            ob = MongoRequest(db.collection)
            if(requestType == "POST")   :
                ob.postData(dataQuery)
                return ob.sms
            elif(requestType == "DELETE")   :
                ob.deleteData()
                return ob.sms
            elif(requestType == "GET") :
                ob.getData(dataQuery)
                return (ob.data, ob.sms)
            else :
                return 'method not define : '+mPath
        except AttributeError:
            print('AttributeError : '+mPath)
        # -------------------------------------------

        # closed connection
        db.end()
    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)
