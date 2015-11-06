import sys
if len(sys.argv[0]) == 1:
    print("usage: python3 solution.py OP1 OP2")
else:
    x = (sys.argv[1])
    y = (sys.argv[2])
    print(int(x)-int(y))
