# part 00
import src.config.config as config
# part 01
import src.excel.xlsxInput as xlsx
import src.grouping.groupingData as groupingData
import src.mongoo.mongoDBController as mongoDB
# part 03
import src.expect.expectingQuery as expectingQuery
import src.ANNalgo.annController1 as ANN1
import src.ANNalgo.annController2 as ANN2
import src.graph.plotGraphController as plotGraphExpectData



##
# @method: expect future data :: using ANN both approach
#           (i) expect form same month of different year
#           (ii) expect a month data from its previous 5 months
# @calling from 'main.py'
##
def analysisData() :
    (mData1,mData2,pData0,pData1,pData2) = ([],[],[],[],[])
    (pDataAll,statusAll) = ([],[])
    mPath = 'src/controller.analysisData()'

    try :
        print('---------going for fetch mongoSave data-----------')
        # expect mongoQuery for plot Data
        (cQuery,mQuery0,mQuery1,mQuery2) = expectingQuery.__main__()
        print('get all Data from Mongo')
        # print('\n\\n\n\n\n\n\n',cQuery,'\n\n\n',mQuery0,'\n\n\n',mQuery1,'\n\n\n',mQuery2)

        ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~find DB Data Original if year<2018~~~~~~~~~~~~~
        if(mQuery0) :
            (mongoData, sms) = mongoDB.__main__(config.jsonData(["mongoDB"]),'GET', mQuery0)
            if(sms) :
                pData0 = mongoData
                # input(pData0)
        ## ~~~~~~~~~~~~~~~~~~~~~~end-of-part00~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Part-01~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~fetch data from MongoDB ANN2--approach1~~~~~~~~~~~~
        for i in range(0, len(mQuery1)) :
            (mongoData, sms) = mongoDB.__main__(config.jsonData(["mongoDB"]),'GET', mQuery1[i])
            if(sms) :
                mData1.append(mongoData)
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
            (mongoData, sms) = mongoDB.__main__(config.jsonData(["mongoDB"]),'GET', mQuery2[i])
            if(sms) :
                del mongoData[0]
                mData2.append(mongoData)
                # print(mData2)
        #chekingFuntion(cQuery, mData2)
        pData2 = ANN2.__main__(cQuery,mData2)
        # input(pData2)
        print('--------complete to fetch ANN-II(with BackwordMonths) data-----------')
        # ~~~~~~~~~~~~~~~~~~~~~end-of-Part02~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
        ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~ploting graph~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if(len(pData1)>0) :
            pDataAll.append(pData1)
            statusAll.append("ANN-I Data")
        if(len(pData2)>0) :
            pDataAll.append(pData2)
            statusAll.append("ANN-II(Backword) Data")
        if(len(pData0)>0) :
            pDataAll.append(pData0)
            statusAll.append("Original Data")
        print('\n\n\\n\n\n\n\n\n\n\nClient Query: ',cQuery)
        if(len(cQuery)==2) :
            sms = graphControllerExpectData(pDataAll,'searchByRegionYear',statusAll)
        if(len(cQuery)==3) :
            sms = graphControllerExpectData(pDataAll,'searchByRegionYearMonth',statusAll)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        return sms


        print('get all Data from Mongo')
    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)

##
# @use to plot graph for data expection result
# @pData: array[[],[],..] data; use for ploting  || queryType: string
##
def graphControllerExpectData(pData,queryType,status=None) :
    # going for graph ploting
    sms = plotGraphExpectData.__main__(pData,queryType,status)
    return sms






## 
# @method: transfer data from Excel --to--> mongoDB
# @path: string: excel file path
##
def postData(path)   :
    (xlsxData, sheetData, sms, mPath) =(None, None, None, 'src/controller.postData()')

    try :   
        # @method: take input from '.xlsx' i.e. excel format
        if(path) :
            xlsxData = xlsx.__main__(config.jsonData([path]))
        # @method : for creating a small sheet;  like:< RegionName--Year--Month--DataValue >
        if(xlsxData) :
            sheetData = groupingData.__main__(xlsxData)
        # @method: send data to mongoDB
        if(sheetData) :
            sms = mongoDB.__main__(config.jsonData(["mongoDB"]),'POST', sheetData)
            if(sms) :
                return(sms)
    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)


##
# @method: full clear mongo database
##
def deleteData()    :
    (query, Data, sms, mPath) =(None, None, None, 'src/controller.deleteData()')
    try :   # @method: delete all data in mongodb
        sms = mongoDB.__main__(config.jsonData(["mongoDB"]),'DELETE')
        if(sms) :
            print('cont: ', sms)
            return sms
    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)

## use to clear arrayList data after it use
def clearArrayData(arrArrData) :
    retArrData = []
    for array in arrArrData :
        del array
        array = []
        retArrData.append(array)
    return retArrData