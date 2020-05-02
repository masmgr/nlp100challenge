s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print("".join([str(len(w)) for w in s.replace(",", "").replace(".", "").split(" ")]))
