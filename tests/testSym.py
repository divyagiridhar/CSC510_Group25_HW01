import unittest
from finalSym import Sym

class testReturnValues(unittest.TestCase):

    def testSym(self):
        symFreq = {"origin":["a", "a", "a", "a", "b", "b", "c"]}
        for colName, data in symFreq.items():
            if colName[0].islower():
                # This column is a symbol
                sym = Sym(0, colName)
                for value in data:
                    sym.add(value)
                mode = sym.mid()
                entropy = sym.div()
                entropy = (1000*entropy) // 1/1000
                self.assertEqual(mode, "a") and self.assertTrue(1.37 <= entropy <= 1.38)

if __name__  == '__main__':
    unittest.main()

