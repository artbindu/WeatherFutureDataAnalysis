import json
# for json static data
# searchItems : array[]
def jsonData(searchItems) :
    jsonConfig = json.load(open("src\config\config.json"))
    # print(len(jsonConfig))
    try :
        data = jsonConfig
        for sItem in searchItems :
            data = data.get(sItem)
        return data
    except :
        return ('invalid search with in \'config.json\'')

# menu drive for main.py
def menuDriven(choice)    :
        print("\n\n----------------------------------------\n")
        print("\n0. Exit")
        print("\n1. POST Data from Excel Format to MongoDB")
        print("\n2. DELETE Data")
        print("\n3. ANALYSIS Data with Both Approach")
        return (input("\n\n\t"+choice))

