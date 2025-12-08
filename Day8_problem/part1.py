

# This function finds the parent (representative) of a node
def find_parent(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  
        x = parent[x]
    return x

# This function joins two sets (union)
def union(parent, size, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if pa == pb:
        return

    # attach smaller tree to larger tree
    if size[pa] < size[pb]:
        pa, pb = pb, pa

    parent[pb] = pa
    size[pa] += size[pb]


points = []
with open("input.txt", "r") as f:
    for line in f:
        x, y, z = line.strip().split(",")
        points.append((int(x), int(y), int(z)))

n = len(points)

# Step 2: Create a list of all pair distances
pairs = []  

for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]

        
        d2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

        pairs.append((d2, i, j))

# Step 3: Sort all pairs by distance
pairs.sort(key=lambda x: x[0])

# Step 4: Prepare Union–Find arrays
parent = list(range(n))
size = [1] * n

# Step 5: Connect the first 1000 closest pairs
for k in range(1000):
    d2, i, j = pairs[k]
    union(parent, size, i, j)


component_count = {}

for i in range(n):
    p = find_parent(parent, i)
    if p not in component_count:
        component_count[p] = 0
    component_count[p] += 1


sizes = sorted(component_count.values(), reverse=True)


while len(sizes) < 3:
    sizes.append(1)


answer = sizes[0] * sizes[1] * sizes[2]

print("Answer =", answer)
