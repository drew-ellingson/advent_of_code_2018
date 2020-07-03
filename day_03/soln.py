from collections import Counter


class Claim:
    def __init__(self, claim_string):
        self.number = claim_string[1 : claim_string.index("@") - 1]

        corner_string = claim_string[
            claim_string.index("@") + 1 : claim_string.index(":")
        ]
        corner_list = [int(x) for x in corner_string.split(",")]
        self.corner = (corner_list[0], corner_list[1])

        size_string = claim_string[claim_string.index(":") + 1 :]
        size_list = [int(x) for x in size_string.split("x")]
        self.size = (size_list[0], size_list[1])

        self.area_coords = self.get_coords(self.corner, self.size)
        self.overlaps = None

    def get_coords(self, claim_corner, claim_size):
        x, y = claim_corner
        height, width = claim_size[0], claim_size[1]
        area_coords = [(x + i, y + j) for i in range(height) for j in range(width)]
        return area_coords


with open("input.txt") as input_file:
    claims = [claim.strip() for claim in input_file.readlines()]
    claims = [Claim(claim) for claim in claims]

all_claim_coords = []
for claim in claims:
    all_claim_coords = all_claim_coords + claim.area_coords

claim_coords_hist = Counter(all_claim_coords)

overlaps = {k: v for k, v in claim_coords_hist.items() if v > 1}

print(f"P1 Answer: {len(overlaps)}")

# P2

for claim_1 in claims:
    for claim_2 in claims[claims.index(claim_1) + 1 :]:
        overlap = len(list(set(claim_1.area_coords) & set(claim_2.area_coords)))
        if overlap > 0:
            claim_1.overlaps = True
            claim_2.overlaps = True
    if claim_1.overlaps is None:
        claim_1.overlaps = False
        print(f"P2 Answer: {claim_1.number}")
        break
