import collections


def count_increases(filename, window_len=1):
    count = 0
    last_window = collections.deque(maxlen=window_len)
    current_window = collections.deque(maxlen=window_len)
    with open(filename, mode="r") as file:
        for line in file:
            current_window.append(int(line))
            if (len(last_window) == window_len) and (
                sum(current_window) > sum(last_window)
            ):
                count += 1
            last_window.append(int(line))
    return count


if __name__ == "__main__":
    print(count_increases("./input.txt"))  # expect 1167
    print(count_increases("./input.txt", 3))  # expect 1130
