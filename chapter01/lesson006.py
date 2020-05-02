
def word_n_gram(s, n):
    l = [w for w in s.split(" ")]
    return n_gram_from_list(l, n)

def char_n_gram(s, n):
    l = [c for c in s]
    return ["".join(cgram) for cgram in n_gram_from_list(l, n)]

def n_gram_from_list(l, n):
    return [l[i:i+n] for i in range(len(l)-1)]

s_X = "paraparaparadise"
s_Y = "paragraph"

ngram_X = char_n_gram(s_X, 2)
ngram_Y = char_n_gram(s_Y, 2)

# 和集合
print(set(ngram_X) | set(ngram_Y))

# 積集合
print(set(ngram_X) & set(ngram_Y))

# 差集合
print(set(ngram_X) - set(ngram_Y))
print(set(ngram_Y) - set(ngram_X))

# ’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
print(True if "se" in ngram_X else False)
print(True if "se" in ngram_Y else False)

