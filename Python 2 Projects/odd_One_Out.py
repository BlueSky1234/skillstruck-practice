phrase = input(" ").strip()
words = [word[0] for word in phrase.split()]
common = [(letter, words.count(letter)) for letter in words]
greatest_common = max(common, key = lambda x: x[1])

print(" ".join([x for x in phrase.split() if x.startswith(greatest_common[0])]))
