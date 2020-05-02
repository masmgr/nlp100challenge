s = "I am an NLPer"

def word_n_gram(s, n):
    l = [w for w in s.split(" ")]
    return n_gram_from_list(l, n)

def char_n_gram(s, n):
    l = [c for c in s]
    return ["".join(cgram) for cgram in n_gram_from_list(l, n)]

def n_gram_from_list(l, n):
    return [l[i:i+n] for i in range(len(l)-1)]

print(word_n_gram(s, 2))
print(char_n_gram(s, 2))
