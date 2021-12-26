def refactor_indata(indata):
    algorithm, image = indata.split("\n\n")
    image = (*image.split(),)
    return (algorithm, image)

def get_index(x,y, lit_pixels, size, rest):
    offsets = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
    binary = ""
    for dx,dy in offsets:
        binary += "1" if (x+dx,y+dy) in lit_pixels else "0" if (size[0][0] <= x+dx <= size[0][1] and size[1][0] <= y+dy <= size[1][1]) or rest == "." else "1"
    return int(binary, 2)

def calc_a(indata):
    algorithm, image = indata
    lit_pixels = set()
    for y, row in enumerate(image):
        for x, char in enumerate(row):
            if char == "#":
                lit_pixels.add((x,y))
    size = ((0,len(image[0]) - 1),(0,len(image) - 1))
    rest = "."
    for _ in range(2):
        new_lit_pixels = set()
        (x_low, x_high),(y_low, y_high) = size
        for y in range(y_low - 1, y_high + 2):
            for x in range(x_low - 1, x_high + 2):
                index = get_index(x, y, lit_pixels, size, rest)
                char = algorithm[index]
                if char == "#":
                    new_lit_pixels.add((x,y))
                    x_low = min((x_low, x))
                    x_high = max((x_high, x))
                    y_low = min((y_low, y))
                    y_high = max((y_high, y))
        size = ((x_low, x_high),(y_low, y_high))
        lit_pixels = new_lit_pixels
        rest = "." if algorithm[0 if rest == "." else -1] == "." else "#"
    return len(lit_pixels)

def calc_b(indata):
    algorithm, image = indata