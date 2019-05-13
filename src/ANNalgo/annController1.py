
'''
 @use while loop bcz: in our DB there is data from 1951 to 2017
 @if we expect data for Year>=2019;
 @ for 2019 Expect Year we have to analysis data on 2018 data 
 @ for 2020 Expect Year we fhave to analysis data on 2018 and thend 2019(which depends on 2018 expect data)
'''
import src.ANNalgo.processingANNdata1 as dataProcessing1
import src.ANNalgo.ann as algoANN
import src.share.utils.utils as utils


def __main__(cQuery,mData):    
    (length, lenANN)=  (len(mData), utils.Utils.jsonData(['ann','annLength']))
    for i in range(0,length) :
        while(1) :
            # this is query for a specific [Region, Year, Month]
            ob1 = dataProcessing1.ProcessOnlyData_of_ANN1(cQuery,mData[i],lenANN)
            (annInput,annQueryInput, annOutput, annMaxData) = (ob1.annInput,ob1.queryInput,ob1.annOutput,ob1.maxData)
            
            print('\n\n\n\n  annInput:\t\t\tOutput')
            for ii in range(0,len(annInput)) :
                print(annInput[ii],'  ::  ',annOutput[ii])
            print('\n\nannQInput: ',annQueryInput)
            print(' Maximum Data: ',annMaxData)

            #using ANN to check % of chance of get result 
            obANN = algoANN.ANN_Algo(annInput,annOutput,annMaxData, annQueryInput)
            annQueryOutput = obANN.qOutput

            result = round(annQueryOutput[0][0], 2)
            print('result: ', result)

            len_mData_i = len(mData[i])
            # change [Year, Data]
            newData = [mData[i][len_mData_i-1][0], mData[i][len_mData_i-1][1]+1, mData[i][len_mData_i-1][2], result]
            mData[i].append(newData)
            print('expect Data: ',newData)
            if(newData[1]==cQuery[1]) :
                break

    return mData
