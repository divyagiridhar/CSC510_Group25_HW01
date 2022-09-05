import math
import random

the = {}


def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]


class num:
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
            pass
            # table.sort(self._has)
        else:
            self.isSorted = True
        return self._has

    def add(self, v):
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < the.nums:
                pos = 1 + len(self._has)
            elif random.random() < the.nums / self.n:
                pos = random.random(len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = float(v)

    def div(self):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        return per(self.nums(), 0.5)
