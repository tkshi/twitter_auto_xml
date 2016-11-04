from GmailRow import *
class GmailList(list):
    def __init__(self,gmailList=[]):
    	for gmail in gmailList:
    		gm = GmailRow(gmailRow=gmail)
    		self.append(gm)
    def dumpArray(self):
    	result = []
    	i = 0
    	for gmailRow in self:
    		print(i)
    		i = i + 1
    		result.append(gmailRow.dumpArray())
    	return result

if __name__ == '__main__':
	arg = [
	{'gmail_adress':"hello@gamil.com",'gmail_pass':"aaa",'phone_number':'0000000'},
	{'gmail_adress':"hello@gamil.com",'gmail_pass':"aaa",'phone_number':'0000000'},
	]
	gl = GmailList(gmailList=arg)
	print(gl[0])
	# print(gl.dumpArray())
