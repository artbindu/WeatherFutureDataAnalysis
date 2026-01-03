import src.clustering.kMeanAlgo as kMeanAlgo

class filtering :
    # method to filtering data of a particular region and months
    def filteringData(self, arrData) :
        # clustering data :: part_01
        ob = kMeanAlgo.Clustering_cMean(arrData)
        clusterData = ob.clusterSet
        # reset data of low_&_high cluster data
        for i in range(0, len(clusterData)) :
            print('for i= ', i, ' density= ', len(clusterData[i])-1)
        # update clustering data
        for i in range(0, len(clusterData)) :
            if(len(clusterData[i]) > 1) :
                # update data
                if(len(clusterData[i])==3) :
                    clusterData[i][1][3] = clusterData[i+1][0]
                else :
                    for j in range(1, len(clusterData[i])) :
                        if(clusterData[i][j][3]<clusterData[i][0]) :
                            clusterData[i][j][3] = round(clusterData[i][j][3] + (clusterData[i+1][0]-clusterData[i][0])/2.0, 2)
                break
        for i in range(len(clusterData)-1, 0, -1) :
            if(len(clusterData[i]) > 1) :
                # update data
                if(len(clusterData[i])==3) :
                    clusterData[i][1][3] = clusterData[i-1][0]
                else :
                    for j in range(1, len(clusterData[i])) :
                        if(clusterData[i][j][3]>clusterData[i][0]) :
                            clusterData[i][j][3] = round(clusterData[i][j][3] - (clusterData[i][0]-clusterData[i-1][0])/2.0, 2)
                break
        # show clustering result
        print('clustering result: ')
        for x in ob.clusterSet :
            print('\n\n', x)
        # remove array header --> [REGION, YEAR, MONTH, DATA]
        updateData = []
        for x in clusterData :
            if(len(x)!=1) :
                del x[0]
                for y in x :
                    updateData.append(y)
        # print('updated clustering result: ')
        # for x in updateData :
        #     print(x)
        return updateData
 