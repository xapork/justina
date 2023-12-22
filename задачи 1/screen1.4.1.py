def useless(s):
    return max(s) / len(s) if s else "Empty list"
s = [223123, 1, 2, 3, 4]
print(useless(s))