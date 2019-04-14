# part 00
import src.config.config as config
# part 01
import src.excel.xlsxInput as xlsx
import src.grouping.groupingData as groupingData
import src.mongoo.mongoDBController as mongoDB


## 
# @method: transfer data from Excel --to--> mongoDB
# @calling from 'main.py'
# @path: string: excel file path
##
def postData(path)   :
    (xlsxData, sheetData, sms, mPath) =(None, None, False, 'src/controller.postData()')

    try :   
        # @method: take input from '.xlsx' i.e. excel format
        if(path) :
            xlsxData = xlsx.__main__(config.jsonData([path]))
        # @method : for creating a small sheet;  like:< RegionName--Year--Month--DataValue >
        if(xlsxData) :
            sheetData = groupingData.__main__(xlsxData)
        # @method: send data to mongoDB
        if(sheetData) :
            sms = mongoDB.__main__(config.jsonData(["mongoDB"]),'POST', sheetData)
            if(sms) :
                return(sms)
    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    finally :
        print('finally error : '+mPath)
        return False


