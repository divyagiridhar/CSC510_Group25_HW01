import re
import Sym
import Num

class Cols:
    def __init__(self, names):
        self.names=names  # all column names
        self.all=[]       # all the columns (including the skipped ones)
        self.klass=None   # the single dependent klass column (if it exists)
        self.x=[]         # independent columns (that are not skipped)
        self.y=[]         # depedent columns (that are not skipped)
        
        for c in range(0, len(names)):
            s =  re.sub('\n', '' , names[c]) 
            if s[0].isupper():
                col = Num.Num(c, s)
            else:
                col = Sym.Sym(c, s)

            if s[-1] in ["+", "-", "!"]:
                self.y.append(col) 
            else:
                self.x.append(col)
            if "!$" in s:
                self.klass = col
