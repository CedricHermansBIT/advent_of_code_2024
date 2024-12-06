with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()

lines=[list(x.strip()) for x in lines]
boundaries = (len(lines[0]),len(lines))
for line in lines:
    if "^" in line:
        x,y=[line.index("^"),lines.index(line)]

visited=set()
visited.add((x,y))
#up
dir=(0,-1)

while (0<=(x:=x+dir[0])<boundaries[0]) and (0<=(y:=y+dir[1])<boundaries[1]):
    print(x,y)
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
        visited.add((x,y))
print(len(visited))