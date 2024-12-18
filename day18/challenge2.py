start=(0,0)

# for testinput
#size=(7,7)
#do_bytes=12
#end=(6,6)

# for challengeinput
size=(71,71)
num_bytes=1024 # starting value
end=(70,70)

coords=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for i,line in enumerate(ifile):
        x,y=line.strip().split(",")
        coords.append((int(x),int(y)))

#print("\n".join(["".join(row) for row in maze]))

def create_maze(coords,size,do_bytes):
    maze=[["." for i in range(size[0])] for j in range(size[1])]
    for i in range(do_bytes):
        maze[coords[i][1]][coords[i][0]]="#"
    return maze


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
    return []


maze=create_maze(coords,size,num_bytes)

while a_star(start,end,maze) != []:
    num_bytes+=1
    print(num_bytes)
    maze=create_maze(coords,size,num_bytes)
print(coords[num_bytes-1],num_bytes-1)