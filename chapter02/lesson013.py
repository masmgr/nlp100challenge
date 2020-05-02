import sys

def paste():
    data1 = []
    data2 = []

    with open("..\data\col1.txt") as f1:
        data1 = [line.strip() for line in f1]

    with open("..\data\col2.txt") as f2:
        data2 = [line.strip() for line in f2]

    with open("..\data\output_lesson013.txt", "w") as wf:
        for col1, col2 in zip(data1, data2):
            wf.write("{0}\t{1}\n".format(col1, col2))

if __name__ == "__main__":
    paste()
