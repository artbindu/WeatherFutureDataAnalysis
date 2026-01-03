'''
@ Class for different Operations in MongoDB
@ operation are: POST(insert data in db), GET(fetch data from db), DELETE(delete data from db)
'''
import src.share.utils.dbUtils as dbUtils

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
                (fQuery,uQuery,iQuery) = dbUtils.MongoDBUtils.postQuery(("rainfall"+str(i)), sheetData[i].region.upper(), sheetData[i].year, sheetData[i].month.upper(), sheetData[i].data)
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
                    print("..."+str(count)+" data inserted/updated......")
            print('....data insert/update complete....')
            self.sms="----Inserted/updated "+str(count)+" Data Successfully----"
        except Exception as e:
            print(type(e).__name__, ':', e)
            print('Failed To Mongo Data Insert')
            self.sms = None

    ##
    # @method: fetch data from mongodb
    ##
    def deleteData(self)    :
        try :
            mongoQuery = dbUtils.MongoDBUtils.deleteQuery()
            # Use delete_many instead of deprecated remove()
            self.data = self.mongoCollection.delete_many({})
            # print(self.data)
            if(self.data.deleted_count > 0) :
                self.sms = ('successfully clear ',self.data.deleted_count,' from collection: ')
            else :
                self.sms = ('empty collection')
        except Exception as e:
            print(type(e).__name__, ':', e)
            print('Failed To Mongo Data Delete')
            self.sms = None

    ##
    # @method: fetch specific data from mongodb
    # @calling 'custom'
    # @mongoQuery: JSON type
    # @return mongoQuery data in array format [[region,year,month,data],[],[],...]
    ##
    def getData(self, mongoQuery)   :
        try :
            (self.data,self.sms) = (None,None)
            self.data = self.mongoCollection.find(mongoQuery)
            # Use count_documents instead of deprecated count()
            count = self.mongoCollection.count_documents(mongoQuery)
            if(count==0) :
                (self.data,self.sms) = (None,None)
            else :
                arrData = self.convertJson2Array()
                (self.data, self.sms) = (arrData, "get data successfully")
        except Exception as e:
            print(type(e).__name__, ':', e)
            print('Failed To Mongo Data Fetch')
            self.sms = None

    ##
    # @method: update data use for filtering
    ##
    def updateData(self, data) :
        try :
            for x in data :
                (fQuery,uQuery,iQuery) = dbUtils.MongoDBUtils.postQuery(None, x[0],x[1],x[2],x[3])
                # print('findQuery', fQuery, 'updateQuery', uQuery)
                record = self.mongoCollection.find_one(fQuery)
                if(record is not None)  :
                    record = self.mongoCollection.update_one(fQuery,uQuery)
        except Exception as e:
            print(type(e).__name__, ':', e)
            print('Failed To Mongo Data Update')
            self.sms = None

    ##
    # @method to get a attributes distinct data
    ##
    def getDistinctData(self, mongoQuery) :
        try :
            self.data = self.mongoCollection.distinct(str(mongoQuery))
            self.sms = "get data successfully"
        except Exception as e:
            print(type(e).__name__, ':', e)
            print('Failed To Mongo Distinct Data Fetch')
            self.sms = None

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
