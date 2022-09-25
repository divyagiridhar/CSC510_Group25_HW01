import sys
import Utils
import Sym 
import Num
import Data
sys.path.insert(0, './code')

def test_the():
    Utils.oo(Utils.the)
    return True

def test_sym():
    sym = Sym.Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    Utils.oo({"mid": mode, "div": entropy})
    return mode == "a" and 1.37 <= entropy and entropy <= 1.38

def test_num():
    num = Num.Num()
    for i in range(1, 100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def test_bignum():
    num = Num.Num()
    Utils.the['nums'] = 32
    for i in range(1, 1000):
        num.add(i)
    res = dict(sorted(num.nums().items(), key=lambda item: item[1]))
    print(res.values())
    return 32 == len(num._has)

def test_data():
    d = Data.Data("../data/data.csv")
    for y in d.cols.y:
        Utils.oo(y)
    return True

def test_stats():
    data = Data.Data("../data/data.csv")
    def div(col):
        return col.div()
    
    def mid(col):
        return col.mid()
    print('xmid=', Utils.o(data.stats(2, data.cols.x, mid)))
    print('xdiv=', Utils.o(data.stats(3, data.cols.x, div)))
    print('ymid=', Utils.o(data.stats(2, data.cols.y, mid)))
    print('ymid=', Utils.o(data.stats(3, data.cols.y, div)))
    return True

def test_csv():
    global n 
    n=0
    
    def function_row(r):
        global n 
        n+=1
        return n if n>10 else Utils.oo(r)
    Utils.parse_csv("../data/data.csv", function_row)
    return True

test_the()
test_sym()
test_num()
test_bignum()
test_data()
test_stats()
test_csv()
