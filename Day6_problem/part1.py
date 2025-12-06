
lines = open("input.txt").read().splitlines()


max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len, " ") for line in lines]


last_row_index = len(lines) - 1

grand_total = 0
col = 0

while col < max_len:

    
    is_separator = True
    for row in range(len(lines)):
        if lines[row][col] != " ":
            is_separator = False
            break

    if is_separator:
        col += 1
        continue

    
    start_col = col

    
    while col < max_len:
        empty_column = True
        for row in range(len(lines)):
            if lines[row][col] != " ":
                empty_column = False
                break

        if empty_column:
            break

        col += 1

    end_col = col - 1

    
    numbers = []
    for row in range(last_row_index):  
        part = lines[row][start_col:end_col + 1].strip()
        if part != "":
            numbers.append(int(part))

    
    op = lines[last_row_index][start_col:end_col + 1].strip()

    
    if op == "+":
        result = sum(numbers)
    else:
        result = 1
        for n in numbers:
            result *= n

    
    grand_total += result


print(grand_total)
