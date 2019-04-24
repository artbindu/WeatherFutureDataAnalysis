# @python Data Analytics Programming
import src.share.utils.utils as utils
import src.controller.controller as controller
# ------------Rainfall--Data--Analysis------------------------

try :
    (choice, sms) = ('1', None)
    while (choice != '0') :
        choice = utils.Utils.menuDriven('Your choice:\t')
        if(choice == '0')   :
            print('\n\n----------Thank You Visit Again')

        # elif(choice == '1')   :  # insert data from excel and store it mongoDb
        #     dataPath = utils.Utils.jsonData(["rawData","rainfall"])
        #     dbConfig = utils.Utils.jsonData(["mongoDB"])
        #     sms = controller.postData(dataPath,dbConfig,"rainfall")

        # elif(choice =='2') :
        #     dbConfig = utils.Utils.jsonData(["mongoDB"])
        #     sms = controller.deleteData(dbConfig,"rainfall")
        #     print('main', sms)
        
        elif(choice=='3') :
            ob = controller.Controller()
            dbConfig = utils.Utils.jsonData(["mongoDB"])
            sms = ob.analysisData(dbConfig,"rainfall")
        
        else :
            sms = 'invalid entry'

        if(sms) :
            print('\n\n\n\n**** : main : ****\n', sms,'\n**** : main : ****\n')
            sms = None
except AttributeError:
    print(' module \'src.controller.controller\' has no method of specific query')
except Exception:
    print('main method : error: ', Exception.__context__())
