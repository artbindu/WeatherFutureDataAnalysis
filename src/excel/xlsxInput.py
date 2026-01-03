# @why: package to read file from excel
try:
    import openpyxl
    USE_OPENPYXL = True
except ImportError:
    import xlrd.__init__ as xlrd
    USE_OPENPYXL = False

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
        self.data = self.processingData()
    # @destructors
    def __del__(self) :
        (self.path, self.sheet, self.data) = (None, None, None)
    ##
    # @method: take_input_from_Excel_Sheet :: constructor calling
    # @return sheet object
    ##
    def excelInput(self) :
        if USE_OPENPYXL:
            workbook = openpyxl.load_workbook(self.path, data_only=True)
            sheet = workbook.active
        else:
            openSheet = xlrd.open_workbook(self.path) 
            sheet = openSheet.sheet_by_index(0) 
            sheet.cell_value(0, 0)
        # print('complete: to take data from excel')
        return sheet
    # @method: prossing_sheet_type_data :: constructor calling
    # @return: <class 'list'> : i-th row <=> list i-th element
    def processingData(self) :
        arrayData = []
        if USE_OPENPYXL:
            for row in self.sheet.iter_rows(values_only=True):
                arrayData.append(list(row))
        else:
            for i in range(self.sheet.nrows) :
                tempArray = []
                for j in range(0,len(self.sheet.row_values(i)))  :
                    tempArray.append(self.sheet.row_values(i)[j])
                arrayData.append(tempArray)
        return arrayData
