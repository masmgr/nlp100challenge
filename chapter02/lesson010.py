import sys

def wc(path):
    with open(path) as f:
        return len(f.readlines())


if __name__ == "__main__":
    print(wc(sys.argv[1]))