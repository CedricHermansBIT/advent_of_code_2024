with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines = ifile.readlines()

total=0
for line in lines:
    queue = []
    result=int(line.split(":")[0])
    equations=list(map(int,line.strip().split(":")[1].split(" ")[1:]))
    #print(result,equations)
    queue.append((result, equations[0]+equations[1],equations[2:]))
    queue.append((result, equations[0]*equations[1],equations[2:]))
    queue.append((result, int(str(equations[0])+str(equations[1])),equations[2:]))

    while len(queue)>0:
        result, current, equations = queue.pop()
        #print(result,current, equations)
        if len(equations)==0:
            if current == result:
                total+=result
                #print("Found")
                break
        else:
            if current<=result:
                queue.append((result, current+equations[0],equations[1:]))
                queue.append((result, current*equations[0],equations[1:]))
                queue.append((result, int(str(current)+str(equations[0])),equations[1:]))

print(total)