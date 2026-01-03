import src.share.utils.utils as utils

class FilterUtils(object) :
    # method to searching mongo query of specific region and months
    @staticmethod
    def selectedRegionMonthQuery(allRegion) :
        mQuery = []
        for reg in allRegion :
            for imon in range(0, 12) :
                mQuery.append(FilterUtils.query_SearchRegionMonth(reg, utils.Utils.month_number_to_string(imon)))
        # print('all mongo query: ', mQuery)
        return mQuery
    @staticmethod
    def query_SearchRegionMonth(reg, mon) :
        query = { 
                "REGION" : {"$eq":str(reg)},
                "MONTH":{'$eq':str(mon)}
            }
        return query
