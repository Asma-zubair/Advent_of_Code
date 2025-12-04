# Read the grid
grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

# Directions for the 8 neighbors
dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

accessible = 0

# Check every cell in the grid
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '@':
            continue

        count_neighbors = 0

        # Count '@' in the 8 directions
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    count_neighbors += 1

        # If fewer than 4 neighbors → accessible
        if count_neighbors < 4:
            accessible += 1

print("Accessible rolls:", accessible)
