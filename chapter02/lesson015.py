import sys

def tail(path, n):
    with open(path) as f:
        return "".join([line for line in f][-n:])

if __name__ == "__main__":
    print(tail(sys.argv[1], int(sys.argv[2])))
