
import numpy as np
import src.share.utils.utils as utils

# lamda function
sigmoid = lambda x : 1/(np.exp(-x)+1)  # f[-1,1] --> (0,1)
derv_sigmoid = lambda x : x*(1-x)      # f[0,1]  --> [0,0.25] : at x=0.5, y=0.25


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
        dk3 = derv_sigmoid(self.z3)*(self.y-self.z3)
        print('z3= ', self.z3, 'derv_sigmoid= ', derv_sigmoid(self.z1))
        input()
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
        (self.input, self.output) = (np.array(iANN),np.array(oANN))
        self.qInput = np.array(qiANN)
        self.maxData = (int(maxData/100)+1)*100
        # print(self.maxData)

        # create Neural class object
        hiddenSize = utils.Utils.jsonData(['ann','hiddenSize'])
        learningRate = utils.Utils.jsonData(['ann','learningRate'])
        self.obj = Neural(self.input/self.maxData, self.output/self.maxData, hiddenSize, learningRate)
        # ann Training
        noOfTraining = utils.Utils.jsonData(['ann',"trainingIteration"])
        self.annTraining(noOfTraining)
        self.qOutput = self.annTesting()

    def annTraining(self,iterationNo)   :
        print('..........Learning Started..........')
        self.obj.learn(iterationNo)
        print('..........Learning Complete.........')

    def annTesting(self)    :
        print('..........Testing Start.............')
        res = self.obj.test(self.qInput/self.maxData)
        print('..........Testing Complete..........')
        return res * self.maxData
    # @destructors
    def __del__(self) :
        (self.input,self.output, self.qInput,self.qOutput, self.maxData) = (None,None, None,None, None)





'''
=============================================
        Error chaking in each step
=============================================
w11 = self.w1 + self.lr*np.dot(self.x.T,dk1)
w22 = self.w2 + self.lr*np.dot(self.z1.T,dk2)
w33 = self.w3 + self.lr*np.dot(self.z2.T,dk3)
self.chakingError(self.w1,w11)
self.chakingError(self.w2,w22)
self.chakingError(self.w3,w33)
(self.w1,self.w2,self.w3) = (w11,w22,w33)

def chakingError(self,array1, array2) :
    print('error chaking')
    print(np.setdiff1d(array1, array2))
    input()

'''