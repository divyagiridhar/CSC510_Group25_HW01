class data:
    def __init__(self, src):
        self.cols = None     #summaries of data
        self.rows = {}      #kept data
        
    if type(src) == str:
        csv(src, data().add(row))
    else:
        for _, row in (src or {}):
            data().add(row)
        
    def add(xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            if xs.cells:
                row = push(self.rows, xs)
            else:
                row = push(self.rows, Row(xs))
            for _, todo in (self.cols.x, self.cols.y):
                for _, col in todo.items():
                    col.append(row.cells[col.at])
    
    
    
    def stats(places,showCols,fun,t,v):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for _, col in showCols:
            v = fun(col)
            v = (type(v) == float) and rnd(v, places) or v
            t[col.name] = v
        return t
    
