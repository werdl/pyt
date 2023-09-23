
import inspect
from typing import Any

class pyt:
    def __init__(self,fun) -> None:
        """Pyt - an easy, simple testing framework. `fun` is thie function to be tested."""
        self.__func=fun
        self.__failed=0
        self.__passed=0
        self.__paramsret=[]
        self.__pass_rate=100
    def __str__(self) -> str:
        """Return pass rate"""
        return str(self.__pass_rate)
    def __repr__(self) -> str:
        return f"pyt.pass_rate={self.__pass_rate}"
    def __eq__(self,other) -> bool:
        if isinstance(other,pyt):
            return (self.__func,self.__failed,self.__passed,self.__paramsret,self.__pass_rate)==(other.__func,other.__failed,other.__passed,other.__paramsret,other.__pass_rate) # comparison
        return NotImplemented
    def __truncate(self,string: str,max):
        """Internal method. Formats function source"""
        if len(string)>max:
            l=string.split("\n")
            processed=f"{l[0]}\n...\n{l[-2]}\n"
            return processed
        else:
            return string
    def __fail(self,msg) -> None:
        """Fail test with `msg`."""
        print(msg)
        self.__failed+=1
    def __succ(self,msg: str) -> None:
        """Pass test with `msg`."""
        print(msg)
        self.__passed+=1
    def addvalues(self,params: list,return_val) -> None:
        """Add a set of values to the list of tests, where `params` is the paramaters to the function and `return_val` the return code."""
        self.__paramsret.append([params,return_val])
    def run(self,human_readable=True) -> float:
        """Run the stored tests, returns pass rate out of 1. If `human_readable`, print nice output"""
        def wrapper(args):
            return self.__func(*args)
        print(f"{self.__truncate(inspect.getsource(self.__func),400)}")
        for tup in self.__paramsret:
            try:
                return_code=wrapper(tup[0])
            except TypeError as e:
                self.__fail(f"Error - incorrect argument types provided. Provided - {tup[0]}, expected {tup[1]}, got {e}") 
                continue
            
            if return_code!=tup[1]:
                self.__fail(f"Expecting {tup[1]}, got {return_code} for parameters {tup[0]}")
            else:
                self.__succ(f"Passed with return {return_code} for parameters {tup[0]}")
        pass_rate=round(100*float(self.__passed)/float(self.__failed+self.__passed))
        if human_readable:
            print(f"""
FAILED tests: {self.__failed}
PASSED tests: {self.__passed}

Passed {self.__passed}/{self.__failed+self.__passed} tests ({pass_rate}%)
""")
        self.__pass_rate=pass_rate
        return pass_rate/100
