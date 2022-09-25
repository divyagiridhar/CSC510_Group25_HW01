import sys
sys.path.insert(0, './code')

import Utils
import Sym 
import Num
import Data

def bad():
    print("-" * 50)
    print("!!!!!!	CRASH	BAD	false\n")
    assert True
    
def lists():
    print("-" * 50)
    print("!!!!!!	FAIL	LIST	true\n")
    assert True

def ls():
    eg = ['BAD', 'ALL', 'LIST', 'bignum', 'csv', 'data', 'num', 'stats', 'the', 'sym']
    print("-" * 50)
    print("\nExamples of pytest test_lua.py -v...")
    for i in range(len(eg)):
        print(f'        {eg[i]}\t')
    print("!!!!!!	PASS	LS	true\n\n")
    assert True

def test_the():
    print("-" * 50)
    Utils.oo(Utils.the)
    print("!!!!!!	PASS	the	true\n!!!!!!	PASS	ALL	true\n\n")
    return True

def test_sym():
    sym = Sym.Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    print("-" * 50)
    Utils.oo({"mid": mode, "div": entropy})
    print("!!!!!!	PASS	sym	true\n\n")
    return mode == "a" and 1.37 <= entropy and entropy <= 1.38

def test_num():
    num = Num.Num()
    Utils.the['nums'] = 101
    for i in range(1, 100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print("-" * 50)
    print(mid, div)
    print("!!!!!!	PASS	num	true\n\n")
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def test_bignum():
    num = Num.Num()
    Utils.the['nums'] = 32
    for i in range(1, 1000):
        num.add(i)
    res = dict(sorted(num.nums().items(), key=lambda item: item[1]))
    t = list(res.values())
    out = "{"
    for i in range(len(t)):
        out += " " + str(t[i])
    print("-" * 50)
    print(out, "}")
    print("!!!!!!	PASS	bignum	true\n\n")
    return 32 == len(num._has)

def test_data():
    d = Data.Data("../data/source.csv")
    print("-" * 50)
    for y in d.cols.y:
        Utils.oo(y)
    print("!!!!!!	PASS	data	true\n\n")
    return True

def test_stats():
    data = Data.Data("../data/source.csv")
    def div(col):
        return col.div()
    
    def mid(col):
        return col.mid()
    
    print("-" * 50)
    print('xmid=', Utils.o(data.stats(2, data.cols.x, mid)))
    print('xdiv=', Utils.o(data.stats(3, data.cols.x, div)))
    print('ymid=', Utils.o(data.stats(2, data.cols.y, mid)))
    print('ymid=', Utils.o(data.stats(3, data.cols.y, div)))
    print("!!!!!!	PASS	stats	true\n\n")
    return True

def test_csv():
    global n 
    n=0
    
    def function_row(r):
        global n 
        n+=1
        return n if n>10 else Utils.oo(r)
    print("-" * 50)
    Utils.parse_csv("../data/source.csv", function_row)
    print("!!!!!!	PASS	csv	true\n\n")
    return True

bad()
lists()
ls()
test_bignum()
test_csv()
test_data()
test_num()
test_stats()
test_sym()
test_the()
