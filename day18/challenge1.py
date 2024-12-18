start=(0,0)

# for testinput
#size=(7,7)
#do_bytes=12
#end=(6,6)

# for challengeinput
size=(71,71)
do_bytes=1024
end=(70,70)

maze=[["." for i in range(size[0])] for j in range(size[1])]

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for i,line in enumerate(ifile):
        if i==do_bytes:
            break
        x,y=line.strip().split(",")
        maze[int(y)][int(x)]="#"

print("\n".join(["".join(row) for row in maze]))


def a_star(start,end,maze):
    def dist(a,b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])
    
    def trace_to_start(history,start,end):
        path=[end]
        while path[-1]!=start:
            path.append(history[path[-1]])
        return path



    search_nodes=[start]
    history={}
    g={start:0}
    f={start:dist(start,end)}

    while search_nodes:
        current=min(search_nodes,key=lambda x:f[x])
        if current==end:
            return trace_to_start(history,start,end)
        search_nodes.remove(current)
        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            new=(current[0]+i,current[1]+j)
            if new[0]>=0 and new[0]<size[0] and new[1]>=0 and new[1]<size[1] and maze[new[1]][new[0]]==".":
                new_g=g[current]+1
                if new not in g or new_g<g[new]:
                    history[new]=current
                    g[new]=new_g
                    f[new]=new_g+dist(new,end)
                    if new not in search_nodes:
                        search_nodes.append(new)

path=a_star(start,end,maze)
print(path)

for i in range(size[1]):
    for j in range(size[0]):
        if (j,i) in path:
            print("X",end="")
        else:
            print(maze[i][j],end="")
    print()

print("Length of path:",len(path)-1)