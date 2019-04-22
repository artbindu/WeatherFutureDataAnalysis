import json

class Utils(object) :
    # for json static data
    # searchItems : array[]
    @staticmethod
    def jsonData(searchItems) :
        jsonConfig = json.load(open("src/share/config.json"))
        # print(len(jsonConfig))
        try :
            data = jsonConfig
            for sItem in searchItems :
                data = data.get(sItem)
            return data
        except :
            return ('invalid search with in \'config.json\'')

    # menu drive for main.py
    @staticmethod
    def menuDriven(choice)    :
        print("\n\n----------------------------------------\n")
        print("\n0. Exit")
        print("\n1. POST Data from Excel Format to MongoDB")
        print("\n2. DELETE Data")
        print("\n3. ANALYSIS Data with Both Approach")
        return (input("\n\n\t"+choice))

    # # chaking variable data type & return particular data type
    @staticmethod
    # method to return actual data type
    def int_or_float_or_str(s):
        s = str(s)
        try:
            try:
                return int(s)
            except ValueError:
                return float(s)
        except ValueError:
            return s

    # @convert Month Number to Name
    @staticmethod
    def month_number_to_string(num) :
        num = num % 12
        monthNumber = {
            '0': 'JANUARY',
            '1': 'FEBRUARY',
            '2': 'MARCH',
            '3': 'APRIL',
            '4': 'MAY',
            '5': 'JUNE',
            '6': 'JULY',
            '7': 'AUGUST',
            '8': 'SEPTEMBER',
            '9': 'OCTOBER',
            '10': 'NOVEMBER',
            '11': 'DECEMBER',
        }
        return(monthNumber[str(num)])

    # @convert Month Name to Number
    @staticmethod
    def month_string_to_number(name):
        monthName = {
            'JANUARY': '0',
            'FEBRUARY': '1',
            'MARCH': '2',
            'APRIL':'3',
            'MAY':'4',
            'JUNE':'5',
            'JULY':'6',
            'AUGUST':'7',
            'SEPTEMBER':'8',
            'OCTOBER':'9',
            'NOVEMBER':'10',
            'DECEMBER':'11',
        }
        return(int(monthName[str(name)]))

    # find endYear & endMonth
    @staticmethod
    def findEndYearEndMonth(arrData) :
        rows = len(arrData)
        colms = len(arrData[rows-1])
        (endYear,endMonth) = (arrData[rows-1][colms-1][1],arrData[rows-1][colms-1][2])
        return (endYear,endMonth)
