# @python Data Analytics Programming
import src.config.config as config
import src.controller.controller as controller

# ------------Rainfall--Data--Analysis------------------------

try :
    (choice, data) = ('1', None)
    while (choice != '0') :
        choice = config.menuDriven('Your choice:\t')
        # choice = '1'
        if(choice == '0')   :
            print('\n\n----------Thank You Visit Again')

        elif(choice == '1')   :  # insert data from excel and store it mongoDb
            data = controller.postData("rainfallDataPath")

        
        else :
            data = 'invalid entry'

        if(data) :
            print('\n**** : main : ****\n', data)
            data = None
        # choice = '0'
except AttributeError:
    print(' module \'src.controller.controller\' has no method of specific query')
except Exception:
    print('main method : error: ', Exception.__context__())
