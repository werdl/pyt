
class test:
    def __init__(self,fun):
        self.func=fun
        self.failed=0
        self.passed=0
    def exp(self,msg):
        print(msg)
        self.failed+=1
    def addvalues(self,params: list,return_val):
        self.params=params
        self.expected_return=return_val
    def run(self):
        def wrapper(args):
            return self.func(*args)
        return_code=wrapper(self.params)
        if return_code!=self.expected_return:
            self.exp(f"Expecting {self.expected_return}, got {return_code}")
        else:
            self.passed+=1
    def end(self):
        print(f"""Results are in!
FAILED tests: {self.failed}
PASSED tests: {self.passed}

PASS rate: {100 * float(self.passed)/float(self.failed+self.passed)}
""")
def x(a,b):
    return a+b

p=test(x)

p.addvalues([3,2],5)
p.run()
p.end()