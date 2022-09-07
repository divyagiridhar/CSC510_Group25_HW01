import math
import random
import statistics as sts

theNums = 32

def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]


class Num:
    def __init__(self, c, s):
        self.n = 0  # items seen
        self.at = c if c else 0  # column  position
        self.name = s or ""  # column name
        self._has = {}  # kept data
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True

    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    def add(self, v):
        if v != "?":
            v = float(v)
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < theNums:
                pos = 1 + len(self._has)
            elif random.random() < theNums / self.n:
                pos = random.random(len(self._has))
                self._has[pos] = v
                
            self.isSorted = False

    def div(self):
        a = self.nums()
        return sts.stdev(a)

    def mid(self):
        return per(self.nums(), 0.5)
