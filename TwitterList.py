from TwitterRow import *

class TwitterList(list):
    def __init__(self,twitterList=[]):
    	for twitter in twitterList:
    		gm = TwitterRow(twitterRow=twitter)
    		self.append(gm)
    def dumpArray(self):
    	result = []
    	i = 0
    	for twitterRow in self:
    		print(i)
    		i = i + 1
    		result.append(twitterRow.dumpArray())
    	return result

if __name__ == '__main__':
	arg = [
    ['username','password','email@adress.com'],
    ['username','password','email@adress.com']
	]
	gl = TwitterList(twitterList=arg)
	print(gl.dumpArray())
	# print(gl.dumpArray())

