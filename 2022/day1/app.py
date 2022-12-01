with open("input.txt", "r") as data_in:
    inventory = []
    all_inventories = []
    for line in data_in:
        if len(line) == 1:  # new elf
            all_inventories.append(inventory)
            inventory = []
        else:
            inventory.append(int(line))
    if inventory:  # last one if the file doesn't have an extra newline
        all_inventories.append(inventory)

    print(sum(sorted([sum(inventory) for inventory in all_inventories])[-3:]))
