# -*- coding: utf-8 -*- 
import sys
sys.path.insert(0, '/Users/takashi/Projects/twitter_auto_login')
from Twitter import *
from Excel import *
result = getSheet(fileName="./uploads/twitter.xlsx",sheetName="Accounts")


for row in result:
	print(result[0])
	if row[0] == u'Login':
		row.append('Login-status')
		continue
	twitter_id = row[0]
	twitter_pass = row[1]
	twitter_email = row[2]
	tw = Twitter(twitter_id=twitter_id,twitter_pass=twitter_pass,twitter_email=twitter_email)
	print(tw.getLoginStatus())
	if tw.getLoginStatus() == True:
		row.append("success")
	else:
		row.append("error")
	tw.close()