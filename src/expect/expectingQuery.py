import src.expect.clientQuery as clientQuery
import src.share.utils.expectUtils as expectUtils
import src.share.utils.utils as utils

class ExpectingQuery :
    def __init__(self) :
        (self.cQuery, self.mQuery0, self.mQuery1, self.mQuery2) = (None, None, None, None)
        # generate cQuery througth constructor
        try :
            ob = clientQuery.ClientQuery()
            self.cQuery = ob.cQuery
            # print('\n\n\n self.cQuery = ',self.cQuery)

            # generate 'mQuery0' through constructor
            self.mQuery0 = self.generateMongoQuery_OriginalData()
            # print('\n\n\n self.mQuery0 = ',self.mQuery0)
            
            # generate 'mQuery1' through constructor
            self.mQuery1 = self.generateMongoQuery_Approch1()
            # print('\n\n\n self.mQuery1 = ',self.mQuery1)

            # generate 'mQuery2_Backword' through constructor :: all db data(1951-2018)
            self.mQuery2 = self.generateMongoQuery_Approch2('backword')
            # print('\n\n\n self.mQuery2 = ',self.mQuery2)
            
            print("\n\n*********************\n\n")
        except AttributeError :
            print('AttributeError')
        except TypeError:
            print('TypeError : ')
        except Exception :
            print('error class ExpectingQuery().__init__()')

    def __del__(self) :
        (self.cQuery, self.mQuery0, self.mQuery1, self.mQuery2) = (None, None, None, None)
       
    # -------generate mongoQuery if year<2018 -----------------
    def generateMongoQuery_OriginalData(self) :
        query = None
        if(self.cQuery[1]<2018) :
            if(len(self.cQuery)==2) :
                return expectUtils.ExpectUtils.createMongoQuery_ForOriginalData(self.cQuery[0],self.cQuery[1])
            elif(len(self.cQuery)==3) :
                return expectUtils.ExpectUtils.createMongoQuery_ForOriginalData(self.cQuery[0],self.cQuery[1],self.cQuery[2])
        elif(len(self.cQuery)==3 and self.cQuery[1]>=2018) :
            return expectUtils.ExpectUtils.createMongoQuery_ForOriginalData(self.cQuery[0],2017,self.cQuery[2])
        return query

    # -------generate MongoQuery with first ANN approach-------
    def generateMongoQuery_Approch1(self)    :
        (qType, mQuery) = (expectUtils.ExpectUtils.queryType(self.cQuery), [])
        
        # [ 'region', year, 'month'] = ['BIHAR', 2018, 'MARCH'] :: search all year Region-Month
        if(qType == "<class 'str'><class 'int'><class 'str'>") : 
            mQuery.append(self.generateQuery1(self.cQuery))
            return(mQuery)
        # [ 'region', year] = ['BIHAR', 2018]  ::  search by Region, Year(with all Month)
        elif(qType == "<class 'str'><class 'int'>") :
            for i in range(0, 12) :
                arr = [self.cQuery[0],self.cQuery[1],utils.Utils.month_number_to_string(i)]
                mQuery.append(self.generateQuery1(arr))
            return(mQuery)
        # for other query
        else :
            print('----invalid query----')
            return None
    def generateQuery1(self, arr) :
        return expectUtils.ExpectUtils.createMongoQueryANN1(arr[0],arr[1],arr[2])

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
                for i in range(0,utils.Utils.month_string_to_number(fMonth)) :
                    months.append(utils.Utils.month_number_to_string(i))
                arr = [self.cQuery[0], fYear, months ]
                mQuery.append(self.generateQuery2(arr))
            return mQuery
        elif(option=='forward') :
            return None
    # generate Query for approach: ANN-2
    def generateQuery2(self, arr) :
        if(len(arr) == 2)   :
            return expectUtils.ExpectUtils.createMongoQueryANN2(arr[0],arr[1])
        elif(len(arr)==3) :
            return expectUtils.ExpectUtils.createMongoQueryANN2(arr[0],arr[1],arr[2])
