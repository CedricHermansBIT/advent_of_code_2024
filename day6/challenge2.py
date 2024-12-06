with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()

lines=[list(x.strip()) for x in lines]
boundaries = (len(lines[0]),len(lines))
for line in lines:
    if "^" in line:
        x,y=[line.index("^"),lines.index(line)]

#up
dir=(0,-1)


def check_route(x,y,dir,lines,boundaries=boundaries):
    visited=set()
    visited.add((x,y,dir[0],dir[1]))
    while (0<=(x:=x+dir[0])<boundaries[0]) and (0<=(y:=y+dir[1])<boundaries[1]):
        if (x,y,dir[0],dir[1]) in visited:
            # we in a loop, visited this before!
            return True
        #print(x,y)
        if lines[y][x] == "#":
            x-=dir[0]
            y-=dir[1]
            match dir:
                case (0,-1):
                    dir=(1,0)
                case (1,0):
                    dir=(0,1)
                case (0,1):
                    dir=(-1,0)
                case (-1,0):
                    dir=(0,-1)
        else:
            visited.add((x,y,dir[0],dir[1]))
    return False # guard left the area


possible_loops=0
for ys in range(boundaries[1]):
    for xs in range(boundaries[0]):
        if lines[ys][xs] == "#":
            continue
        else:
            if (xs,ys) != (x,y):
                lines2=[line.copy() for line in lines]
                lines2[ys][xs] = "#"
                possible_loops+= check_route(x,y,dir,lines2)

print(possible_loops)