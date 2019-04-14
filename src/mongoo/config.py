# POST endpoint
def postQuery(id,reg,yr,mon,data) :
    (id,data) = (int_or_float_or_str(id), int_or_float_or_str(data))
    (reg,yr,mon) = (int_or_float_or_str(reg), int_or_float_or_str(yr),int_or_float_or_str(mon))
    # print(id,data,reg,yr,mon)
    query = {
        "findQuery" : {
            "_id": id,
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
    return (query.get("findQuery"),query.get("setQuery"),query.get("insertQuery"))

# DELETE endpoint
def deleteQuery()   :
    # delete all data from 'collection' in mongodb
    query = {}
    return query


# method to return actual data type
def int_or_float_or_str(s):
    s = str(s)
    try:
        try:
            return int(s)
        except ValueError:
            return float(s)
    except ValueError:
        return s


