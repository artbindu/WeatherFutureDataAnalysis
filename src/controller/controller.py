# part 00
import src.config.config as config
# part 01
import src.excel.xlsxInput as xlsx
import src.grouping.groupingData as groupingData
import src.mongoo.mongoDBController as mongoDB


## 
# @method: transfer data from Excel --to--> mongoDB
# @path: string: excel file path
##
def postData(path)   :
    (xlsxData, sheetData, sms, mPath) =(None, None, None, 'src/controller.postData()')

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
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)


##
# @method: full clear mongo database
##
def deleteData()    :
    (query, Data, sms, mPath) =(None, None, None, 'src/controller.deleteData()')
    try :   # @method: delete all data in mongodb
        sms = mongoDB.__main__(config.jsonData(["mongoDB"]),'DELETE')
        if(sms) :
            print('cont: ', sms)
            return sms
    except AttributeError:
        print('AttributeError : '+mPath)
    except TypeError:
        print('TypeError : '+mPath)
    except Exception :
        print('Unknone Exception '+mPath+' ==> ', Exception)
