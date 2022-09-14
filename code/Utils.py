import math
import re
import sys
import random
from Num import Num 

help = " \n\
CSV : summarized csv file \n\
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\n\
USAGE: lua seen.lua [OPTIONS]\n\
OPTIONS:\n\
-e  --eg        start-up example                      = nothing\n\
-d  --dump      on test failure, exit with stack dump = false\n\
-f  --file      file with csv data                    = ../data/auto93.csv\n\
-h  --help      show help                             = false\n\
-n  --nums      number of nums to keep                = 512\n\
-s  --seed      random number seed                    = 10019\n\
-S  --seperator feild seperator                       = , "

def oo(t):
    print(str(t))
    return t

def message(status):
    if status:
        return "PASS"
    else:
        return "FAIL"

def coerce(s):
    s = s.strip()
    if s.isnumeric():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            if s == 'true' or s == 'TRUE' or s == 'True':
                return True
            elif s == 'false' or s == 'FALSE' or s == 'False':
                return False
            return re.match("\s*(.*)\s*", s).string

def csv(src, func, separator):
    lines = src.split('\n')
    for line in lines:
        t = []
        for ele in line.split(separator):
            ele = coerce(ele)
            t.append(ele)
        
def copy(t):
    if type(t) != dict:
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u

the = {}
pattern = r"-(\w+)[\s]*--[\s]*(\w+)[\s]*[^=]*[\s]*=[\s]*(.*)"
match_list = re.findall(pattern, help)
for k,x in match_list:
    the[k] = coerce(x)
