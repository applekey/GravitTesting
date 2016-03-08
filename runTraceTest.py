
####################
# Configuration
#     
####################
import unittest

gravitProgramBin = ''

####################
#  Test Expected Data
#
####################
ObjData = {
	'bunny': ((0,'fileLocationLayer0'),
			  (1,'fileLocationLayer1'),
			  (2,'fileLocationLayer2'),	
			  (3,'fileLocationLayer3'))	
}



def testLayer(obj, layer):
    return layer + 1

class MyTest(unittest.TestCase):
    def testOBJLayers(self):
    	layers = 3
    	for layer in range(layers):
        	self.assertEqual(testLayer('blah',layer), layer+1, 'Layer: ' + str(layer) + ' is not correct.' )


if __name__ == '__main__':
    unittest.main()