import src.clustering.kmean as kmean

class Filturing :
    # method to filtering data of a particular region and months
    def filturingData(self, arrData) :
        # clustering data :: part_01
        del arrData[0] #delete header ['REGION', 'YEAR', 'MONTH', 'DATA']
        ob = kmean.Clustering_cMean(arrData)
        clusterData = ob.clusterSet
        # print('clustering result: ')
        # for x in ob.clusterSet :
        #     print('\n\n', x)

        # reset data of low&high cluster data
        for i in range(0, len(clusterData)) :
            print('for i= ',i,' density= ', len(clusterData[i])-1)

        # 
        for i in range(0, len(clusterData)) :
            if(len(clusterData[i]) == 1) :
                if(i>=2) :
                    break
                continue
            for j in range(1, len(clusterData[i])) :
                clusterData[i][j][3] = round(clusterData[i][j][3] + (clusterData[i+1][0]-clusterData[i][0])/1.5, 2)
            clusterData[i][0] = None
            break
        for i in range(len(clusterData)-1, 0, -1) :
            for j in range(1, len(clusterData[i])) :
                clusterData[i][j][3] = round(clusterData[i][j][3] - (clusterData[i][0]-clusterData[i-1][0])/2.0, 2)
            clusterData[i][0] = None
            break
        
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
 