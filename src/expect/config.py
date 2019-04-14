"""
# generate Query
"""
# @query: JSON object :: For DB Actual Data :: ANN-0
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
def createMongoQueryANN1(region,year,month) :
    query={
        "REGION":{"$eq":str(region)},
        "YEAR":{"$lt":year},
        "MONTH":{'$regex':'.*'+str(month)}
    }
    return query
# @query: JSON object :: ANN-2
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
def queryType (query) :
    queryType = ""
    for i in range(0, len(query))   :
        queryType += str(type(query[i]))
    return queryType
# @convert Month Number to Name
def month_number_to_string(num) :
    num = num % 12
    monthNumber = {
        '0': 'JANUARY',
        '1': 'FEBRUARY',
        '2': 'MARCH',
        '3': 'APRIL',
        '4': 'MAY',
        '5': 'JUNE',
        '6': 'JULY',
        '7': 'AUGUST',
        '8': 'SEPTEMBER',
        '9': 'OCTOBER',
        '10': 'NOVEMBER',
        '11': 'DECEMBER',
    }
    return(monthNumber[str(num)])
# @convert Month Name to Number
def month_string_to_number(name):
    monthName = {
        'JANUARY': '0',
        'FEBRUARY': '1',
        'MARCH': '2',
        'APRIL':'3',
        'MAY':'4',
        'JUNE':'5',
        'JULY':'6',
        'AUGUST':'7',
        'SEPTEMBER':'8',
        'OCTOBER':'9',
        'NOVEMBER':'10',
        'DECEMBER':'11',
    }
    return(int(monthName[str(name)]))