class Point:
    def __init__(self, coord):
        self.coord = coord
        self.closest_obj = None
        self.is_boundary = None
        self.within_safety_range = None


class Grid:
    def __init__(self, obj_coords):
        self.obj_coords = obj_coords

        x_coords = [coord[0] for coord in obj_coords]
        y_coords = [coord[1] for coord in obj_coords]

        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)

        grid = [
            Point((i, j))
            for i in range(x_min, x_max + 1)
            for j in range(y_min, y_max + 1)
        ]

        for point in grid:
            point.closest_obj = self.get_closest_obj(point)
            point.is_boundary = point.coord[0] in [x_min, x_max] or point.coord[1] in [
                y_min,
                y_max,
            ]
            point.within_safety_range = self.get_total_dist(point) < 10000

        self.grid = grid

    def manhattan_distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def get_closest_obj(self, grid_point):
        # want to account for ties
        # closest_obj = min(self.obj_coords, key=lambda x: self.manhattan_distance(grid_point, x))

        closest_points = []
        min_dist = None
        for x in self.obj_coords:
            cur_dist = self.manhattan_distance(x, grid_point.coord)
            if min_dist is None or cur_dist < min_dist:
                closest_points = [x]
                min_dist = cur_dist
            elif min_dist == cur_dist:
                closest_points.append(x)

        if len(closest_points) == 1:
            return closest_points[0]
        else:
            return None

    def count_closest(self, obj):
        return len(list(filter(lambda x: x.closest_obj == obj, self.grid)))

    def get_total_dist(self, grid_point):
        return sum(
            [self.manhattan_distance(grid_point.coord, x) for x in self.obj_coords]
        )


if __name__ == "__main__":
    with open("input.txt") as input_file:
        coords_raw = [line.strip().split(",") for line in input_file.readlines()]
        coordinates = [(int(x), int(y)) for [x, y] in coords_raw]

    grid = Grid(coordinates)
    boundary_points = list(filter(lambda x: x.is_boundary, grid.grid))

    finite_coords = list(
        filter(
            lambda x: x not in [pt.closest_obj for pt in boundary_points], coordinates
        )
    )

    safest_coord = max([grid.count_closest(x) for x in finite_coords])

    print(f"P1 Answer: {safest_coord}")

    within_safety = list(filter(lambda x: x.within_safety_range, grid.grid))

    print(f"P2 Answer: {len(within_safety)}")
