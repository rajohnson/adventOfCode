def location(filename):
    x, y, aim = 0, 0, 0
    with open(filename, mode="r") as file:
        for line in file:
            command, value = line.split()
            value = int(value)
            if command == "forward":
                x += value
                y += aim * value
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value
    return x, y


if __name__ == "__main__":
    result = location("input.txt")
    print(result)
    print(f"product = {result[0] * result[1]}")
