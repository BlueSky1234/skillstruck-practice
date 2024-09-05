code = { "a": "q", "b": "x", "c": "j", "d": "z", "e": "v", "f": "p", "g": "k", "h": "u", "i": "w", "j": "y", "k": "b", "l": "t", "m": "r", "n": "d", "o": "h", "p": "s", "q": "e", "r": "a", "s": "i", "t": "f", "u": "l", "v": "g", "w": "o", "x": "n", "y": "c", "z": "m", " ": "1" }

text = input()
result = []

for x in text:
    result.append(code.get(x, " "))
print("".join(result))
