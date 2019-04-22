import src.share.utils.utils as utils

class ProcessOnlyData_of_ANN2 :
    def __del__(self) :
        (self.lenANN,self.maxData) = (5,None)
        (self.annInput,self.annOutput,self.annQInput) = (None,None,None)
    # constructor
    def __init__(self, cQuery, arrData, lenANN, option) :
        (self.lenANN,self.maxData) = (lenANN,None)
        (self.annInput,self.annOutput,self.annQInput) = ([],[],[])
        self.createANNIO(cQuery,arrData,option)
        #self.display()
        
    def getANNInput(self) :
        return self.annInput
    def getANNOutput(self) :
        return self.annOutput
    def getANNQInput(self) :
        return self.annQInput
    def getMaxData(self) :
        return self.maxData

    # cQuery = ['BIHAR', 2018, 'JANUARY']  ; i.e. length=3 all-time
    def createANNIO(self,cQuery,arrData,option) :
        (stYear,stMonth,endYear,endMonth) =  find_First_End_Details(arrData)
        print('starting status:', stYear,stMonth)
        print('ending status:', endYear,endMonth)

        (qYear,qMonth) = (cQuery[1],cQuery[2])
        l1 = len(arrData)
        l2 = len(arrData[l1-1])
        print('tRow= ',l1,'tCol= ',l2)
        if(option=='backword') :
            # print('\n\n\n\n================data==============')
            # ckLast: take data from 2017--to--1951
            # ckFirst: for understand which is 'annQueryInput'
            (ckLast,ckFirst) = (0,0)
            for k in range(l1,0,-1) :
                # stop last moment: when take both-year-data
                if(ckLast==1 and k==1) :
                    break
                (filterIData,filterOData, row,flag) = ([],[], k-1,-1)
                for i in range(0,self.lenANN) :
                    if( ((l2-1)-i)<0 and flag==-1) :
                        (row,flag,ckLast) = (row-1,0,1)
                    col = ((l2-1)-i)%12
                    filterIData.append(arrData[row][col][3])
                self.maxData = self.maxValue(filterIData)
                filterIData.reverse()
                
                if(ckFirst==0) :
                    self.annQInput.append(filterIData)
                    ckFirst = 1
                else:
                    self.annInput.append(filterIData)                    
                    filterOData.append(arrData[k-1][utils.Utils.month_string_to_number(cQuery[2])][3])
                    self.maxData = self.maxValue(filterOData)
                    self.annOutput.append(filterOData)

            self.annInput.reverse()
            self.annOutput.reverse()

        print('create ANN I/O data')

    def maxValue(self, b) :
        if(self.maxData==None) :
            return max(b)
        elif(max(b)>self.maxData) :
            return max(b)
        return self.maxData

    def display(self) :
        print('\n\n\n\n  annInput:\t\t\tOutput')
        for i in range(0,len(self.annInput)) :
            print(self.annInput[i],'  ::  ',self.annOutput[i])
        print('\n\nannQInput: ',self.annQInput)
        print(' Maximum Data: ',self.maxData)


## option=> foward/backword Data
# newQuery = ['BIHAR', 2018, 'JANUARY']  ; i.e. length=3 all-time
def __main__(nowQuery, allData, lenANN) :
    print('with in ANN Data Processing2')
    # array[0] contains ['REGION','YEAR','MONTH','DATA']
    # so we avaoid it
    ob = ProcessOnlyData_of_ANN2(nowQuery, allData, lenANN,'backword')
    return(ob.getANNInput(),ob.getANNOutput(),ob.getANNQInput(),ob.getMaxData())


def find_First_End_Details(arrData) :
    (stYear,stMonth) = (arrData[0][0][1],arrData[0][0][2])
    l1 = len(arrData)-1
    l2 = len(arrData[l1])-1
    (endYear,endMonth) = (arrData[l1][l2][1],arrData[l1][l2][2])
    return(stYear,stMonth,endYear,endMonth)
