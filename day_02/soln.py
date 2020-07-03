# P1
from collections import Counter

with open("input.txt") as input_file:
    words = [word.strip() for word in input_file.readlines()]

word_hists = [Counter(word) for word in words]


def n_match(word_hist, n):
    return n in word_hist.values()


two_match = len(list(filter(lambda x: n_match(x, 2), word_hists)))
three_match = len(list(filter(lambda x: n_match(x, 3), word_hists)))

print(f"P1 Answer: {two_match * three_match}")

# P2


def commons(word_1, word_2):
    matches = [word_1[i] == word_2[i] for i in range(len(word_1))]
    commons = [word_1[i] for i in range(len(word_1)) if matches[i]]
    return commons


for x in words:
    for y in words[words.index(x) + 1 :]:
        match = commons(x, y)
        if len(match) == len(x) - 1:
            print(f"P2 Answer: {''.join(match)}")
            break
        else:
            continue
