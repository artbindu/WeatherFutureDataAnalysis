import src.share.utils.utils as utils
error = 5

maximumData = lambda x,y : x if(x>y) else y
minimumData = lambda x,y : y if(x>y) else x

class Clustering_cMean :
    (arrData, clusterSet, meanSet) = (None, None, None)
    ##
    # @constructor
    # @functionality: fetch data from csv file && create basic cluster mean
    # @functionality: generate clustering
    ##
    def __init__(self, arrData) :
        self.arrData = arrData
        (maxData, minData, sumData, count) = (None,None, 0,0)
        for i in range(0, len(self.arrData)) :
            if(i==0) :
                (maxData, minData) = (self.arrData[0][3], self.arrData[0][3])
            else :
                maxData = maximumData(maxData, self.arrData[i][3])
                minData = minimumData(minData, self.arrData[i][3])
            sumData += self.arrData[i][3]
            count += 1
        # print('maximum and minnum data: ', maxData, minData)
        # print('avg data: ', sumData/count)

        self.clusterSet = None
        if(self.arrData)  :
            self.meanSet = self.findClusteringMeans(utils.Utils.jsonData(["clustering", "noOfClusterSet"]),maxData,minData)
            self.clusterSet = []
            # calling to clustering algorithems
            self.clusterSet = self.clusteringAlgo()
            # assemble self.clusterSet
            self.clusterSet = self.assembleClusterSet()

    # re-assemble cluster set
    def assembleClusterSet(self) :
        l = len(self.clusterSet)
        for i in range(0,l-1)  :
            for j in range(i+1,l) :
                # sorting clustering mean in 'ACCENDING ORDER' i.e. small--big
                if(self.clusterSet[j][0]<self.clusterSet[i][0]) :
                    (self.clusterSet[i], self.clusterSet[j]) = (self.clusterSet[j], self.clusterSet[i])
        return self.clusterSet   
    # @method: find initial clustering mean
    def findClusteringMeans(self, noOfCluster, maxData, minData)    :
        diff=(maxData-minData)/(noOfCluster)
        ar=[]
        for i in range(0,noOfCluster)   :
            ar.append(round(minData+diff*(i+.5),2))
        # print('mean data-set: ', ar)
        return ar
    
    # main algorithems
    def clusteringAlgo(self)    :
        if (self.clusterSet == None)    :
            return None
        # store mean at 0-th position of the 'clusterSet'
        for i in range(0, len(self.meanSet)) :
            temp = []
            temp.append(self.meanSet[i])
            self.clusterSet.append(temp)
        (self.meanSet, count) = (None, 0)     # count no of iterations
        while(count!=-1)  :
            for i in range(0,len(self.arrData))   :
                position = self.chooseProperCluster(self.arrData[i][3])
                temp = self.clusterSet[position]
                temp.append(self.arrData[i])
            meanArr = self.findMean()
            inc = self.compareMeanAfterExecution(meanArr)
            if(inc==-1) :
                # print('no of iteration: ',count)
                count = inc
            else    :
                count += inc
        return (self.clusterSet)
    ## 04
    # @method: find a point goes to in which cluster set
    def compareMeanAfterExecution(self, meanArr)   :
        global error
        flag=0
        for i in range(0,len(meanArr))  :
            if(abs(meanArr[i]-self.clusterSet[i][0])>error) :
                flag=-1
                break
        if(flag == 0)    :
            return(-1)
        else    :
            for i in range(0, len(self.clusterSet)) :
               self.clusterSet[i][0] =  meanArr[i]
               del self.clusterSet[i][1:len(self.clusterSet[i])]
            return(+1)
    ## 03
    # @method: find a point goes to in which cluster set
    def findMean(self)   :
        meanArr = []
        for i in range(0,len(self.clusterSet))  :
            (sum,rowLength)=(0,len(self.clusterSet[i]))
            for j in range(1,rowLength)   :
                sum+=self.clusterSet[i][j][3]
            meanArr.append(round(sum/rowLength,2))
        # print(meanArr)
        return meanArr  # which is mean of cluster
    ## 02
    # @method: find a point goes to in which cluster set
    def chooseProperCluster(self, value)  :
        diff=[]
        for i in range(0,len(self.clusterSet))  :
            distance = abs(value-self.clusterSet[i][0])
            diff.append(distance)
        position = diff.index(min(diff))
        return position
