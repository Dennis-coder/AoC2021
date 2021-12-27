from collections import defaultdict

def refactor_indata(indata):
    algorithm, image = indata.split("\n\n")
    image = (*image.split(),)
    return (algorithm, image)

def calc(indata, iterations):
    algorithm, image = indata
    pixels = defaultdict(lambda: 0)
    offsets = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
    for y, row in enumerate(image):
        for x, char in enumerate(row):
            pixels[(x,y)] = 0 if char == "." else 1
    for i in range(iterations):
        minx = min(x for x, _ in pixels)
        maxx = max(x for x, _ in pixels)
        miny = min(y for _, y in pixels)
        maxy = max(y for _, y in pixels)

        if algorithm[0] == "#" and algorithm[-1] == "." and i % 2 == 0:
            new_pixels = defaultdict(lambda: 1)
        else:
            new_pixels = defaultdict(lambda: 0)

        for y in range(miny - 1, maxy + 2):
            for x in range(minx - 1, maxx + 2):
                index = 0
                for dx,dy in offsets:
                    index <<= 1
                    index += pixels[(x+dx,y+dy)]
                new_pixels[(x,y)] = 0 if algorithm[index] == "." else 1

        pixels = new_pixels
    return sum(pixels.values())

def calc_a(indata):
    return calc(indata, 2)

def calc_b(indata):
    return calc(indata, 50)