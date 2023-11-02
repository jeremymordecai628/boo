!/usr/bin/env python3 
if _name_ == "_main_":
    import sys
    count = len(sys.argv) -1 
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else: 
        print("{}:{}".format(i + 1, sys.argv[i + 1]))

