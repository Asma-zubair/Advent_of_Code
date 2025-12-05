# Read the whole input
text = open("input.txt").read().strip()

# Split into two parts
parts = text.split("\n\n")

# First part: ranges
range_lines = parts[0].split("\n")
ranges = []
for line in range_lines:
    start, end = line.split("-")
    start = int(start)
    end = int(end)
    ranges.append((start, end))

# Second part: ingredient IDs
id_lines = parts[1].split("\n")
ids = [int(x) for x in id_lines]

fresh_count = 0

# Check each ID
for x in ids:
    is_fresh = False

    # Check if x fits in any range
    for r in ranges:
        a = r[0]
        b = r[1]
        if a <= x <= b:
            is_fresh = True
            break  # no need to check other ranges
    
    if is_fresh:
        fresh_count += 1

print(fresh_count)
