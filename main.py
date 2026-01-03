# @python Data Analytics Programming
import src.share.utils.utils as utils
import src.controller.controller as controller
# ------------Rainfall--Data--Analysis------------------------

if __name__ == "__main__":
    try :
        dbConfig = utils.Utils.jsonData(["mongoConfig"])
        obj = controller.Controller(dbConfig,'rainfall')
        
        (choice, sms) = ('1', None)
        while (choice != '0') :
            choice = utils.Utils.menuDriven('Your choice:\t')
            if(choice == '0')   :
                break

            elif(choice == '1')   :  # insert data from excel and store it mongoDb
                dataPath = utils.Utils.jsonData(["rawDataPath","rainfall"])
                # insert data into database
                sms = obj.postData(dataPath)
                # filtering data and update database
                if(input('clustering data[Y/n]: ').lower() == 'y') :
                    sms = obj.filteringData()

            elif(choice =='2') :
                sms = obj.deleteData()
            
            elif(choice=='3') :
                sms = obj.analysisData()
            
            else :
                sms = 'invalid entry'

            if(sms) :
                print('\n\n**** : ***** : ****\n', sms,'\n**** : ***** : ****\n')
                sms = None
    except AttributeError:
        print(' module \'src.controller.controller\' has no method of specific query')
    except Exception:
        print('main method : error: ', Exception.__context__())

# print('\n\n----------Thank You Visit Again')
