
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
            print("{0}\t{1}".format(x.strip(),y.strip()))


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
    unittest.main()