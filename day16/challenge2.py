maze=[]
            #down,right,    up,  left
directions=[(0,1),(1,0),(0,-1),(-1,0)]
icons=["v",">","^","<"]

# start facing east
start=(0,0,1)
end=(0,0,1)
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for i,line in enumerate(ifile):
        maze.append(list(line.strip()))
        if "S" in maze[i]:
            start=(maze[i].index("S"),i,1)
        if "E" in maze[i]:
            end=(maze[i].index("E"),i,1)
print(start,end)
to_visit=[start]
visited=set()
scores={start:(0,set())}
end_score=0
while True:
    # grab all scores from to_visit
    s=sorted([(scores[(point[0],point[1],point[2])],point) for point in to_visit],key=lambda x:x[0][0])
    #print(s[0][0][0])
    #input()
    # grab smallest score
    x,y,d=s[0][1]
    # remove from to_visit
    to_visit.remove((x,y,d))
    if (x,y,d)==end and end_score==0:
        end_score=scores[(x,y,d)][0]
        print("end:",end_score)
        # print path based on scores[1]
        # for i,line in enumerate(maze):
        #     for j,c in enumerate(line):
        #         if (j,i) in scores[(x,y,d)][1]:
        #             print("O",end="")
        #         else:
        #             print(c,end="")
        #     print()
        #break
    if end_score!=0 and s[0][0][0]>end_score:
        #print(scores)
        coords=end
        all_coords=set()
        # trace back
        queue=[end]
        while queue:
            # we have the path stored in scores[coords][1] (and can be multiple paths)
            coords=queue.pop(0)
            all_coords.add(coords[0:2])
            queue.extend(scores[coords][1])
        print(all_coords)
        print(len(all_coords))
        # remove d from all_coords
        all_coords = [(x,y) for x,y in all_coords]
        for i,line in enumerate(maze):
            for j,c in enumerate(line):
                if (j,i) in all_coords:
                    print("O",end="")
                else:
                    print(c,end="")
            print()

        break
    #print maze
    # for i,line in enumerate(maze):
    #     if i==y:
    #         print("".join(line[:x]+[icons[d]]+line[x+1:]))
    #     else:
    #         print("".join(line))
    for i in range(-1,2):
        # new direction
        dn=(d+i)%4
        dx,dy=directions[dn]
        new_score=scores[(x,y,d)][0]+1+abs(i)*1000
        if maze[y+dy][x+dx]!="#":
            if  (x+dx,y+dy,dn) not in scores:
                to_visit.append((x+dx,y+dy,dn))
                #print(scores[(x,y,d)])
                #print(scores[(x,y,d)][1]+[(x,y)])
                s=set()
                s.add((x,y,d))
                scores[(x+dx,y+dy,dn)]=(new_score,s)
            elif (new_score)==scores[(x+dx,y+dy,dn)][0]:
                s=scores[(x+dx,y+dy,dn)][1]
                s.add((x,y,d))
                #print(scores[(x,y)])
                scores[(x+dx,y+dy,dn)]=(new_score,s)
            # elif new_score<scores[(x+dx,y+dy,dn)][0]:
            #     print(scores[(x+dx,y+dy,dn)],(x,y,d),new_score)
            #     print("did this")
            #     s=set()
            #     s.add((x,y,d))
            #     scores[(x+dx,y+dy,dn)]=(new_score,s)
                

                #else:
                #    print(abs((scores[(x,y)][0]+1+abs(i)*1000)-scores[(x+dx,y+dy)][0]))
    #print(to_visit)
    #input()

print("done")
