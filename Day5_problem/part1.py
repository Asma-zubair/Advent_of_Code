
text = open("input.txt").read().strip()


parts = text.split("\n\n")


range_lines = parts[0].split("\n")
ranges = []
for line in range_lines:
    start, end = line.split("-")
    start = int(start)
    end = int(end)
    ranges.append((start, end))


id_lines = parts[1].split("\n")
ids = [int(x) for x in id_lines]

fresh_count = 0


for x in ids:
    is_fresh = False

    
    for r in ranges:
        a = r[0]
        b = r[1]
        if a <= x <= b:
            is_fresh = True
            break  
    
    if is_fresh:
        fresh_count += 1

print(fresh_count)
