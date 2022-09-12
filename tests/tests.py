from cli import CLI
import unittest
from num import Num
from Sym import Sym
from config import t
from row import Row
from col import Col

class testReturnValues(unittest.TestCase):

    def testThe(self):
        obj = CLI()
        the = obj.cli(obj.the)
        t["nums"] = obj.the["nums"]
        print(obj.the)
        assert True
        print("!!!!!!   PASS    the     true")
    
    def testNum(self):
        t["nums"] = 1000
        numData = {"Cldrs":list(range(1,100+1))}
        for colName, data in numData.items():
            if colName[0].isupper():
                num = Num(0, colName)
                for value in data:
                    num.add(value)
                mode = num.mid()
                div = num.div()
                self.assertTrue(50 <= mode <= 52) and self.assertTrue(30.5 <= div <= 32)
                num.print_Num(div, mode)

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
                sym.print_Sym(entropy, mode)
                

    def testBigNum(self):
        t["nums"] = 32
        numData = {"Cldrs":list(range(1,1000+1))}
        for colName, data in numData.items():
            if colName[0].isupper():
                num = Num(0, colName)
                for value in data:
                    num.add(value)
            print(num._has)
            self.assertEqual(32, len(num._has))
            num.print_BigNum()
      
    
    def testCsv(self):
        n=0
        csv= Data("../data/source.csv")
            row()
            n = n+1
            if n>10:
                return
            else:
                num.print_Csv() 
        return true

    def testData(self):
        d = Data("../data/source.csv")
        for Col in pairs (d.items()):
            num.print_Data()
        return true
    
    def testStats(self):
        data = Data("../data/source.csv")
        div = Col.div()
        mid = Col.mid()
        num.print_Stats()
        return true

if __name__  == '__main__':
    unittest.main()
