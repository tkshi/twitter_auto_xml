# -*- coding: utf-8 -*- 
from Excel import *
result = getSheet(fileName="test.xlsx",sheetName="Accounts")

# for cell in row:

# import xlwt
 
# book = xlwt.Workbook()
# book.add_sheet('NewSheet_1')
# book.save('sample.xls')

writeSheet(fileName='output.xls',sheetName='Accounts',rows=result)