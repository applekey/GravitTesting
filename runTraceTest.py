
####################
# Configuration
#     
####################
import unittest

gravitProgramBin = ''

####################
# Test Expected Data
#
####################
ObjData = {
	'bunny': ((0,'fileLocationLayer0'),
			  (1,'fileLocationLayer1'),
			  (2,'fileLocationLayer2'),	
			  (3,'fileLocationLayer3'))	
}

validateFileName = 'validation'

####################
# Tests
#
####################
def isSame(a,b, errorMargin):
    if a == b:
        return true;


def textDiff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        for x,y in zip(f1,f2):
            ## do some matching here
            f1Vals = x.strip().split(',')
            f2Vals = y.strip().split(',')
            f1Vals = [ float(f1val) for f1val in f1Vals]
            f2Vals = [ float(f2val) for f2val in f2Vals]
            for i in range(len(f1Vals)):
                if f1Vals[i] == f2Vals[i]:
                    print 'difference, file1: '+str(f1Vals[i]) + ' , file 2: ' + str(f2Vals[i])


def testLayer(obj, layer):
    expectedResults = ObjData[obj]
    for result in expectedResults:
        if result[0] == layer:
            textDiff(validateFileName, result[1])



class MyTest(unittest.TestCase):
    def testOBJLayers(self):
    	layers = 3
    	for layer in range(layers):
        	self.assertEqual(testLayer('blah',layer), layer+1, 'Layer: ' + str(layer) + ' is not correct.' )


if __name__ == '__main__':
    file1 = '/home/users/applekey/documents/gravit/build/validation'
    file2 = '/home/users/applekey/documents/gravit/build/validation'
    textDiff(file1,file2)
    exit()
    unittest.main()