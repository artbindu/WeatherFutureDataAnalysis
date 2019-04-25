'''
    @it use to help process three types Mongo Data; (mData1,mData,mData)

    @now we have to process its Data for Read to ANN algo
    @where,
    @mData ::: searching Month and its next 5 Month Data; ANN Approach-II (write New Code: 'ANNalgo/processingData2.py')
    @mData ::: searching Month and its next 5 Month Data; ANN Approach-II (write New Code: 'ANNalgo/processingData2.py')
'''
import src.ANNalgo.processingANNdata2 as dataProcessing2
import src.ANNalgo.ann as algoANN
import src.share.utils.utils as utils

##
#
##
def __main__(cQuery, mData) :
    print('i am with in ann controller2')
    for x in mData :
        print('\n',x)
    (annInput,annOutput,annQInput,annQOutput,lenANN) = (None,None,None,None,utils.Utils.jsonData(['annLength']))
    (lastYr,lastMonth) = utils.Utils.findEndYearEndMonth(mData)
    (expectQuery,lastMonth) = (None,utils.Utils.month_string_to_number(lastMonth))
    print('LASTyEAR:     ',lastYr)
    while(1) :
        # function to generate newQuery for ANN-II
        lastMonth += 1
        if(lastMonth%12 == 0) :
            lastYr += 1
        expectQuery = [cQuery[0],lastYr,utils.Utils.month_number_to_string(lastMonth)]
        print('expectQuery: ', expectQuery)
        # ----------------------------------
        # calling ANN-II
        # analysis data (of all DATABASE data) && create ANN-I/O data
        ob2 = dataProcessing2.ProcessOnlyData_of_ANN2(expectQuery,mData,lenANN)
        (annInput,annOutput,annQueryInput, annMaxData) = (ob2.annInput,ob2.annOutput,ob2.annQInput,ob2.maxData)
        # -------------------------------------
        #---------ann algo calling-------------
        obANN = algoANN.ANN_Algo(annInput,annOutput,annMaxData, annQueryInput)
        annQueryOutput = obANN.qOutput
        result = round(annQueryOutput[0][0], 2)
        print('result: ', result)
        expectQuery.append(result)

        # ---- insert expect data last part of mainData ---------
        print('result query: ',expectQuery)
        print(expectQuery[2])
        print(utils.Utils.month_string_to_number(expectQuery[2]))
        if(utils.Utils.month_string_to_number(expectQuery[2])%12 == 0) :
            tempArr = []
            tempArr.append(expectQuery)
            mData.append(tempArr)
        else :
            tempArr = mData[len(mData)-1]
            tempArr.append(expectQuery)
            mData[len(mData)-1] = tempArr
        print(tempArr)
        
        #-----------end of data adding last part -----------------
        '''
        for x in mData:
            print('\n\n\n',x)
        input('continue?  :==>  ')
        '''
        # ---------------------------------

        # ----condition for stop while loop: when (expectQuery == cQuery)
        if(len(cQuery)==2) :
            if(cQuery == [expectQuery[0],expectQuery[1]] and expectQuery[2]=='DECEMBER') :
                pData = createPlottingDataANN_II(cQuery,mData)
                break
        elif(len(cQuery)==3) :
            if(cQuery == [expectQuery[0],expectQuery[1],expectQuery[2]]) :
                pData = createPlottingDataANN_II(cQuery,mData)
                break
        # ------------------------------------------------
    return (pData)

def createPlottingDataANN_II(cQuery,allData) :
    headPart = ['REGION', 'YEAR', 'MONTH', 'DATA']
    pData = []
    #print('cquery: ',cQuery)
    l1 = len(allData)
    if(len(cQuery)==2) :
        pData.append(headPart)
        for x in allData[l1-1] :
            pData.append(x)
    elif(len(cQuery)==3) :
        pData.append(headPart)
        for i in range(0,l1) :
            pData.append(allData[i][len(allData[l1-1])-1])
    print(pData)
    return pData
