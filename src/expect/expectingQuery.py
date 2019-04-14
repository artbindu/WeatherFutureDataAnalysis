import src.expect.clientQuery as clientQuery
import src.expect.config as config

class ExpectingQuery :
    def __init__(self) :
        (self.cQuery, self.mQueryApproch0, self.mQueryApproch1, self.mQueryApproch2) = (None, None, None, None)
        # generate cQuery througth constructor
        try :
            self.cQuery = clientQuery.__main__()
            # print('\n\n\n self.cQuery = ',self.cQuery)

            # generate 'mQueryApproch0' through constructor
            self.mQueryApproch0 = self.generateMongoQuery_OriginalData()
            # print('\n\n\n self.mQueryApproch0 = ',self.mQueryApproch0)
            
            # generate 'mQueryApproch1' through constructor
            self.mQueryApproch1 = self.generateMongoQuery_Approch1()
            # print('\n\n\n self.mQueryApproch1 = ',self.mQueryApproch1)

            # generate 'mQueryApproch2_Backword' through constructor :: all db data(1951-2018)
            self.mQueryApproch2 = self.generateMongoQuery_Approch2('backword')
            # print('\n\n\n self.mQueryApproch2 = ',self.mQueryApproch2)
            
            print("\n\n*********************\n\n")
        except AttributeError :
            print('AttributeError')
        except TypeError:
            print('TypeError : ')
        except Exception :
            print('error class ExpectingQuery().__init__()')

    def __del__(self) :
        (self.cQuery, self.mQueryApproch0, self.mQueryApproch1, self.mQueryApproch2) = (None, None, None, None)
       
    # -------generate mongoQuery if year<2018 -----------------
    def generateMongoQuery_OriginalData(self) :
        query = None
        if(self.cQuery[1]<2018) :
            if(len(self.cQuery)==2) :
                return config.createMongoQuery_ForOriginalData(self.cQuery[0],self.cQuery[1])
            elif(len(self.cQuery)==3) :
                return config.createMongoQuery_ForOriginalData(self.cQuery[0],self.cQuery[1],self.cQuery[2])
        elif(len(self.cQuery)==3 and self.cQuery[1]>=2018) :
            return config.createMongoQuery_ForOriginalData(self.cQuery[0],2017,self.cQuery[2])
        return query


    # -------generate MongoQuery with first ANN approach-------
    def generateMongoQuery_Approch1(self)    :
        (qType, mQuery) = (config.queryType(self.cQuery), [])
        
        # [ 'region', year, 'month'] = ['BIHAR', 2018, 'MARCH'] :: search all year Region-Month
        if(qType == "<class 'str'><class 'int'><class 'str'>") : 
            mQuery.append(self.generateQuery1(self.cQuery))
            return(mQuery)
        # [ 'region', year] = ['BIHAR', 2018]  ::  search by Region, Year(with all Month)
        elif(qType == "<class 'str'><class 'int'>") :
            for i in range(0, 12) :
                arr = [self.cQuery[0],self.cQuery[1],config.month_number_to_string(i)]
                mQuery.append(self.generateQuery1(arr))
            return(mQuery)
        # for other query
        else :
            print('----invalid query----')
            return None
    def generateQuery1(self, arr) :
        return config.createMongoQueryANN1(arr[0],arr[1],arr[2])

    # -------generate MongoQuery with second ANN approch-------
    # -------here we picup all data from database-------------
    def generateMongoQuery_Approch2(self,option) :
        print('come to fetch all data .........')
        (query,mQuery, isQueryForLastPart,sms) = (None, [], False,None)
        # cQuery = ['REGION', 'YEAR'] / ['REGION', 'YEAR', 'MONTH']
        if(option=='backword') :
            # ---if QueryYear >2017 --------
            if(len(self.cQuery)==2 and self.cQuery[1]>2017) :
                (fYear,fMonth) = (2017,'DECEMBER')
            elif(len(self.cQuery)==2 and self.cQuery[1]<=2017) :
                (fYear,fMonth) = (self.cQuery[1]-1,'DECEMBER')
            elif(len(self.cQuery)==3 and self.cQuery[1]>2017) :
                (fYear,fMonth) = (2017,'DECEMBER')
            elif(len(self.cQuery)==3 and self.cQuery[1]<=2017) :
                if(self.cQuery[2]=='JANUARY') :
                    (fYear, fMonth) = (self.cQuery[1]-1,'DECEMBER')
                else :
                    isQueryForLastPart = True
                    (fYear,fMonth) = (self.cQuery[1],self.cQuery[2])
            # do it for: 'for loop'
            if(isQueryForLastPart==False) :
                fYear += 1
            print('fYear, fMonth= ',fYear,fMonth)
            # ----------------
            for yr in range(1951,fYear) :
                arr = [self.cQuery[0], yr]
                mQuery.append(self.generateQuery2(arr))
            # ---for last Year-----
            if(isQueryForLastPart) :
                months = []
                for i in range(0,config.month_string_to_number(fMonth)) :
                    months.append(config.month_number_to_string(i))
                arr = [self.cQuery[0], fYear, months ]
                mQuery.append(self.generateQuery2(arr))
            return mQuery
        elif(option=='forward') :
            return None
    # generate Query for approach: ANN-2
    def generateQuery2(self, arr) :
        if(len(arr) == 2)   :
            return config.createMongoQueryANN2(arr[0],arr[1])
        elif(len(arr)==3) :
            return config.createMongoQueryANN2(arr[0],arr[1],arr[2])

##
# getmQuery0 : if(yr<2018 & len(cQuery)=2) => Original Data
# getmQuery1 : MongoQuery for ANN-I approach
# getmQuery2 : MongoQuery for ANN-II approach (Backword) => getAllData from DB
##
def __main__():
    mPath = "src\expect\expectingQuery.py"
    try :

        ob = ExpectingQuery()
        return(ob.cQuery, ob.mQueryApproch0, ob.mQueryApproch1, ob.mQueryApproch2)

    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)
