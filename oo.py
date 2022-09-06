t={ 'abc' : '12', 'abcjdh': '47', 'dbsjbv': '75'}


def o(t):
    
    def show(k, v):
        if not str(k):
            print('hi')
            v = o(v)
            return len(t)==0 and format(":%s%s", k, v) or str(v)
    
    u={}
    for k, v in t.items():
        u[1+len(u)] = show(k, v)
        
    if len(t)==0:
        sorted(u)
        
    for i in range(len(t)):
        return '{'+str(list((t.values())[i]))+' '+'}'
    

def oo(t):
    print(o(t))
    return t


oo(t)