# @python Data Analytics Programming
import src.config as config
import src.controller.controller as controller
# @generate logger file
import lib.logging as logging

# ------------Rainfall--Data--Analysis------------------------
LOG_FILENAME = 'logger/logger.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

try :
    (choice, sms) = ('1', None)
    while (choice != '0') :
        choice = config.menuDriven('Your choice:\t')
        if(choice == '0')   :
            print('\n\n----------Thank You Visit Again')

        elif(choice == '1')   :  # insert data from excel and store it mongoDb
            sms = controller.postData("rainfallDataPath")

        elif(choice =='2') :
            sms = controller.deleteData()
            print('main', sms)
        
        elif(choice=='3') :
            sms = controller.analysisData()
        
        else :
            sms = 'invalid entry'

        if(sms) :
            print('\n\n\n\n**** : main : ****\n', sms,'\n**** : main : ****\n')
            sms = None
except AttributeError:
    print(' module \'src.controller.controller\' has no method of specific query')
except Exception:
    print('main method : error: ', Exception.__context__())
