class Operation:
    def plus(self,a,b):
        print("%d + %d = %d"%(a,b,a+b))
    def sub(self,a,b):
        print("%d - %d = %d"%(a,b,a-b))
    def mul(self,a,b):
        print("%d * %d = %d"%(a,b,a*b))
    def div(self,a,b):
        print("%d / %d = %d"%(a,b,a/b))

if  __name__ == "__main__":
    oper = Operation()
    oper.plus(3,2)
    oper.sub(3,2)
    oper.mul(3,2)
    oper.div(3,2)
