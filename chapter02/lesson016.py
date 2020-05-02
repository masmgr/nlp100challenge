import sys

def split(path, n):
    with open(path) as f:
        data = [line for line in f]
        return "\n".join(["".join(data[i:i+n]) for i in range(0, len(data), n)])

if __name__ == "__main__":
    print(split(sys.argv[1], int(sys.argv[2])))
