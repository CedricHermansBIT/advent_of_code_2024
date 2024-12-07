with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines = ifile.readlines()

total=0
for line in lines:
    queue = []
    # Get result
    result=int(line.split(":")[0])
    # Get equations (numbers)
    equations=list(map(int,line.strip().split(":")[1].split(" ")[1:]))
    # we construct a queue, where we add the first two numbers, and keep the rest of the numbers
    queue.append((result, equations[0]+equations[1],equations[2:]))
    # instead of adding the first two numbers, we multiply them
    queue.append((result, equations[0]*equations[1],equations[2:]))

    #now we have 2 options in the queue (+ and *)

    #while we have options in the queue
    while len(queue)>0:
        # get the last option (depth first search, first one would be breadth first search, but is slower in this context)
        result, current, equations = queue.pop()
        # if there are no more equations (numbers) to add or multiply, we reached the end
        if len(equations)==0:
            # if the current number is the result, we found the solution
            if current == result:
                total+=result
                # we don't need to keep looking, we found the solution, break from current equation
                break
        else:
            # Heuristic: if the current number is bigger than the result, we don't need to keep looking, because it can't get smaller anymore
            if current<=result:
                # if there are more numbers to add or multiply, we add them to the queue
                queue.append((result, current+equations[0],equations[1:]))
                queue.append((result, current*equations[0],equations[1:]))

print(total)