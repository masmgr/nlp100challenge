import sys

def head(path, n):
    with open(path) as f:
        return "".join([line for line in f][-n:])

if __name__ == "__main__":
    print(head(sys.argv[1], int(sys.argv[2])))
