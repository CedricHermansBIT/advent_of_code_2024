maze=[]
            #down,right,    up,  left
directions=[(0,1),(1,0),(0,-1),(-1,0)]
icons=["v","^",">","<"]

# start facing east
start=(0,0,2)
end=(0,0)
#with open("challengeinput.txt","r") as ifile:
with open("testinput.txt","r") as ifile:
    for i,line in enumerate(ifile):
        maze.append(list(line.strip()))
        if "S" in maze[i]:
            start=(maze[i].index("S"),i,2)
        if "E" in maze[i]:
            end=(maze[i].index("E"),i)
print(start,end)
to_visit=[start]
visited=set()
while True:
    x,y,d=to_visit.pop()
    # print maze
    for i,line in enumerate(maze):
        if i==y:
            print("".join(line[:x]+[icons[d]]+line[x+1:]))
        else:
            print("".join(line))
    if (x,y)==end:
        break
    for i in range(-1,2):
        dx,dy=directions[(d+i)%4]
        if maze[y+dy][x+dx]!="#" and (x+dx,y+dy,(d+i)%4) not in visited:
            to_visit.append((x+dx,y+dy,(d+i)%4))
    visited.add((x,y,d))
    print(to_visit)
    #input()

print("done")
