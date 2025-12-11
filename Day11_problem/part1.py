
graph = {}

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, outputs = line.split(":")
        graph[name.strip()] = outputs.strip().split()


# DFS function to count all paths from node to "out"
def count_paths(node):
    if node == "out":
        return 1  

    total = 0
    for nxt in graph.get(node, []):
        total += count_paths(nxt)

    return total



print(count_paths("you"))
