maze=[]
            #down,right,    up,  left
directions=[(0,1),(1,0),(0,-1),(-1,0)]
icons=["v",">","^","<"]

# start facing east
start=(0,0,1)
end=(0,0)
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for i,line in enumerate(ifile):
        maze.append(list(line.strip()))
        if "S" in maze[i]:
            start=(maze[i].index("S"),i,1)
        if "E" in maze[i]:
            end=(maze[i].index("E"),i)
print(start,end)
to_visit=[start]
visited=set()
scores={start:0}
while True:
    # grab all scores from to_visit
    s=sorted([(scores[point],point) for point in to_visit],key=lambda x:x[0])
    #print(s)
    #input()
    # grab smallest score
    x,y,d=s[0][1]
    # remove from to_visit
    to_visit.remove((x,y,d))
    # print maze
    # for i,line in enumerate(maze):
    #     if i==y:
    #         print("".join(line[:x]+[icons[d]]+line[x+1:]))
    #     else:
    #         print("".join(line))
    if (x,y)==end:
        print(scores[(x,y,d)])
        break
    for i in range(-1,2):
        dx,dy=directions[(d+i)%4]
        if maze[y+dy][x+dx]!="#" and (x+dx,y+dy,(d+i)%4) not in visited:
            if (x+dx,y+dy,(d+i)%4) not in to_visit or scores[(x,y,d)]+1+abs(i)*1000<scores[(x+dx,y+dy,(d+i)%4)]:
                to_visit.append((x+dx,y+dy,(d+i)%4))
                scores[(x+dx,y+dy,(d+i)%4)]=scores[(x,y,d)]+1+abs(i)*1000
    visited.add((x,y,d))
    #print(to_visit)
    #input()

print("done")
