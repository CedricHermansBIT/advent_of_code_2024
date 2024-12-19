patterns=[]

towels=[]

first_line=True
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        if first_line:
            first_line=False
            patterns=line.strip().split(", ")
        elif line.strip()!="":
            towels.append(line.strip())

print(patterns)
print(towels)

def try_pattern(current,patterns,towel):
    queue=[]
    for pattern in patterns:
        if towel.startswith(current+pattern):
            queue.append(current+pattern)
    return queue

total=0
for towel in towels:
    queue=[""]
    while towel not in queue and len(queue)>0:
        current=queue.pop()
        #print(current)
        queue+=try_pattern(current,patterns,towel)
    if towel in queue:
        total+=1

print(total)
