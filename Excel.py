import xlwt
rows = [
['a','b','c'],
['a1','b1','c1'],
['a2','b2','c2']
]


def getSheet(fileName="test.xlsx",sheetName="Accounts"):
	import xlrd
	 
	book = xlrd.open_workbook(fileName)
	 

	sheet = book.sheet_by_index(0)
	 

	result = []

	for i in range(sheet.nrows):
		row = sheet.row(i)
		_row = []
		for cell in row:
			_row.append(cell.value)
		result.append(_row)

	return result

def writeSheet(fileName="sample.xlsx",sheetName="Accounts",rows=rows):
	book = xlwt.Workbook()
	newSheet_1 = book.add_sheet(sheetName)

	for row_i,row in enumerate(rows):
		for i,cell in enumerate(row):
			print(row_i,i,cell)
			newSheet_1.write(row_i,i,cell)
	book.save(fileName)