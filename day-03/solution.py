import numpy as np

def convert(x):
    # Convert a bit array to a string and then convert to decimal

    return int("".join([str(y) for y in x.astype(int)]), 2)

def filter(x, cmp_func):
    # For each position, filter the bits

    for i in range(x.shape[1]):
        # If all the bits are the same, go to the next position
        if x[:, i].sum() in [0, x.shape[0]]: continue

        # Depending on the comparison function, filter on the most common
        # bit or least common bit
        bit = cmp_func(x[:, i].sum(), x.shape[0] / 2)
        x = x[x[:, i] == bit]

    return convert(x[0,:])

def main():

    # Read data
    data = []
    while True:
        try:
            data.append([int(x) for x in input()])
        except Exception:
            break
    data = np.array(data)

    # Keep the most common bits
    gr = convert(data.sum(axis=0) > data.shape[0] / 2)
    # Keep the least common bits
    er = convert(data.sum(axis=0) < data.shape[0] / 2)
    # Product of the gamma rate and epsilon rate
    p1 = gr * er

    # Filter on the most common bit, ties are settled to 1
    ogr = filter(data, np.greater_equal)
    # Filter on the least common bit, ties are settled to 0
    csr = filter(data, np.less)
    p2 = ogr * csr

    return p1, p2

p1, p2 = main()
print("Puzzle answer, part 1:", p1)
print("Puzzle answer, part 2:", p2)
