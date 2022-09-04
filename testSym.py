from Sym import Sym
def testSym():
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
            return mode == "a" and 1.37 <= entropy <= 1.38
