import xlrd

# path: excel表路径
def getDataTable(path):
    dataBook = xlrd.open_workbook(path);
    dataSheet = dataBook.sheet_by_name(dataBook.sheet_names()[0])
    columnName = [ 'name', 'course', 'grade1', 'grade2' ]
    columnIndex = [ 2, 3, 5, 6 ]
    dataTable = []
    for i in range(2, dataSheet.nrows):
        dataRow = {}
        for j in range(0, 4):
            value = dataSheet.cell_value(i, columnIndex[j])
            dataRow[columnName[j]] = value
        dataTable.append(dataRow)
    return dataTable