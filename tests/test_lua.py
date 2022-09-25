import sys

sys.path.append("../code/")

import pytest
import unittest
import Num
import Sym
import Utils
import random

class testReturnValues(unittest.TestCase):

    def oo(self,t):
        print(str(t))
        assert True

    def testThe(self):
        self.oo(Utils.the)
        assert True
        
    def testSym(self):
        sym = Sym.Sym()
        for val in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(val)
        mode = sym.mid()
        entropy = sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        self.oo({"mid": mode, "div": entropy})
        self.assertEqual(mode, "a") and self.assertTrue(1.37 <= entropy <= 1.38)

    def testNum(self):
        num = Num.Num()
        for i in range(1, 100):
            num.add(i)
        mid, div = num.mid(), num.div()
        print(mid, div)
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32


    def testBignum(self):
        num = Num.Num()
        Utils.the['nums'] = 32
        for i in range(1, 1000):
            num.add(i)
        self.oo(num.nums())
        self.assertEqual(32, len(num._has))
        
    def testCsv(self):
        n = 0
        def fun(row):
            n = n + 1
            if n > 10:
                return
            else:
                self.oo(row)
        csv("../data/source.csv", fun)
        return True

    def testData(self):
        d = Data("../data/source.csv")
        for _, col in enumerate(d.cols.y):
            self.oo(col)

    def testStats(self):
        data = Data("../data/source.csv")
        def div(col):
            if not isinstance(col, Num) or not isinstance(col, Num):
                return None
            return col.div()

    def mid(col):
            if not isinstance(col, Num) or not isinstance(col, Num):
                return None
            return col.mid()

        print("xmid\t" + self.oo(data.stats(2, data.cols.x, mid)))
        print("xdiv\t" + self.oo(data.stats(3, data.cols.x, div)))
        print("ymid\t" + self.oo(data.stats(2, data.cols.y, mid)))
        print("ydiv\t" + self.oo(data.stats(3, data.cols.y, div)))
        
        return True
        
        
if __name__  == '__main__':
    unittest.main()
