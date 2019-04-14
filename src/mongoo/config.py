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


# GET endpoint
def queryMenuDrivenGETdata(choice) :
    while(1)  :
        print("\n1. <searchByRegion> \n2. <searchByYear>  \n3. <searchByMonth>")
        print("\n4. <searchByRegionYear> \n5. <searchByRegionMonth> \n6. <searchByYearMonth>")
        print("\n7. <searchByRegionYearMonth>")
        choice = input("\n\n\t"+choice)
        try :
            if(choice=='1')   :
                region = str(input("Searching Region:  ").upper())
                query = {"REGION":{"$eq":region}}
                return("searchByRegion", query)
            elif(choice=='2') :
                year = int(input("Searching Year:  "))
                query = {"YEAR":{"$eq":year}}
                return("searchByYear", query)
            elif(choice=='3') :
                month = str(input("Searching Month:  ").upper())
                query = {"MONTH":{"$eq":month}}
                return("searchByMonth", query)

            elif(choice=='4') :
                region = str(input("Searching Region:  ").upper())
                year = int(input("Searching Year:  "))
                query = {"REGION":{"$eq":region},"YEAR":{"$eq":year}}
                return("searchByRegionYear", query)
            elif(choice=='5') :
                region = str(input("Searching Region:  ").upper())
                month = str(input("Searching Month:  ").upper())
                query = {"REGION":{"$eq":region},"MONTH":{"$eq":month}}
                return("searchByRegionMonth", query)
            elif(choice=='6') :
                year = int(input("Searching Year:  "))
                month = str(input("Searching Month:  ").upper())
                query = {"YEAR":{"$eq":year},"MONTH":{"$eq":month}}
                return("searchByYearMonth", query)

            elif(choice=='7') :
                region = str(input("Searching Region:  ").upper())
                year = int(input("Searching Year:  "))
                month = str(input("Searching Month:  ").upper())
                query = {"REGION":{"$eq":region},"YEAR":{"$eq":year},"MONTH":{"$eq":month}}
                return("searchByRegionYearMonth", query)

            else :
                print("Invalid Input")
                choice = "Enter Your Choice: "
        except Exception:
            print('invalid Input Data Type')
            choice = "Enter Your Choice: "


# DELETE endpoint
def queryMenuDrivenDELETEdata()   :
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


