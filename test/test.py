#from myfirstpythonpackage.cython_part._cython_code import fib_cpdef
from myfirstpythonpackage.python_part.fib import fib
from myfirstpythonpackage import fib_cpdef
import time


n=40
start = time.time()
print("cython output = ",fib_cpdef(n))
end = time.time()
print("time to test Cython Fib(",n,")= \n",end-start,"s")

start = time.time()
print("python output = ",fib(n))
end = time.time()
print("time to test Python Fib(",n,")= \n",end-start,"s")

