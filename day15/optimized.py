import heapq

def refactor_indata(indata):
    indata = indata.split("\n")
    w, h = len(indata[0]), len(indata)
    map = {}
    for y, row in enumerate(indata):
        for x, val in enumerate(row):
            map[(x,y)] = int(val)
    return (map, w, h)

def astar(map, start, goal, map_size):
    w, h = map_size
    pq = [(0, start)]
    seen = {(0,0)}

    neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
    while len(pq)>0:
        cost, current = heapq.heappop(pq)
        if current == goal:
            return cost   
        x, y = current
        for dx,dy in neighbors:
            x1,y1 = x+dx, y+dy 
            if 0 <= x1 <= goal[0] and 0 <= y1 <= goal[1] and (x1,y1) not in seen:
                yd, ym = divmod(y1, h)
                xd, xm = divmod(x1, w)
                seen.add((x1,y1))
                heapq.heappush(pq, (cost + (map[(xm, ym)] + xd + yd - 1) % 9 + 1, (x1,y1)))

def calc_a(indata):
    map, w, h = indata
    return astar(map, (0,0), (w - 1,  h - 1), (h, w))

def calc_b(indata):
    map, w, h = indata
    return astar(map, (0,0), (w*5 - 1,  h*5 - 1), (h, w))