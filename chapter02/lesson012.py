import sys

def output_separate(path):
    data = []
    with open(path) as f:
        data = [line.strip().split("\t") for line in f]

    with open("..\data\col1.txt", mode="w") as f1:
        for cols in data:
            f1.write(cols[0] + "\n")

    with open("..\data\col2.txt", mode="w") as f2:
        for cols in data:
            f2.write(cols[1] + "\n")
            

if __name__ == "__main__":
    output_separate(sys.argv[1])
