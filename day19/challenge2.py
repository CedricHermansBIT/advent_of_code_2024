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
    queue={"":1}
    while len(queue)>0:
        keys=list(queue.keys())
        # grab smallest key
        keys.sort(key=lambda x: len(x))
        current=keys[0]
        amount=queue.pop(current)
        if current==towel:
            total+=amount
            continue
        #print(current)
        new_queue = try_pattern(current,patterns,towel)
        for new in new_queue:
            if new in queue:
                queue[new]+=amount
            else:
                queue[new]=amount

print(total)
