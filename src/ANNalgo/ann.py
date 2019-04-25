
import numpy as np

# this is Meta class
class Neural:
    def __init__(self,x,y,hidden_size,rate) :
        self.input_size=np.shape(x)[1]
        self.output_size=np.shape(y)[1]
        self.hidden_size=hidden_size
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

    def sigmoid(self,xx):
        return 1/(np.exp(-xx)+1)
        
    def derv_sigmoid(self,tt):
        return tt*(1-tt)
        
    def forward(self,x):
		# ----calculation of hidden layer 01----
        h1=np.dot(self.x,self.w1)+self.b1
        self.z1=self.sigmoid(h1)
		# ----calculation of hidden layer 02----
        h2=np.dot(self.z1,self.w2)+self.b2
        self.z2=self.sigmoid(h2)
		# ----calculation of hidden layer 03----
        h3=np.dot(self.z2,self.w3)+self.b3
        self.z3=self.sigmoid(h3)
        
    def backward(self,x,y):
        dk1=self.derv_sigmoid(self.z3)*(self.y-self.z3)
        dk2=self.derv_sigmoid(self.z2)*np.dot(dk1,self.w3.T)
        dk3=self.derv_sigmoid(self.z1)*np.dot(dk2,self.w2.T)
        
        self.w1+=self.lr*np.dot(x.T,dk3)
        self.w2+=self.lr*np.dot(self.z1.T,dk2)
        self.w3+=self.lr*np.dot(self.z2.T,dk1)

        self.b1+=np.sum(dk3,axis=0)
        self.b2+=np.sum(dk2,axis=0)
        self.b3+=np.sum(dk1,axis=0)
        
    def learn(self,iteration):
        for i in range(iteration):
            self.forward(self.x)
            self.backward(self.x,self.y)
            
    def test(self,test_x):
        test_x=np.array(test_x)

        h1=np.dot(test_x,self.w1)+self.b1
        z1=self.sigmoid(h1)

        h2=np.dot(z1,self.w2)+self.b2
        z2=self.sigmoid(h2)

        h3=np.dot(z2,self.w3)+self.b3
        t_result=self.sigmoid(h3)

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
        self.obj = Neural(self.input/self.maxData, self.output/self.maxData, 8, 0.1)
        # ann Training
        self.annTraining(1000)
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
