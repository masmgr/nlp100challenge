import sys

def convert_tab(path):
    with open(path) as f:
        return "".join([line.replace("\t", " ") for line in f])

if __name__ == "__main__":
    print(convert_tab(sys.argv[1]))