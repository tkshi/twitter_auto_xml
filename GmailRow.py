# -*- coding: utf-8 -*- 

import sys
class GmailRow:
	def __init__(self,gmailRow={}):
		if(isinstance(gmailRow, list)):
			print('row3',gmailRow[3])
			self.gmail_adress = gmailRow[0]
			self.gmail_pass = gmailRow[1]
			self.phone_number = gmailRow[2]
			self.used = gmailRow[3] if len(gmailRow) == 9 else u'未使用'
		elif(isinstance(gmailRow,dict)):
			self.gmail_adress = gmailRow['gmail_adress']
			self.gmail_pass = gmailRow['gmail_pass']
			self.phone_number = gmailRow['phone_number']
			self.used = u'使用済み'
	def dumpArray(self):
		print(self)
		result = [''] * 4
		result[0] = self.gmail_adress
		result[1] = self.gmail_pass
		result[2] = self.phone_number
		result[3] = self.used
		return result
if __name__ == '__main__':
	gr = GmailRow(gmailRow={'gmail_adress':"hello@gamil.com",'gmail_pass':"aaa",'phone_number':'0000000'})
	print(gr.gmail_adress)
	gr.used = 'treu'
