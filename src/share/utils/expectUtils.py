

class ExpectUtils(object) :
    """
    # generate Query
    """
    # @query: JSON object :: For DB Actual Data :: ANN-0
    @staticmethod
    def createMongoQuery_ForOriginalData(region,year,month=None) :
        if(month) :
            query={ 
                "REGION" : {"$eq":str(region)},
                "YEAR" : {"$lte":year},
                "MONTH":{'$regex':'.*'+str(month)}
            }
        else :
            query={ 
                "REGION" : {"$eq":str(region)},
                "YEAR" : {"$eq":year}
            }
        return query
    # @query: JSON object :: ANN-1
    @staticmethod
    def createMongoQueryANN1(region,year,month) :
        query={
            "REGION":{"$eq":str(region)},
            "YEAR":{"$lt":year},
            "MONTH":{'$regex':'.*'+str(month)}
        }
        return query
    # @query: JSON object :: ANN-2
    @staticmethod
    def createMongoQueryANN2(region,year,months=None) :
        if(months) :
            query={ 
                "REGION" : {"$eq":str(region)},
                "YEAR" : {"$eq":year},
                "MONTH": {'$in': months}
            }
        else :
            query={ 
                "REGION" : {"$eq":str(region)},
                "YEAR" : {"$eq":year}
            }
        return query


    """
    # other helping function
    """
    #@queryType : <class 'str'><class 'int'><class 'str'>
    @staticmethod
    def queryType (query) :
        queryType = ""
        for i in range(0, len(query))   :
            queryType += str(type(query[i]))
        return queryType
        