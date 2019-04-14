# @python Data Analytics Programming
import src.config.config as config
import src.controller.controller as controller

# ------------Rainfall--Data--Analysis------------------------

try :
    (choice, sms) = ('1', None)
    while (choice != '0') :
        choice = config.menuDriven('Your choice:\t')
        # choice = '1'
        if(choice == '0')   :
            print('\n\n----------Thank You Visit Again')

        elif(choice == '1')   :  # insert data from excel and store it mongoDb
            sms = controller.postData("rainfallDataPath")

        elif(choice =='2') :
            sms = controller.deleteData()
            print('main', sms)
        
        else :
            sms = 'invalid entry'

        if(sms) :
            print('\n\n\n\n**** : main : ****\n', sms,'\n**** : main : ****\n')
            sms = None
        # choice = '0'
except AttributeError:
    print(' module \'src.controller.controller\' has no method of specific query')
except Exception:
    print('main method : error: ', Exception.__context__())
