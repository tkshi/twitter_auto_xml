# -*- coding: utf-8 -*- 
import sys
sys.path.insert(0, '/Users/takashi/Projects/twitter_auto_login')
from Twitter import *
from Gmail import *
from Excel import *
from GmailList import *
result = getSheet(fileName="./uploads/gmail.xlsx",sheetName="Accounts")

gl = GmailList(gmailList=result)
# print(gl[0].dumpArray())
result = gl.dumpArray()
# print(reuslt)

# for row in result:
# 	# print(result[0])
# 	if row[0] == u'GoogleID':
# 		row.append(u'使用済み')
# 		continue
# 	gmail_phone_number = row[3]
# 	gmail_pass = row[1]
# 	gmail_adress = row[0]
# 	gm = Gmail(gmail_adress=gmail_adress,gmail_pass=gmail_pass)
	# tw = Twitter(twitter_id=twitter_id,twitter_pass=twitter_pass,twitter_email=twitter_email)
	# print(tw.getLoginStatus())
	# if tw.getLoginStatus() == True:
	# 	row.append("success")
	# else:
	# 	row.append("error")
	# tw.close()

# import xlwt
 
# book = xlwt.Workbook()
# book.add_sheet('NewSheet_1')
# book.save('sample.xls')

writeSheet(fileName="./uploads/gmail_out.xls",sheetName='Accounts',rows=result)