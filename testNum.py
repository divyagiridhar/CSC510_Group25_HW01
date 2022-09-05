def testNum(self):
    num = num()
    for i in range(1,100):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    self.assertTrue(50 <= mid <= 52) and self.assertTrue(30.5 <= div <= 32)
