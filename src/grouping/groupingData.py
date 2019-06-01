import src.share.utils.utils as utils

##
# @meta class : containing 4 types of data
##
class DataSheet :
    (Region, Year, Month, Data) = (None, None, None, None)
    # @constructors
    # @(region,year,month,data) = (string,int,string,float)
    def __init__(self, region, year, month, data)  :
        (self.region,self.year,self.month,self.data) = (region,year,month,data)
    # @destructors
    def __del__(self) :
        (self.region,self.year,self.month,self.data) = (None,None,None,None)

##
# @functionality: create small sheets of excel-sheet(listtype) data 
##
class GroupingData :
    (dataList, dataGroup) = (None, None)
    # @constructors
    # @dataList : excel-data
    def __init__(self, dataList)    :
        self.dataList = dataList
        self.dataGroup = self.processDataForGrouping()
    # @destructors
    def __del__(self) :
        (self.dataList,self.dataGroup) = (None, None)
    # @method: create sheet type data using meta-class: DataSheet
    # @calling from 'constructor'
    def processDataForGrouping(self)    :
        arrayList = []
        l = len(self.dataList)
        count = 0
        for i in range(1, l)  :
            # col-0: SUBDIVISION, col-1: YEAR
            # col-2::col-13 : (JAN	FEB	MAR	APR	MAY	JUN	JUL	AUG	SEP	OCT	NOV	DEC)
            for j in range(2, 14)   :
                if(self.dataList[i][j]=='NA')   :
                    self.dataList[i][j] = 0
                count += 1
                # create Object of 'DastSheet' class
                region =  utils.Utils.int_or_float_or_str(self.dataList[i][0])
                year = utils.Utils.int_or_float_or_str(self.dataList[i][1])
                month = utils.Utils.int_or_float_or_str(self.dataList[0][j])
                data = utils.Utils.int_or_float_or_str(self.dataList[i][j])

                # creating object of meta class 'DataSheet'
                obj = DataSheet(region, year, month, data)
                arrayList.append(obj)
        # print('complete: grouping data for insert data in database in proper format')
        return arrayList
