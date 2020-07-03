# P1
with open("input.txt") as input_file:
    freqs = [int(x) for x in input_file.readlines()]

print(f"P1 Answer: {sum(freqs)}")

# P2

freq_sum = sum(freqs)

cycled_freqs = [sum(freqs[: i + 1]) for i in range(len(freqs))]


def dupes_exist(cycled_freqs):
    return not len(list(set(cycled_freqs))) == len(cycled_freqs)


while not dupes_exist(cycled_freqs):
    next_loop = list(map(lambda x: x + freq_sum, cycled_freqs[-len(freqs) :]))
    cycled_freqs = cycled_freqs + next_loop

for val in cycled_freqs[-len(freqs) :]:
    if val in cycled_freqs[: len(freqs)]:
        print(f"P2 Answer: {val}")
        break
