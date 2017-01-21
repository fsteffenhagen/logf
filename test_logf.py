import logging
from logf import logF

logging.basicConfig(level=logging.DEBUG)

@logF(logLevel=logging.INFO)
def myFunction(a, b, c, d=1):
    if a > 0:
        myFunction(a-1, b, c, d)
    else:
        return

myFunction(10,20,30)
