#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}\n{:d} + {:d} = {:d}\n{:d} + {:d} = {:d}\n{:d} + {:d} = {:d}\n".format(a, b, add(a, b), a, b, sub(a, b), a, b, mul(a, b), a, b, div(a, b))) 
