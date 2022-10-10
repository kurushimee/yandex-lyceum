import re
import sys

data = " ".join(list(map(str.strip, sys.stdin)))

narrative = []
interrogative = []
exclamatory = []

sentence = []
for word in re.findall(r"[\w-]+|[,.?!]", data):
    word = word.lower()
    if word in ".?!":
        if word == ".":
            narrative.extend(sentence)
        elif word == "?":
            interrogative.extend(sentence)
        elif word == "!":
            exclamatory.extend(sentence)
        sentence.clear()
    else:
        sentence.append(word)

both = set(narrative) & set(interrogative)
both = both - set(exclamatory)
print(" ".join(sorted(list(both))))
