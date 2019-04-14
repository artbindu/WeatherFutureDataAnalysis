##
# @meta class : containing 4 types of data
##
class DataSheet :
    (Region, Year, Month, Data) = (None, None, None, None)
    # @constructor
    # @(region,year,month,data) = (string,int,string,float)
    def __init__(self, region, year, month, data)  :
        (self.region,self.year,self.month,self.data) = (region,year,month,data)
    # @destructor
    def __del__(self) :
        (self.region,self.year,self.month,self.data) = (None,None,None,None)

##
# @functionality: create small sheets of excel-sheet(listtype) data 
##
class GroupingData :
    (dataList, dataGroup) = (None, None)
    # @constructor
    # @dataList : excel-data
    def __init__(self, dataList)    :
        self.dataList = dataList
        self.dataGroup = self.processDataForGrouping()
    # @destructor
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
                    continue
                count += 1
                # create Object of 'DastSheet' class
                region =  self.int_or_float_or_str(self.dataList[i][0])
                year = self.int_or_float_or_str(self.dataList[i][1])
                month = self.int_or_float_or_str(self.dataList[0][j])
                data = self.int_or_float_or_str(self.dataList[i][j])

                # creating object of meta class 'DataSheet'
                obj = DataSheet(region, year, month, data)
                arrayList.append(obj)
        # print('complete: grouping data for insert data in database in proper format')
        return arrayList
    # method to return actual data type
    def int_or_float_or_str(self,s):
        s = str(s)
        try:
            try:
                return int(s)
            except ValueError:
                return float(s)
        except ValueError:
            return s

##
# @main function: calling from controller
# @dataList: <class 'list'> :: excel file data
# @return: <class 'list'[<class 'src.grouping.groupingData.DataSheet']> : {region/year/month/data}
##
def __main__(dataList)  :
    ob = GroupingData(dataList)
    return ob.dataGroup
