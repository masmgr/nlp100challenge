import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def word_shuffle(w):
    if len(w) > 4:
        return w[0] + "".join(random.sample(list(w[1:-1]), len(w) - 2)) + w[-1]
    else:
        return w

print(" ".join([word_shuffle(w) for w in s.split(" ")]))

