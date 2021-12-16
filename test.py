from puzzles import day6_fish as fishes

days = 256

old_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

new_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

# Populate old fishes
for num in fishes:
    old_fish[num] += 1

# Start processing
for day in range(days):

    for index in range(0, (int(len(new_fish)))):
        if index == 0:
            # Number of fish to create
            create_fish = old_fish[index] + new_fish[index]

            # Remove old and new 0 fish. We will add these back in at 6 later
            old_fish[index] = 0
            new_fish[index] = 0
        elif index == 7:
            print("ran 7")
            old_fish[6] += create_fish

        # Minus one day from fish, aslong as index isn't 0
        if index > 0:
            if old_fish[index] > 0:
                store_fish = old_fish[index]
                old_fish[index - 1] += store_fish
                old_fish[index] = 0

            if new_fish[index] > 0:
                store_fish = new_fish[index]
                new_fish[index - 1] += store_fish
                new_fish[index] = 0

    # Create fish
    new_fish[8] += create_fish

total = 0
for index in range(0, (int(len(new_fish)))):
    total += old_fish[index]
    total += new_fish[index]

print(f"Total Fish: {total}")
