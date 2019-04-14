# find endYear & endMonth
def findEndYearEndMonth(arrData) :
    rows = len(arrData)
    colms = len(arrData[rows-1])
    (endYear,endMonth) = (arrData[rows-1][colms-1][1],arrData[rows-1][colms-1][2])
    return (endYear,endMonth)
# @convert Month Name to Number
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
# @convert Month Number to Name
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