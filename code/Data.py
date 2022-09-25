import Cols
import Row
import Utils

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        self.n = None
        
        if type(src) == str:
            Utils.parse_csv(src, self.add)
        else:
            for row in (src or []):
                self.add(row)
        
    def add(self, xs):
        if not self.cols:
            self.cols = Cols.Cols(xs)
        else:
            if hasattr(xs,'cells'):
                self.rows.append(xs)
            else:
                row = Row.Row(xs)
                self.rows.append(row)
                for col in self.cols.x + self.cols.y:
                        col.add(row.cells[col.at])
    
    def stats(self, round_upto=2, showCols=None, fun=None):
        showCols, fun = showCols or self.cols.y, fun or self.cols.mid
        t = {}
        for col in showCols:
            v = fun(col) 
            if type(v) == float:
                v = round(v, round_upto)
            t[col.name] = v
        return t
