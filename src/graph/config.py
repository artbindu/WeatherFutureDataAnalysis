
##
# @method: to fetch Data from CSV file and stor it into list
# @csvfile: <class '_io.TextIOWrapper'>
# @plots: <class '_csv.reader'>
# @region, year, month, data :: <class 'list'>
# @return: <class 'list'>
##
def processDataForPloting(arrayData) :
    (region, year, month, data) = ([],[],[],[])
    # print('length: ',len(arrayData))
    if(len(arrayData)>1) :
        for i in range(1, len(arrayData)) :
            # print(arrayData[i][0],arrayData[i][1],arrayData[i][2],arrayData[i][3])
            region.append(arrayData[i][0])
            year.append(arrayData[i][1])
            month.append(arrayData[i][2])
            data.append(arrayData[i][3])
        # return([regions],[years],[months],[data], 'REGION','YEAR','MONTH','DATA')
        return(region,year,month,data, arrayData[0][0],arrayData[0][1],arrayData[0][2],arrayData[0][3])
    return None

# ploting color
def checkColor(i) :
    colorStatus = {
        "0": {
            "color": "BLUE",
            "status": "ANN-I Algo Result"
        },
        "1": {
            "color": "RED",
            "status": "ANN-II Algo Result"
        },
        "2": {
            "color": "GREEN",
            "status": "Original Data in DB"
        }
    }
    return(colorStatus.get(str(i)).get("color"), colorStatus.get(str(i)).get("status"))

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
