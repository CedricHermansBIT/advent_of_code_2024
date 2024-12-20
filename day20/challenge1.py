maze=[]
start=(0,0)
end=(0,0)
#with open("testinput.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for y,line in enumerate(ifile):
        maze.append(list(line.strip()))
        if "S" in line:
            start=(line.index("S"),y)
        if "E" in line:
            end=(line.index("E"),y)

print(maze)
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
            continue
        if newpos in scores:
            continue
        scores[newpos]=scores[current]+1
        current=newpos


saved_steps={}
current=start
while current!=end:
    for dir in dirs:
        newpos=(current[0]+dir[0]*2,current[1]+dir[1]*2)
        if newpos[0]<0 or newpos[0]>=len(maze[0]) or newpos[1]<0 or newpos[1]>=len(maze):
            continue
        if maze[newpos[1]][newpos[0]]=="#":
            continue
        if newpos in scores and (scores[newpos])<=scores[current]+2:
            continue
        saved_step_amount=scores[newpos]-scores[current]-2
        if saved_step_amount not in saved_steps:
            saved_steps[saved_step_amount]=1
        else:
            saved_steps[saved_step_amount]+=1
        #print(f"Saved {scores[newpos]-scores[current]-2} steps by going to {newpos} from {current}")
    for dir in dirs:
        newpos=(current[0]+dir[0],current[1]+dir[1])
        if maze[newpos[1]][newpos[0]]=="#":
            continue
        if newpos in scores and scores[newpos]==scores[current]+1:
            current=newpos
            break
print(saved_steps)
keys=list(saved_steps.keys())
keys.sort()
total=0
for key in keys:
    if key<100:
        continue
    total+=saved_steps[key]

print(total)