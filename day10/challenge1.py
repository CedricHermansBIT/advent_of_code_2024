with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines = [line.strip() for line in ifile.readlines()]

w,h= len(lines[0]), len(lines)
zeros = []
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == "0":
            zeros.append((x,y))

total=0
for zero in zeros:
    queue = set()
    visited = set()
    nines=set()
    queue.add((0,zero))
    while queue:
        #print(queue)
        (n,(x,y)) = queue.pop()
        #print(n,x,y)
        visited.add((x,y))
        if n == 9:
            nines.add((x,y))
        if ((x-1)>=0) and ((x-1,y) not in visited) and (int(lines[y][x-1]) == n+1):
            #print("left")
            queue.add((n+1,(x-1,y)))
        if ((x+1)<w) and ((x+1,y) not in visited) and (int(lines[y][x+1]) == n+1):
            #print("right")
            queue.add((n+1,(x+1,y)))
        if (y-1)>=0 and (x,y-1) not in visited and int(lines[y-1][x]) == n+1:
            #print("up")
            queue.add((n+1,(x,y-1)))
        if (y+1)<h and (x,y+1) not in visited and int(lines[y+1][x]) == n+1:
            #print("down")
            queue.add((n+1,(x,y+1)))
    total+=len(nines)
print(total)

        
