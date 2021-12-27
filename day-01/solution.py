import numpy as np

def main():

    # Read data
    data = [int(input())]
    while True:
        try:
            data.append(int(input()))
        except Exception:
            break
    data = np.array(data)

    # How many values are greater than the previous value?
    nb_inc1 = (np.diff(data) > 0).sum()
    # Rolling mean of size 3: how many means are greater than the previous mean?
    nb_inc2 = (np.diff(np.convolve(data, [1]*3, "valid")) > 0).sum()

    # Return results
    return nb_inc1, nb_inc2

p1, p2 = main()
print("Puzzle answer, part 1:", p1)
print("Puzzle answer, part 2:", p2)
