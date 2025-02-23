from collections import Counter

a = "word"

b = "Word"

print(Counter(a), Counter(b.lower()), '   ', Counter(a)== Counter(b.lower()))



print(a == sorted(b.lower()), sorted(b))
