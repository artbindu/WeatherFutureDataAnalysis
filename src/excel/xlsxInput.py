# @why: package to read file from excel
import lib.xlrd.__init__ as xlrd

##
#  @functionality: read/convert-to-array-type of excel data
##
class ExcelInput :
    (path, sheet, data) = (None, None, None)
    # @constructors
    # @path: string
    def __init__(self, path)    :
        self.path = path
        self.sheet = self.excelInput()
        # @return to controller
        self.data = self.prossingData()
    # @destructors
    def __del__(self) :
        (self.path, self.sheet, self.data) = (None, None, None)
    ##
    # @method: take_input_from_Excel_Sheet :: constructor calling
    # @return 'lib.xlrd.sheet.Sheet' 
    ##
    def excelInput(self) :   
        openSheet = xlrd.open_workbook(self.path) 
        sheet = openSheet.sheet_by_index(0) 
        sheet.cell_value(0, 0) 
        # print(type(sheet))
        # print('complete: to take data from excel')
        return sheet
    # @method: prossing_sheet_type_data :: constructor calling
    # @return: <class 'list'> : i-th row <=> list i-th element
    def prossingData(self) :
        arrayData = []
        for i in range(self.sheet.nrows) :
            tempArray = []
            for j in range(0,len(self.sheet.row_values(i)))  :
                tempArray.append(self.sheet.row_values(i)[j])
            arrayData.append(tempArray)
        return arrayData
