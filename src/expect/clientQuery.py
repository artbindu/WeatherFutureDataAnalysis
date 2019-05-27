##
# Searching porper state name from json file
##
import json
from pprint import pprint

import src.share.utils.utils as utils

class ClientQuery :
    def __init__(self) :
        self.stateJFile = utils.Utils.jsonData(["expectData","clientQuery","searchingStates"])
        self.monthJFile = utils.Utils.jsonData(["expectData","clientQuery","searchingMonths"])
        # print(self.stateJFile, self.monthJFile)
        # self.cQuery = ['KERALA', 2020, 'MAY']
        self.cQuery = self.clientQuery()
        # print(self.cQuery)
        
    def __del__(self) :
        (self.stateJFile, self.monthJFile, self.cQuery) = (None, None, None)

    def clientQuery(self) :
        # return(['KERALA',2019,'MAY'])
        try :            
            while(1)  :        
                print("\n1. expect by Region & Year  \n2. expect by Region, Year & Month")
                choice = input("\n\tEnter your choice: ")

                # print('json file: ',self.stateJFile)
                allStatesData = json.load(open(self.stateJFile))
                # pprint(allStatesData)
                allMonthsData = json.load(open(self.monthJFile))
                # pprint(allStatesData)

                try: 
                    if(choice=='1') :
                        region = self.searchJSONData(allStatesData,'REGION', 'Searching State: ', 'Searching State\'s Area: ')
                        year = self.searchYear("expect Year: ")
                        # return <'string', 'int'> type
                        # print('queryType ==> \'searchByRegion\'')
                        return([region,year])
                    elif(choice=='2') :
                        region = self.searchJSONData(allStatesData,'REGION', 'Searching State: ', 'Searching State\'s Area: ')
                        month = self.searchJSONData(allMonthsData,'MONTH', "Searching Month:  ")
                        year = self.searchYear("expect Year: ")
            
                        # return <'string', 'int', 'string'> type
                        # print('queryType ==> \'searchByRegionMonth\'')
                        return([region,year,month])
                    else :
                        print("Invalid Input")
                        choice = "Enter Your Choice: "
                except AttributeError:
                    print('AttributeError : clientQuery()')
                    choice = "Enter Your Choice: "
        except AttributeError:
            print('AttributeError : clientQuery()')

    def searchYear(self,sms) :
        flag = 0
        while(flag==0) :
            try :
                yr = int(input(sms))
                if(yr>1952) :
                    return yr
            except  ValueError :
                print('Did not enter Number')
            print('Enter Again,--------') 
            
    def searchJSONData(self, statesData, hintsSMS, sms1, sms2=None ) :
        if(hintsSMS == 'REGION') :
            hintsSMS = {
                "Searching Hints":{
                    1: "Search with first 3/4 letters of a State/Union Territory",
                    2: "Search with short name of each state; a.e. 'West Bengal' : 'WB'"
                },
                "Example" : {
                    "West Bengal" : "WB or wes",
                    "Jammu & Kashmir" : "JK or J&K or Jammu or jam"
                }
            }
        elif(hintsSMS == 'MONTH') :
            hintsSMS = {
                1: "Search with first three letters/ full Name",
                2: "Search with Numeric Number with Months a.e. 1,6,12"
            }
        try :
            while(1) :
                (findState,findStateArea) = ('','')
                searchState = input(sms1).upper()
                findState = self.searchingFromJSON(statesData,searchState)
                if(findState) :
                    print(findState)
                    if(str(type(findState)) == "<class 'dict'>") :
                        searchStateArea = input(sms2).upper()
                        findStateArea = self.searchingFromJSON(statesData,searchState,searchStateArea)
                        if(findStateArea) :
                            print(str(findStateArea))
                if(findState==None or findStateArea==None) :
                    print(hintsSMS)
                else :
                    if(findStateArea) :
                        return findStateArea
                    else :
                        return findState
        except AttributeError:
            print('AttributeError : searchingRegionName()')

    def searchingFromJSON(self, allData,stateName,stateArea=None) :
        sName = None
        if(stateArea) :
            sName = allData.get(stateName).get(stateArea)
        else :
            sName = allData.get(stateName)
        return sName
