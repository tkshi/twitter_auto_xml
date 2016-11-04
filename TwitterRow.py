# -*- coding: utf-8 -*- 

import sys
class TwitterRow:
	def __init__(self,twitterRow=[]):
		self.twitter_id = twitterRow[0]
		self.twitter_pass = twitterRow[1]
		self.twitter_email = twitterRow[2]
		self.phoneNumber = twitterRow[3] if len(twitterRow) == 4 else u'-'
	def dumpArray(self):
		result = [''] * 4
		result[0] = self.twitter_id
		result[1] = self.twitter_pass
		result[2] = self.twitter_email
		result[3] = self.phoneNumber
		return result
if __name__ == '__main__':
	gr = TwitterRow(twitterRow=['username','password','email@adress.com'])
	print(gr.dumpArray())
