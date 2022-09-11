class data:
    def __init__(self, src):
        self.cols = None     #summaries of data
        self.rows = {}      #kept data
        
    if type(src) == str:
        csv(src, Row )
    else:
        pass
        
    def add(xs, row):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            if xs.cells:
                row = push(self.rows, xs)
            else:
                row = push(self.rows, Row(xs))
            for _, todo in (self.cols.x, self.cols.y):
                for _, col in todo.items():
                    pass
    
    
    
    def stats(places,showCols,fun,t,v)
        showCols, fun=showCols or self.cols.y, fun or "mid"
        t = {}
        for pass
            v=fun(col)
            v=type(v)=="number" and rnd(v,places) or V
            t[cols.name]=V
            return t
    
    
    