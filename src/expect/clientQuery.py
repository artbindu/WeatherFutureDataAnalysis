##
# Searching porper state name from json file
##
import json
from pprint import pprint

import src.config.config as mainConfig

class ClientQuery :
    def __init__(self) :
        self.jfile = "src/expect/indianStates.json"
        self.cQuery = self.clientQuery()
        # print(self.cQuery)
        
    def __del__(self) :
        (self.jfile, self.cQuery) = (None, None)

    def clientQuery(self) :
        try :            
            while(1)  :        
                print("\n1. <searchByRegionYear> \n2. <searchByRegionYearMonth>")
                choice = input("\n\n\tEnter your choice: ")

                # print('json file: ',self.jfile)
                allStatesData = json.load(open(self.jfile))
                # pprint(allStatesData)

                try: 
                    if(choice=='1') :
                        region = self.searchingRegionName(allStatesData)
                        year = int(input("expect Year: "))
                        # return <'string', 'int'> type
                        # print('queryType ==> \'searchByRegion\'')
                        return([region,year])
                    elif(choice=='2') :
                        region = self.searchingRegionName(allStatesData)
                        month = str(input("Searching Month:  ").upper())
                        year = int(input("expect Year: "))
            
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

    def searchingRegionName(self, statesData) :
        try :
            while(1) :
                (findState,findStateArea) = ('','')
                searchState = input('\n\nsearching State: ').upper()
                findState = self.searchingFromJSON(statesData,searchState)
                if(findState) :
                    print(findState)
                    if(str(type(findState)) == "<class 'dict'>") :
                        searchStateArea = input('searching State\'s Area: ').upper()
                        findStateArea = self.searchingFromJSON(statesData,searchState,searchStateArea)
                        if(findStateArea) :
                            print(findStateArea)
                if(findState==None or findStateArea==None) :
                    sms = {
                        "Searching Hints":{
                            1: "Search with first 3 letters of a State/Union Territory (if not get search with first 4 letters)",
                            2: "Search with short name of each state; a.e. 'West Bengal' : 'WB'"
                        }
                    }
                    print(sms)
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

    

# main method
def __main__() :
    mPath = "src\expect\clientQuery.py"
    print(mPath)
    
    try :

        ob = ClientQuery()
        return ob.cQuery

    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)
    