def refactor_indata(indata):
    operations = []
    for line in indata.splitlines():
        op, bounds = line.split()
        x,y,z = bounds.split(",")
        x1, x2 = [int(a) for a in x[2:].split("..")]
        y1, y2 = [int(a) for a in y[2:].split("..")]
        z1, z2 = [int(a) for a in z[2:].split("..")]
        operations.append((op == "on", Cube(x1, x2 + 1, y1, y2 + 1 , z1, z2 + 1)))
    return operations
    
class Cube:

    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
    
    def __repr__(self):
        return f"{self.x1=}, {self.x2=}, {self.y1=}, {self.y2=}, {self.z1=}, {self.z2=}"

    def size(self):
        return (
            (self.x2 - self.x1) *
            (self.y2 - self.y1) *
            (self.z2 - self.z1)
        )
    
    def intersects(self, other):
        return (
            self.x1 < other.x2 and
            self.x2 > other.x1 and
            self.y1 < other.y2 and
            self.y2 > other.y1 and
            self.z1 < other.z2 and
            self.z2 > other.z1
        )

    def contains(self, other):
        return (
            self.x1 <= other.x1 and
            self.x2 >= other.x2 and
            self.y1 <= other.y1 and
            self.y2 >= other.y2 and
            self.z1 <= other.z1 and
            self.z2 >= other.z2
        )
    
    def subtract(self, other):
        if not self.intersects(other):
            return [self]
        elif other.contains(self):
            return []

        xs = sorted((self.x1, self.x2, other.x1, other.x2))
        ys = sorted((self.y1, self.y2, other.y1, other.y2))
        zs = sorted((self.z1, self.z2, other.z1, other.z2))

        ret = []
        for x1, x2 in zip(xs, xs[1:]):
            for y1, y2 in zip(ys, ys[1:]):
                for z1, z2 in zip(zs, zs[1:]):
                    cube = Cube(x1,x2,y1,y2,z1,z2)
                    if self.contains(cube) and not cube.intersects(other):
                        ret.append(cube)
        return ret
    
    def overlapping_cube(self, other):
        ((x1,x2),(y1,y2),(z1,z2)) = ((max(self.x1,other.x1),min(self.x2,other.x2)),(max(self.y1,other.y1),min(self.y2,other.y2)),(max(self.z1,other.z1),min(self.z2,other.z2)))
        return Cube(x1,x2,y1,y2,z1,z2)
        
def calc_a(operations):
    cubes = []
    bound = Cube(-50,51,-50,51,-50,51)
    for on, step_cube in operations:
        if not bound.intersects(step_cube):
            continue
        step_cube = bound.overlapping_cube(step_cube)
        cubes = [
            part
            for cube in cubes
            for part in cube.subtract(step_cube)
        ]
        if on:
            cubes.append(step_cube)
    return sum(cube.size() for cube in cubes)

def calc_b(operations):
    cubes = []
    for on, step_cube in operations:
        cubes = [
            part
            for cube in cubes
            for part in cube.subtract(step_cube)
        ]
        if on:
            cubes.append(step_cube)
    return sum(cube.size() for cube in cubes)