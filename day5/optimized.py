def refactor_indata(indata):
    lines = (*[(*[(*[int(z) for z in y.split(",")],) for y in x.split(" -> ")],) for x in indata.split("\n")],)
    return lines

def calc_a(lines):
    seen = set()
    seen_twice = set()
    count = 0
    for ((x1, y1), (x2, y2)) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1,y) not in seen:
                    seen.add((x1,y))
                elif (x1,y) not in seen_twice:
                    seen_twice.add((x1,y))
                    count += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x,y1) not in seen:
                    seen.add((x,y1))
                elif (x,y1) not in seen_twice:
                    seen_twice.add((x,y1))
                    count += 1

    return count

def calc_b(lines):
    count_dict = {}
    count = 0
    for ((start_x, start_y), (stop_x, stop_y)) in lines:
        if start_x == stop_x:
            x = start_x
            it = range(start_y, stop_y + 1) if start_y < stop_y else range(stop_y, start_y + 1)
            for y in it:
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1
        elif start_y == stop_y:
            y = start_y
            it = range(start_x, stop_x + 1) if start_x < stop_x else range(stop_x, start_x + 1)
            for x in it:
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1
        else:
            for i in range(abs(start_x - stop_x) + 1):
                x = start_x + i if start_x < stop_x else start_x - i
                y = start_y + i if start_y < stop_y else start_y - i
                if (x,y) in count_dict:
                    if count_dict[(x,y)] == 1:
                        count += 1
                    count_dict[(x,y)] += 1
                else:
                    count_dict[(x,y)] = 1

    return count