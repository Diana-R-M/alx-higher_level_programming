#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)


if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))
for idx, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(idx, sys.argv[idx]))
