
from collections import defaultdict
import sys
import re

def parse_input(text):
    shapes = {}
    regions = []

    section = "shapes"
    current_shape = None
    current_lines = []

    for line in text.splitlines():
        line = line.rstrip("\n")

        if not line.strip():
            continue

    
        if re.match(r"^\d+x\d+:", line):
            section = "regions"
            w, h, rest = re.match(r"^(\d+)x(\d+):\s*(.*)$", line).groups()
            counts = list(map(int, rest.split()))
            regions.append((int(w), int(h), counts))
            continue

    
        if section == "shapes" and re.match(r"^\d+:\s*$", line):
        
            if current_shape is not None:
                shapes[current_shape] = current_lines
            current_shape = int(line[:-1])
            current_lines = []
            continue

    
        if section == "shapes":
            current_lines.append(line)


    if current_shape is not None:
        shapes[current_shape] = current_lines

    return shapes, regions


def shape_to_coords(shape_lines):
    coords = []
    for r, row in enumerate(shape_lines):
        for c, ch in enumerate(row):
            if ch == '#':
                coords.append((r, c))

    if not coords:
        return frozenset()
    minr = min(r for r,c in coords)
    minc = min(c for r,c in coords)
    norm = frozenset(((r - minr, c - minc) for r,c in coords))
    return norm

def rotate_coords(coords):

    rotated = [(c, -r) for r,c in coords]
    minr = min(r for r,c in rotated)
    minc = min(c for r,c in rotated)
    return frozenset(((r - minr, c - minc) for r,c in rotated))

def flip_coords(coords):

    flipped = [(r, -c) for r,c in coords]
    minr = min(r for r,c in flipped)
    minc = min(c for r,c in flipped)
    return frozenset(((r - minr, c - minc) for r,c in flipped))

def all_orientations(shape_lines):
    base = shape_to_coords(shape_lines)
    if not base:
        return {base}
    orientations = set()
    cur = base
    for _ in range(4):
        orientations.add(cur)
        orientations.add(flip_coords(cur))
        cur = rotate_coords(cur)

    return orientations

def placements_for_orientation(coords, region_w, region_h):
    if not coords:
        return []
    max_r = max(r for r,c in coords)
    max_c = max(c for r,c in coords)
    placements = []
    for top in range(0, region_h - max_r):
        for left in range(0, region_w - max_c):
        
            row_masks = defaultdict(int)
            for r,c in coords:
                rr = top + r
                cc = left + c
                row_masks[rr] |= (1 << cc)
        
            placements.append(tuple(sorted(row_masks.items())))
    return placements 

def placements_for_shape(shape_lines, region_w, region_h):
    orients = all_orientations(shape_lines)
    seen = set()
    all_places = []
    for coords in orients:
    
        place_list = placements_for_orientation(coords, region_w, region_h)
        for p in place_list:
        
            key = tuple(p)
            if key not in seen:
                seen.add(key)
                all_places.append(p)
    return all_places

def can_place_all(region_w, region_h, shapes, counts):

    piece_list = []
    shape_cells = {}
    for sidx, slines in shapes.items():
        coords = shape_to_coords(slines)
        shape_cells[sidx] = len(coords)

    total_cells_needed = sum(counts[i] * shape_cells[i] for i in range(len(counts)))
    if total_cells_needed > region_w * region_h:
        return False

    for i, cnt in enumerate(counts):
        piece_list.extend([i] * cnt)

    if not piece_list:
        return True


    placements_per_shape = {}
    for sidx in set(piece_list):
        placements_per_shape[sidx] = placements_for_shape(shapes[sidx], region_w, region_h)
        if not placements_per_shape[sidx]:
        
            if counts[sidx] > 0:
                return False



    static_info = []
    for sidx in set(piece_list):
        static_info.append((sidx, shape_cells[sidx], len(placements_per_shape[sidx])))

    static_info_map = {s: (area, pcnt) for s, area, pcnt in static_info}


    piece_list_sorted = sorted(piece_list, key=lambda s: (static_info_map[s][1], -static_info_map[s][0]))




    occupancy = [0] * region_h


    placements_array = {s: placements_per_shape[s] for s in placements_per_shape}

    N = len(piece_list_sorted)
    visited = 0


    def dfs(idx):
        nonlocal visited
        if idx == N:
            return True
        visited += 1
        s = piece_list_sorted[idx]
    
        for placement in placements_array[s]:
            conflict = False
            for rr, mask in placement:
                if occupancy[rr] & mask:
                    conflict = True
                    break
            if conflict:
                continue
        
            for rr, mask in placement:
                occupancy[rr] |= mask
            if dfs(idx + 1):
                return True
        
            for rr, mask in placement:
                occupancy[rr] ^= mask
        return False

    return dfs(0)

def main():
    fname = "input.txt"
    try:
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Cannot find {fname}. Please place your input in {fname} and run again.")
        sys.exit(1)

    shapes, regions = parse_input(text)



    max_shape_id = max(shapes.keys())

    shapes_list = {i: shapes[i] for i in range(0, max_shape_id + 1)}

    fit_count = 0
    for i, (w, h, counts) in enumerate(regions):
    
        if len(counts) < len(shapes_list):
        
            counts = counts + [0] * (len(shapes_list) - len(counts))
        print(f"Region #{i+1}: {w}x{h}, counts = {counts}")
        ok = can_place_all(w, h, shapes_list, counts)
        print("  -> FITS" if ok else "  -> DOES NOT FIT")
        if ok:
            fit_count += 1

    print(f"\nTotal regions that fit all presents: {fit_count} / {len(regions)}")

if __name__ == "__main__":
    main()
