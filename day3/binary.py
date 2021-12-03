import collections

Diagnostics = collections.namedtuple("Diagnostics", "gamma epsilon")


def diagnostic(filename):
    with open(filename, mode="r") as file:
        gamma = ""
        epsilon = ""
        lines = file.readlines()
        transposed_lines = zip(*lines)
        for bits in transposed_lines:
            bit_counts = collections.Counter()
            bit_counts["0"] = 0  # can't use the initializer for integer value
            bit_counts["1"] = 0  # these are need in case a line is all 1 or 0
            bit_counts.update(bits)
            gamma += bit_counts.most_common()[0][0]
            epsilon += bit_counts.most_common()[1][0]
    return Diagnostics(int(gamma, base=2), int(epsilon, base=2))


if __name__ == "__main__":
    result = diagnostic("./day3/input.txt")
    print(result)
    print(result.gamma * result.epsilon)
