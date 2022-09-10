# from main import for_sym
# from main import for_num
from num import Num
from Sym import Sym

def push(t, x):
    t[1 + len(t)] = x
    return x

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}
        
        for c, s in names.items():
            if s.isupper():
                Num(c, s)
                col = push(self.all, (c, s))
            
            if s.islower():
                Sym(c, s)
                col = push(self.all, (c, s))
            
            if not s.find(':'):
                if s.find('+' or '-'):
                    self.y.append(s)
                    push(s, col)
                else:
                    self.x.append(s)
                    push(s, col)
                    
            if s.find('!'):
                self.klass = col