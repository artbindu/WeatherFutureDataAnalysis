
class ProcessOnlyData_of_ANN1 :
    def __del__(self) :
        self.lenANN = None
        (self.onlyData,self.annInput,self.annOutput,self.queryInput) = (None,None,None,None)
        self.maxData = None
    # constructor
    def __init__(self, cQuery, allData, lenANN) :
        self.lenANN = lenANN
        self.onlyData = self.fetchingOnlyDataPart(allData)
        self.annInput = self.createANNInput()
        self.annOutput =  self.createANNOutput()
        self.maxData = self.getMaxData()
        # to ready ann data
        self.readyIOdata()
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
        temp= ['?'] # use it for dummy
        arr.append(temp)
        # print(arr)
        return arr
    # send data
    def getMaxData(self) :
        return max(self.onlyData)
    def readyIOdata(self) :
        self.queryInput = []
        # last term of 'self.annInput' is 'self.queryInput'
        self.queryInput.append(self.annInput[len(self.annInput)-1])
        # so, remaining first (n-1) data are 'self.annInput'
        del self.annInput[len(self.annInput)-1]
        # delete last term [?] part of 'self.annOutput' for 'self.annOutput'
        del self.annOutput[len(self.annOutput)-1]
        # print ('\n\nannInput: ',self.annInput,'\n\nqueryInput: ',self.queryInput,'\n\nannOutput: ',self.annOutput)
