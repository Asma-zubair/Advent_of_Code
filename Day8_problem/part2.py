

# Function to find the parent/root of a node
def find_parent(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   
        x = parent[x]
    return x

# Function to join two groups
def union(parent, size, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if pa == pb:
        return False   

    # attach smaller tree to bigger tree
    if size[pa] < size[pb]:
        pa, pb = pb, pa

    parent[pb] = pa
    size[pa] += size[pb]

    return True




# 1. Read points from input.txt
points = []
with open("input.txt", "r") as f:
    for line in f:
        x, y, z = line.strip().split(",")
        points.append((int(x), int(y), int(z)))

n = len(points)

# 2. Make a list of all distances between all pairs
pairs = []  # (distance, i, j)

for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]

        
        d2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

        pairs.append((d2, i, j))

# 3. Sort by distance (smallest first)
pairs.sort(key=lambda x: x[0])

# 4. Prepare union-find
parent = list(range(n))
size = [1] * n
components = n  # initially, n separate circuits

last_pair = None

# 5. Keep connecting pairs until ALL points belong to ONE circuit
for d2, i, j in pairs:
    merged = union(parent, size, i, j)

    if merged:
        components -= 1

        
        if components == 1:
            last_pair = (i, j)
            break

# 6. Compute answer
if last_pair is not None:
    i, j = last_pair
    x1 = points[i][0]
    x2 = points[j][0]
    answer = x1 * x2

    print("The last connection was between:")
    print("Point", i, "=", points[i])
    print("Point", j, "=", points[j])
    print("\nAnswer =", answer)
else:
    print("Error: Could not find the final connecting pair.")
