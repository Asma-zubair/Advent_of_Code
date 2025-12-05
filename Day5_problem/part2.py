def solve():
    ranges = []

    
    with open("input2.txt", "r") as f:
        for line in f:
            line = line.strip()
            if "-" in line:
                try:
                    a, b = line.split("-")
                    a, b = int(a), int(b)
                    if a > b:
                        a, b = b, a
                    ranges.append((a, b))
                except:
                    pass 

    
    ranges.sort()

    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]

           
            if start <= last_end + 1:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

    
    total_fresh = sum((end - start + 1) for start, end in merged)

    print("Total fresh ingredient IDs:", total_fresh)


if __name__ == "__main__":
    solve()
