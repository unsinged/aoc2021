import numpy as np

def main():

    # Read data
    data = []
    while True:
        try:
            # First column is for depth/aim, second column is for horizontal
            command, num = input().split()
            if command == "forward":
                data.append((0, int(num)))
            elif command == "down":
                data.append((int(num), 0))
            elif command == "up":
                data.append((-int(num), 0))
        except:
            break
    data = np.array(data)

    # Compute the sum of each column and multiply the results
    p1 = data.sum(axis=0).prod()

    # Compute the cumulative sum of the first column, multiplied by the second column
    data[:, 0] = np.cumsum(data[:, 0]) * data[:, 1]
    # Sum the result
    p2 = data.sum(axis=0).prod()

    return p1, p2

p1, p2 = main()
print("Puzzle answer, part 1:", p1)
print("Puzzle answer, part 2:", p2)
