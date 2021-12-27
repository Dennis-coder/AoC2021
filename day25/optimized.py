def refactor_indata(indata):
    indata = indata.split()
    w, h = len(indata[0]), len(indata)
    east_sea_cucumbers = set()
    south_sea_cucumbers = set()
    for y in range(h):
        for x in range(w):
            if indata[y][x] == ">":
                east_sea_cucumbers.add((x,y))
            elif indata[y][x] == "v":
                south_sea_cucumbers.add((x,y))
    return (w, h, east_sea_cucumbers, south_sea_cucumbers)

def calc_a(indata):
    w, h, east_sea_cucumbers, south_sea_cucumbers = indata
    i = 0
    while True:
        movement = False
        new_east_sea_cucumbers = set()
        for x,y in east_sea_cucumbers:
            if ((x+1)%w,y) not in east_sea_cucumbers and ((x+1)%w,y) not in south_sea_cucumbers:
                new_east_sea_cucumbers.add(((x+1)%w,y))
                movement = True
            else:
                new_east_sea_cucumbers.add((x,y))
        east_sea_cucumbers = new_east_sea_cucumbers

        new_south_sea_cucumbers = set()
        for x,y in south_sea_cucumbers:
            if (x,(y+1)%h) not in east_sea_cucumbers and (x,(y+1)%h) not in south_sea_cucumbers:
                new_south_sea_cucumbers.add((x,(y+1)%h))
                movement = True
            else:
                new_south_sea_cucumbers.add((x,y))
        south_sea_cucumbers = new_south_sea_cucumbers

        i += 1
        if not movement:
            return i    

def calc_b(indata):
    w, h, east_sea_cucumbers, south_sea_cucumbers = indata
