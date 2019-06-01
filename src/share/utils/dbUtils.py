import src.share.utils.utils as utils
 
class MongoDBUtils(object) :
    # POST endpoint
    @staticmethod
    def postQuery(id=None,reg=None,yr=None,mon=None,data=None) :
        id = utils.Utils.int_or_float_or_str(id)
        data = utils.Utils.int_or_float_or_str(data)
        reg = utils.Utils.int_or_float_or_str(reg)
        yr = utils.Utils.int_or_float_or_str(yr)
        mon = utils.Utils.int_or_float_or_str(mon)
        # print(id,data,reg,yr,mon)
        query = {
            "findQuery" : {
                "REGION": reg,
                "YEAR": yr,
                "MONTH": mon
            },
            "setQuery" : {
                "$set": {
                    "DATA": data
                } 
            },
            "insertQuery" : {
                "_id": id,
                "REGION": reg,
                "YEAR": yr,
                "MONTH": mon,
                "DATA": data
            }
        }
        # return(         findQuery,             updateQuery,          insertQuery  )
        return (query.get("findQuery"),query.get("setQuery"),query.get("insertQuery"))

    # DELETE endpoint
    @staticmethod
    def deleteQuery()   :
        # delete all data from 'collection' in mongodb
        query = {}
        return query



