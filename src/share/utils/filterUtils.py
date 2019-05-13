
class FilterUtils :
    # methods to search all Regions
    @staticmethod
    def searchAllRegion() :
        regions = ["JAMMU & KASHMIR", "HIMACHAL PRADESH", "WEST RAJASTHAN"]
        return (regions)
    def queryForDistinctRegion(self) :
        return None
    def queryForRegionMonth(self,reg,mon) :
        query={ 
                "REGION" : {"$eq":str(reg)},
                "MONTH":{'$regex':'.*'+str(mon)}
            }
        return query
