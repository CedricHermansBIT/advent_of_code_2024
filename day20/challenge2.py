maze=[]
start=(0,0)
end=(0,0)

cutoff=100
#with open("testinput.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for y,line in enumerate(ifile):
        maze.append(list(line.strip()))
        if "S" in line:
            start=(line.index("S"),y)
        if "E" in line:
            end=(line.index("E"),y)

#print(maze)
print(start)
print(end)
        
dirs=[(0,1),(0,-1),(1,0),(-1,0)]
scores={start:0}

current=start
#determine normal path scores
while current!=end:
    for dir in dirs:
        newpos=(current[0]+dir[0],current[1]+dir[1])
        if maze[newpos[1]][newpos[0]]=="#":
            # wall
            continue
        if newpos in scores:
            # backwards path
            continue
        scores[newpos]=scores[current]+1
        current=newpos

def manhattan_distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def is_inside_square(center,radius,point):
    #print(f"Checking if {point} is inside square with center {center} and radius {radius}, manhattan distance: {manhattan_distance(center,point)}")
    return manhattan_distance(center,point)<=radius

radius=20
saved_steps={}
current=start
while current!=end:
    coords=[]
    # check the square/diamond area within border
    for y in range(max(0,current[1]-radius),min(len(maze),current[1]+radius+1)):
        for x in range(max(0,current[0]-radius),min(len(maze[0]),current[0]+radius+1)):
            mh=manhattan_distance(current,(x,y))
            newpos=(x,y)
            #print(newpos)
            if is_inside_square(current,radius,newpos):
                # check if we are on a path
                if newpos not in scores:
                    continue
                # check if we save time
                if (scores[newpos])<(scores[current]+mh):
                    continue
                #print("Saving time!")
                coords.append(newpos)
                saved_picoseconds=scores[newpos]-scores[current]-mh
                if saved_picoseconds not in saved_steps:
                    saved_steps[saved_picoseconds]=1
                else:
                    saved_steps[saved_picoseconds]+=1
    # # print the maze
    # for y in range(len(maze)):
    #     for x in range(len(maze[0])):
    #         if (x,y) in coords:
    #             print("*",end="")
    #         else:
    #             print(maze[y][x],end="")
    #     print()
    # print(coords)
    # exit(0)
                
    # continue on the normal path
    for dir in dirs:
        newpos=(current[0]+dir[0],current[1]+dir[1])
        if maze[newpos[1]][newpos[0]]=="#":
            continue
        if newpos in scores and scores[newpos]==scores[current]+1:
            current=newpos
            break
#print(saved_steps)
picoseconds=list(saved_steps.keys())
picoseconds.sort()
total=0
for picosecond in picoseconds:
    if picosecond>=cutoff:
        total+=saved_steps[picosecond]
        #print(f"{picosecond}: {saved_steps[picosecond]}")

print(total)