
import numpy as np
import math
import src.share.utils.utils as utils

# lamda function
sigmoid = lambda x : 1/(1+np.exp(-x))  # f[-1,1] --> (0,1)
derv_sigmoid = lambda x : sigmoid(x)*(1-sigmoid(x))
remender = lambda x,y : 0 if(int(x)%y==0) else 1


# this is Meta class
class Neural:
    def __init__(self,x,y,hidden_size,rate) :
        self.input_size=np.shape(x)[1]
        self.output_size=np.shape(y)[1]
        self.hidden_size = hidden_size
        # print('input size: ', self.input_size)
        # print('output size: ', self.output_size)
        # print('hidden size: ',self.hidden_size)

        self.lr=rate
		# read ANN input output
        self.x=np.array(x)
        self.y=np.array(y)
        # ----hidden layer 01----
        self.w1=np.random.uniform(-1,1,size=(self.input_size,self.hidden_size))
        self.b1=np.random.uniform(-1,1,size=(1,self.hidden_size))
		# ----hidden layer 01----
        self.w2=np.random.uniform(-1,1,size=(self.hidden_size,self.hidden_size))
        self.b2=np.random.uniform(-1,1,size=(1,self.hidden_size))
		# ----hidden layer 03----
        self.w3=np.random.uniform(-1,1,size=(self.hidden_size,self.output_size))
        self.b3=np.random.uniform(-1,1,size=(1,self.output_size))

    def __del__(self) :
        (self.input_size,self.output_size,self.hidden_size,self.lr) = (None,None,None,None)
        (self.x,self.y) = (None,None)
        (self.w1,self.b1,self.w2,self.b3,self.w3,self.b3) = (None,None,None,None,None,None)
        (self.z1,self.z2,self.z3) = (None,None,None)

    def forward(self):
		# ----calculation of hidden layer 01----
        h1=np.dot(self.x,self.w1)+self.b1
        self.z1 = sigmoid(h1)

		# ----calculation of hidden layer 02----
        h2=np.dot(self.z1,self.w2)+self.b2
        self.z2 = sigmoid(h2)

		# ----calculation of hidden layer 03----
        h3=np.dot(self.z2,self.w3)+self.b3
        self.z3 = sigmoid(h3)
        
    def backward(self):
        # here error of forward calculation is: (self.y-self.z3)
        dk3 = derv_sigmoid(self.z3)*(self.y-self.z3)
        dk2 = derv_sigmoid(self.z2)*np.dot(dk3,self.w3.T)
        dk1 = derv_sigmoid(self.z1)*np.dot(dk2,self.w2.T)
        
        # ----update weight w------
        self.w1+=self.lr*np.dot(self.x.T,dk1)
        self.w2+=self.lr*np.dot(self.z1.T,dk2)
        self.w3+=self.lr*np.dot(self.z2.T,dk3)
        # ----update bias b-------
        self.b1+=np.sum(dk1,axis=0)
        self.b2+=np.sum(dk2,axis=0)
        self.b3+=np.sum(dk3,axis=0)

    def learn(self,iteration):
        for i in range(iteration):
            self.forward()
            self.backward()

    def test(self,test_x):
        test_x=np.array(test_x)

        h1=np.dot(test_x,self.w1)+self.b1
        z1 = sigmoid(h1)

        h2=np.dot(z1,self.w2)+self.b2
        z2 = sigmoid(h2)

        h3=np.dot(z2,self.w3)+self.b3
        t_result = sigmoid(h3)

        return t_result


class ANN_Algo :
    # @constructors
    def __init__(self, iANN,oANN,maxData,qiANN)   :
        # ANN I/O data
        # if maxData = 123, then return 130
        self.maxData = 10 * float(int(maxData)//10 + remender(maxData,10))
        (self.input, self.output) = (np.array(iANN),np.array(oANN))
        self.norm = 1
        self.norm = self.normalizedData()
        self.qInput = np.array(qiANN)
        print('maxdata: ', self.maxData, 'norm data: ', self.norm)
        
        # create Neural class object
        hiddenSize = utils.Utils.jsonData(['ann','hiddenSize'])
        learningRate = utils.Utils.jsonData(['ann','learningRate'])
        # create object
        self.obj = Neural(self.input/(self.maxData*self.norm), self.output/(self.maxData*self.norm), hiddenSize, learningRate)
        # ann Training
        noOfTraining = utils.Utils.jsonData(['ann',"trainingIteration"])
        self.annTraining(noOfTraining)
        self.qOutput = self.annTesting()

    # norm: sets_element/squre_root(sum(sets_element*sets_element))
    def normalizedData(self) :
        sqSum = 0
        for i in range (0, len(self.input)) :
            for y in (self.input[i]) :
                sqSum += math.pow(y/self.maxData, 2)
            for y in (self.output[i]) :
                sqSum += math.pow(y/self.maxData, 2)
        # normalized data
        return(math.sqrt(sqSum))

    def annTraining(self,iterationNo)   :
        print('..........Learning Started..........')
        self.obj.learn(iterationNo)
        print('..........Learning Complete.........')

    def annTesting(self)    :
        print('..........Testing Start.............')
        res = self.obj.test(self.qInput/(self.maxData*self.norm))
        print('..........Testing Complete..........')
        return res * (self.maxData*self.norm)
    # @destructors
    def __del__(self) :
        (self.maxData, self.norm) = (None, None)
        (self.input, self.output, self.qInput, self.qOutput) = (None, None, None, None)
