from collections import defaultdict
import numpy as np

def count_intersections(hist, lines):
    # Add points in lines to the histogram and count the number of points that
    # belongs to two lines or more
    count = 0
    for p1, p2 in lines:
        # For each 2D point, round, cast to int and wrap in tuple
        tokenize = lambda x: tuple(x.round().astype(int))
        # For each point on the line between points p1 and p2
        for p in map(tokenize, np.linspace(p1, p2, abs(p1-p2).max()+1)):
            # If this point was already part of a previous line, add to count
            if hist[p] == 1:
                count += 1
            # Add point to histogram
            hist[p] += 1
    return count

def main():

    # Set of "straight" lines (extreme points share same x or same y)
    straight_lines = []
    # Set of "diagonal" lines (extreme points have distinct x and y)
    diagonal_lines = []

    while True:
        try:
            # Read and parse line
            x1, y1, x2, y2 = [int(x) for y in input().split(" -> ") for x in y.split(",")]
            p1, p2 = np.array([x1, y1]), np.array([x2, y2])
            # If line is "straight"
            if any(p1 == p2):
                straight_lines.append((p1, p2))
            # Else line is "diagonal"
            else:
                diagonal_lines.append((p1, p2))
        except Exception:
            break

    hist = defaultdict(int)
    # Count intersections between "straight" lines
    res1 = count_intersections(hist, straight_lines)
    # Count intersections between all lines
    res2 = res1 + count_intersections(hist, diagonal_lines)

    return res1, res2

p1, p2 = main()
print("Puzzle answer, part 1:", p1)
print("Puzzle answer, part 2:", p2)
