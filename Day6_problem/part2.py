
lines = open("input2.txt").read().splitlines()


max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len, " ") for line in lines]

rows = len(lines)
last_row = rows - 1  

grand_total = 0
col = max_len - 1    

while col >= 0:

    # Check if this column is a separator (all spaces)
    is_separator = True
    for r in range(rows):
        if lines[r][col] != " ":
            is_separator = False
            break

    if is_separator:
        col -= 1
        continue

    
    end_col = col

    # Move left until we hit a full blank column
    while col >= 0:
        empty_column = True
        for r in range(rows):
            if lines[r][col] != " ":
                empty_column = False
                break

        if empty_column:
            break

        col -= 1

    start_col = col + 1

    
    numbers = []
    # For each column inside this block
    for c in range(start_col, end_col + 1):
        digits = ""
        for r in range(0, last_row):
            ch = lines[r][c]
            if ch != " ":
                digits += ch
        if digits != "":
            numbers.append(int(digits))

    
    op = ""
    for c in range(start_col, end_col + 1):
        if lines[last_row][c] != " ":
            op = lines[last_row][c]
            break

    
    if op == "+":
        result = sum(numbers)
    else:
        result = 1
        for n in numbers:
            result *= n

    # Add to total
    grand_total += result

print(grand_total)
