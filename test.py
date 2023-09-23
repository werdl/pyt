import pyt

def add(a: int|float, b: int|float) -> int|float:
    return a+b

o=pyt.pyt(add)
o.addvalues([0,0],0)
o.addvalues([1,34],35) 
o.addvalues([2,9],10)
o.run()



