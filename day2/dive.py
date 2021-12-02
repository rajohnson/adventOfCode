def location(filename):
    x, y = 0, 0
    with open(filename, mode="r") as file:
        for line in file:
            command, value = line.split()
            value = int(value)
            if command == "forward":
                x += value
            elif command == "down":
                y += value
            elif command == "up":
                y -= value
    return x, y


if __name__ == "__main__":
    result1 = location("input.txt")
    print(result1)
    print(f"product = {result1[0] * result1[1]}")
