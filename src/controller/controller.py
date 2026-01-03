# part 00
import src.share.utils.utils as utils
# part 01
import src.excel.xlsxInput as xlsx
import src.grouping.groupingData as groupingData
import src.mongoo.mongoDBController as mongoDB
import src.mongoo.dbConnection as dbConnect
# part 03
import src.expect.expectingQuery as expectingQuery
import src.ANNalgo.annController1 as ANN1
import src.ANNalgo.annController2 as ANN2
import src.graph.plotGraphController as plotExpectData
# part 04
import src.clustering.filtering as filtering
import src.share.utils.filterUtils as fUtils

class Controller :
    db = None
    # @constructors
    def __init__(self,dbConfig,dbName) :
        # print('with in constructor: ',dbConfig,dbName)
        self.db = dbConnect.MongoConnection(dbConfig,dbName)
        self.db.start()
        # print(self.db.collection)
    # @destructors
    def __del__(self) :
        self.db.end()

    ##
    # @method: get all distinct region from db, using clustering upate noise data and update db data
    ##
    def filteringData(self) :
        obDB = mongoDB.MongoRequest(self.db.collection)
        # get all distinct region
        obDB.getDistinctData("REGION")
        # print(obDB.data)
        # get mongoQuery for filtering data
        mQuery = fUtils.FilterUtils.selectedRegionMonthQuery(obDB.data)
        # print(mQuery)
        ob0 = filtering.filtering()
        tData = []
        for query in mQuery :
            print('for query --> ', query)
            obDB.getData(query)
            # remove header part --> [REGION, YEAR, MONTH, DATA]
            Arr = list(obDB.data) if obDB.data else []
            if(Arr and len(Arr)>0) :
                del Arr[0]
            # print('length: ', len(obDB.data)-1) # for header file
            if(obDB.sms) :
                # send_Old_Data for filtering and get_New_Data
                newData = ob0.filteringData(Arr)
                # update data into database
                obDB.updateData(newData)
                tData.clear()
                print('\n\n\n\n.....filtering Complete: ',newData[0][0],' 1951-2017 ', newData[0][2], ' data......')
                # input('update data into data base')
            
    ## 
    # @method: transfer data from Excel --to--> mongoDB
    # @dataPath: string: excel file path
    ##
    def postData(self,dataPath)   :
        mPath ='src/controller.postData()'
        try :   
            # @method: take input from '.xlsx' i.e. excel format
            if(dataPath) :
                ob1 = xlsx.ExcelInput(dataPath)
            # @method : for creating a small sheet;  like:< RegionName--Year--Month--DataValue >
            if(ob1.data) :
                ob2 = groupingData.GroupingData(ob1.data)
            # @method: send data to mongoDB
            if(ob2.dataGroup) :
                ob3 = mongoDB.MongoRequest(self.db.collection)
                ob3.postData(ob2.dataGroup)
                return(ob3.sms)
        except AttributeError as e:
            print('AttributeError : '+mPath+' ==> ', str(e))
        except TypeError as e:
            print('TypeError : '+mPath+' ==> ', str(e))
        except Exception as e:
            print('Unknown Exception '+mPath+' ==> ', str(e))


    ##
    # @method: full clear mongo database
    ##
    def deleteData(self)    :
        mPath ='src/controller.deleteData()'
        try :   # @method: delete all data in mongodb
            ob1 = mongoDB.MongoRequest(self.db.collection)
            ob1.deleteData()
            return ob1.sms
        except AttributeError as e:
            print('AttributeError : '+mPath+' ==> ', str(e))
        except TypeError as e:
            print('TypeError : '+mPath+' ==> ', str(e))
        except Exception as e:
            print('Unknown Exception '+mPath+' ==> ', str(e))


    ##
    # @method: expect future data :: using ANN both approach
    #           (i) expect form same month of different year
    #           (ii) expect a month data from its previous 5 months
    ##
    def analysisData(self) :
        (mData1,mData2,pData0,pData1,pData2) = ([],[],[],[],[])
        (pDataAll,statusAll) = ([],[])
        mPath = 'src/controller.analysisData()'

        try :
            print('---------going for fetch mongoSave data-----------')
            # expect mongoQuery for plot Data
            obExp = expectingQuery.ExpectingQuery()
            (cQuery,mQuery0,mQuery1,mQuery2) = (obExp.cQuery,obExp.mQuery0,obExp.mQuery1,obExp.mQuery2)
            print('get all MongoQuery')
            # print('\n\\n\n\n\n\n\n',cQuery,'\n\n\n',mQuery0,'\n\n\n',mQuery1,'\n\n\n',mQuery2)
            # create mongoDBController Class Object to fetch mongoData
            obDB = mongoDB.MongoRequest(self.db.collection)

            doAgain = 'y'
            while(doAgain != 'N') :
            ## ~~~~~~~~~~~~~~~~~~~~~start-while-loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~find DB Data Original if year<2018~~~~~~~~~~~~~
                if(mQuery0) :
                    obDB.getData(mQuery0)
                    if(obDB.sms) :
                        pData0 = obDB.data
                        # input(pData0)
                ## ~~~~~~~~~~~~~~~~~~~~~~end-of-part00~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~Part-01~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~fetch data from MongoDB ANN2--approach1~~~~~~~~~~~~
                for i in range(0, len(mQuery1)) :
                    obDB.getData(mQuery1[i])
                    if(obDB.sms) :
                        mData1.append(obDB.data)
                        # print(mData1)
                pData1 = ANN1.__main__(cQuery,mData1)
                if(len(cQuery)==3 and len(pData1)==1) :
                    pData1 = pData1[0]
                elif(len(cQuery)==2 and len(pData1)==12) :
                    arr = []
                    arr.append(['REGION', 'YEAR', 'MONTH', 'DATA'])
                    for x in pData1 :
                        arr.append(x[len(x)-1])
                        # print(mData1)
                    pData1 = arr
                # input(pData1)
                print('--------complete to fetch ANN-I data-----------')
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~end-of-Part01~~~~~~~~~~~~~~~~~~~~~~~~        
                ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~Part-02~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~fetch data from MongoDB ANN2-approach2(Backword)~~~~~~~~
                for i in range(0, len(mQuery2)) :
                    obDB.getData(mQuery2[i])
                    if(obDB.sms) :
                        del obDB.data[0]
                        mData2.append(obDB.data)
                        # print(mData2)
                #chekingFuntion(cQuery, mData2)
                pData2 = ANN2.__main__(cQuery,mData2)
                # input(pData2)
                print('--------complete to fetch ANN-II(with BackwordMonths) data-----------')
                # ~~~~~~~~~~~~~~~~~~~~~end-of-Part02~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
                ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~plotting graph~~~~~~~~~~~~~~~~~~~~~~~~~~~
                if(len(pData1)>0) :
                    pDataAll.append(pData1)
                    statusAll.append("ANN-I Data")
                if(len(pData2)>0) :
                    pDataAll.append(pData2)
                    statusAll.append("ANN-II(Backword) Data")
                if(len(pData0)>0) :
                    pDataAll.append(pData0)
                    statusAll.append("Original Data")
                print('\n\n\n\n\n\n\n\n\n\nClient Query: ',cQuery)
                if(len(cQuery)==2) :
                    sms = self.plottingData(pDataAll,'searchByRegionYear',statusAll)
                if(len(cQuery)==3) :
                    sms = self.plottingData(pDataAll,'searchByRegionYearMonth',statusAll)
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                (mData1,mData2,pData0,pData1,pData2,pDataAll,statusAll) = self.clearArrayData([mData1,mData2,pData0,pData1,pData2,pDataAll,statusAll])
                doAgain = input('\n\nAgain Expect Result On Same Query: [Y/n] ').upper()
            ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~end-while-loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            return sms

        except AttributeError as e:
            print('AttributeError : '+mPath+' ==> ', str(e))
        except TypeError as e:
            print('TypeError : '+mPath+' ==> ', str(e))
        except Exception as e:
            print('Unknown Exception '+mPath+' ==> ', str(e))

    ##
    # @use to plot graph for data expection result
    # @pData: array[[],[],..] data; use for plotting  || queryType: string
    ##
    def plottingData(self,pData,queryType,status=None) :
        # going for graph plotting
        ob = plotExpectData.PlotController()
        sms = ob.plotExpectData(pData,queryType,status)
        return sms

    ## use to clear arrayList data after it use
    def clearArrayData(self,arrArrData) :
        retArrData = []
        for array in arrArrData :
            del array
            array = []
            retArrData.append(array)
        return retArrData
