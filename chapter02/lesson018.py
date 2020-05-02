import sys

def sort_by_num(path):
    with open(path) as f:
        return "".join(sorted([line for line in f], reverse=True, key=lambda d: int(d.split("\t")[2])))

if __name__ == "__main__":
    print(sort_by_num(sys.argv[1]))
