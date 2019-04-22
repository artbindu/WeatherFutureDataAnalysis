# package: to draw graph
import matplotlib.pyplot as plt
import numpy as np  # using numpy

import src.graph.dataProcess as plotUtils
import src.share.utils.utils as utils

##
# @draw graph according to different searching type
##
class PlotGraph :
    # @constructor
    def __init__(self)  :
        self.sms = None   
    # @destructor
    def __del__(self) :
        self.sms = None   
    # @xlabel_sms,ylabel_sms,title_sms: 'string'
    def DrawGraph(self,xlabel_sms,ylabel_sms,title_sms)   :
        plt.xlabel("---------"+xlabel_sms+"------------>")
        plt.ylabel("---------"+ylabel_sms+"------------>")
        plt.title(title_sms)
        plt.show()
        self.sms = "done graph ploting"
    #def whenTakeSingleInput(self, title, xdata1,xdata2, ydata, tSMS, xSMS1,xSMS2, ySMS) :
    #                   Region, Month, Year, Data,    r,   m,   y,    d
    def plotGraph(self, region, month, year, data, rsms, ysms, msms, dsms) :
        self.sms = rsms+" :: "+str(utils.Utils.int_or_float_or_str(region[1][0]))
        self.sms += "\n"+ysms+" ::"+str(utils.Utils.int_or_float_or_str(month[1][0]))
        for i in range(0, len(data))   :
            plt.plot(year[i],data[i], label=data[i])
            plt.plot(year[i],data[i],'ro')
            # change below part
            #self.DrawGraph(msms,dsms,self.sms)
        self.DrawGraph(msms,dsms,self.sms)


##
# arrayData : 
#
##
def __main__(arrayData, queryType,status=None) :
    (Region,Year,Month,Data) = ([],[],[],[])
    # region,year,month,data :: 1-dim array
    # r,y,m,d :: correspoinding header files
    for i in range(0, len(arrayData)) :
        (region,year,month,data, r,y,m,d) = plotUtils.dataProcessing.processDataForPloting(arrayData[i])
        Region.append(region)
        Year.append(year)
        Month.append(month)
        Data.append(data)
        (color,sms) = plotUtils.dataProcessing.checkColor(i)
        print('\n\ncolor= ',color,'\tStatus= ',sms,'\n Data: ',year,data)

    ob = PlotGraph()  #create object
    if(queryType=="searchByRegionYear") :
        ob.plotGraph(Region,Year,Month,Data, r,y,m,d)
    elif( queryType=="searchByRegionYearMonth" ) :
        ob.plotGraph(Region,Month,Year,Data, r,m,y,d)
        return ob.sms

    else :
        print('did not plot graph for this query')
        return None
