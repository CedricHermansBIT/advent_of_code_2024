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
    nines=set()
    # having the previous path as a string is cheasy but it works
    # basically, by using this, we can keep track of the unique paths
    queue.add((0,zero,""))
    while queue:
        #print(queue)
        (n,(x,y),p) = queue.pop()
        #print(n,x,y)
        p+=str(x)+str(y)
        if n == 9:
            nines.add((x,y,p))
        if ((x-1)>=0) and (int(lines[y][x-1]) == n+1):
            #print("left")
            queue.add((n+1,(x-1,y),p))
        if ((x+1)<w) and (int(lines[y][x+1]) == n+1):
            #print("right")
            queue.add((n+1,(x+1,y),p))
        if (y-1)>=0 and int(lines[y-1][x]) == n+1:
            #print("up")
            queue.add((n+1,(x,y-1),p))
        if (y+1)<h and int(lines[y+1][x]) == n+1:
            #print("down")
            queue.add((n+1,(x,y+1),p))
    total+=len(nines)
print(total)

        
