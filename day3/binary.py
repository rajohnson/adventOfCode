import collections

Diagnostics = collections.namedtuple("Diagnostics", "gamma epsilon")
Frequency = collections.namedtuple("Frequency", "most least")
Gas_rating = collections.namedtuple("Gas_rating", "o2 co2")


def get_bit_counts(lines):
    transposed_lines = zip(*lines)
    frequencies = []
    for bits in transposed_lines:
        bit_counts = collections.Counter()
        bit_counts["0"] = 0  # can't use the initializer for integer value
        bit_counts["1"] = 0  # these are need in case a line is all 1 or 0
        bit_counts.update(bits)
        frequencies.append(bit_counts)
    return frequencies


def get_most_and_least_common(lines):
    most_common = ""
    least_common = ""
    for bit_count in get_bit_counts(lines):
        (
            (first_key, first_count),
            (second_key, second_count),
        ) = bit_count.most_common(2)
        if first_count == second_count:
            most_common += "1"
            least_common += "0"
        else:
            most_common += first_key
            least_common += second_key
    return Frequency(most_common, least_common)


def get_gamma_epsilon(filename):
    gamma = ""
    epsilon = ""
    with open(filename) as file:
        lines = file.readlines()
        gamma, epsilon = get_most_and_least_common(lines)
    return Diagnostics(gamma, epsilon)


def filter_out_values(lines, mostFrequent):
    frequency_index = 0 if mostFrequent else 1
    bit_index = 1
    while len(lines) > 1:
        frequency = get_most_and_least_common(lines)
        lines = [
            value
            for value in lines
            if value[bit_index] == frequency[frequency_index][bit_index]
        ]
        bit_index += 1
    return lines.pop()


def get_oxygen(filename):
    most_frequent, _ = get_gamma_epsilon(filename)
    with open(filename) as file:
        oxygen = []
        co2 = []
        for line in file:
            if line[0] == most_frequent[0]:
                oxygen.append(line)
            else:
                co2.append(line)

        oxygen = filter_out_values(oxygen, True)
        co2 = filter_out_values(co2, False)

    return Gas_rating(int(oxygen, base=2), int(co2, base=2))


if __name__ == "__main__":
    result = get_oxygen("./day3/input.txt")
    print(result)
    print(result.o2 * result.co2)
