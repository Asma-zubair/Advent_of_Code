# Read the grid only from input.txt (no example inside code)
grid = []
with open("input2.txt") as f:
    for line in f:
        line = line.strip()
        if line != "":
            grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

# 8 directions
dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

total_removed = 0

while True:
    to_remove = []

    # find rolls that can be removed
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbors += 1

            if neighbors < 4:
                to_remove.append((r, c))

    # no more removable rolls
    if not to_remove:
        break

    # remove them all at once
    for r, c in to_remove:
        grid[r][c] = '.'

    total_removed += len(to_remove)

print("Total removed:", total_removed)
