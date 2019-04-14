
class ProcessOnlyData_of_ANN1 :
    def __del__(self) :
        self.lenANN = None
        (self.onlyData,self.annInput,self.annOutput ) = (None,None,None)
    # constructor
    def __init__(self, cQuery, allData, lenANN) :
        self.lenANN = lenANN
        self.onlyData = self.fetchingOnlyDataPart(allData)
        self.annInput = self.createANNInput()
        self.annOutput =  self.createANNOutput()
    # calling from Constructor
    def fetchingOnlyDataPart(self,allData) :
        arr = []
        for i in range(1,len(allData)) :
            # allData: [region, year, month, data]
            arr.append(allData[i][3])
        # print(arr)
        return arr
    # calling from Constructor
    def createANNInput(self) :
        (arr, count) = ([],0)
        for i in range(0,len(self.onlyData)) :
            (temp, count) = ([], count+1)
            for j in range(0, self.lenANN) :
                temp.append(self.onlyData[i+j])
            arr.append(temp)
            if((len(self.onlyData)-count)<self.lenANN)   :
                # print(arr)
                return arr
    # calling from Constructor
    def createANNOutput(self) :
        arr = []
        for i in range(self.lenANN, len(self.onlyData))   :
            temp= []
            temp.append(self.onlyData[i])
            arr.append(temp)
        temp= ['?']
        arr.append(temp)
        # print(arr)
        return arr
    # send data
    def getMaxData(self) :
        return max(self.onlyData)
    def getANNinput(self) :
        self.queryInput = []
        self.queryInput.append(self.annInput[len(self.annInput)-1])
        del self.annInput[len(self.annInput)-1]
        # print ('\n\nannInput: ',self.annInput,'\n\nqueryInput: ',self.queryInput)
        return(self.annInput, self.queryInput)
    def getANNoutput(self) :
        self.queryOutput = []
        self.queryOutput.append(self.annOutput[len(self.annOutput)-1])
        del self.annOutput[len(self.annOutput)-1]
        # print('\n\nannOutput: ',self.annOutput,'\n\nannOutput: ',self.queryOutput)
        return (self.annOutput, self.queryOutput)

    

    

def __main__(clientQuery, array, lenANN) :
    # array[0] contains ['REGION','YEAR','MONTH','DATA']
    # so we avaoid it
    ob = ProcessOnlyData_of_ANN1(clientQuery, array, lenANN)
    # return({annInput,annQueryInput},  {annOutput,annQueryOutput},  {annMaxData})
    (annInput, annQInput) = ob.getANNinput()
    (annOutput, annQOutput) = ob.getANNoutput()
    return(annInput,annQInput, annOutput,annQOutput, ob.getMaxData())


