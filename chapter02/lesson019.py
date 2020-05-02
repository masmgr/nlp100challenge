import sys

def word_count(path):
    with open(path) as f:
        word_count_dict = {}
        for word in [line.split("\t")[0] for line in f]:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
        
        return "\n".join([
            "{0} {1}".format(k, v) for k, v in
            sorted([(k, v) for k, v in word_count_dict.items()], reverse=True, key=lambda item: item[1])
        ])

if __name__ == "__main__":
    print(word_count(sys.argv[1]))
