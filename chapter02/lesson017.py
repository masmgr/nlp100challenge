import sys

def word_set(path, n):
    with open(path) as f:
        return set(line.split("\t")[0] for line in f)

if __name__ == "__main__":
    print(word_set(sys.argv[1], int(sys.argv[2])))
