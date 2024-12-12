from collections import defaultdict
fields=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        fields.append(list(line.strip()))
# Now we have a list of lists, e.g. 
# [[A,A,A],
#  [A,B,B],
#  [B,C,C]]
# However, we will first rename the fields to numbers of connected regions
# Because B is split in two regions, and we want them separate, not as the "same" field

def neighbours(x,y,max_x,max_y):
    n=set()
    if x>0:
        n.add((x-1,y))
    if x<max_x:
        n.add((x+1,y))
    if y>0:
        n.add((x,y-1))
    if y<max_y:
        n.add((x,y+1))
    return n

current_id=-1
max_x=len(fields[0])-1
max_y=len(fields)-1
for y in range(0,len(fields)):
    for x in range(0,len(fields[0])):
        if type(fields[y][x]) == str:
            current_id+=1
            to_visit=set()
            current_char=fields[y][x]
            to_visit.update(neighbours(x,y,max_x,max_y))
            fields[y][x]=current_id
            while to_visit:
                current_x,current_y=to_visit.pop()
                if fields[current_y][current_x] == current_char:
                    fields[current_y][current_x]=current_id
                    to_visit.update(neighbours(current_x,current_y,max_x,max_y))
#defaultdict with default list of 2 elements (0,0)
sizes=defaultdict(lambda: [0,0])

#horizontal borders
for y in range(0,len(fields)):
    for x in range(1,len(fields[y])):
        # leftmost border
        previous_field=fields[y][x-1]
        current_field=fields[y][x]
        if x-1 == 0:
            sizes[previous_field][0]+=1
            sizes[previous_field][1]+=1
        if previous_field != current_field:
            sizes[previous_field][0]+=1
            sizes[current_field][0]+=1
        if x == len(fields[y])-1:
            sizes[current_field][0]+=1
        sizes[current_field][1]+=1

#vertical borders
for x in range(0,len(fields[y])):
    for y in range(1,len(fields)):
        # upmost border
        previous_field=fields[y-1][x]
        current_field=fields[y][x]
        if y-1 == 0:
            sizes[previous_field][0]+=1
        if previous_field != current_field:
            sizes[previous_field][0]+=1
            sizes[current_field][0]+=1
        if y == len(fields)-1:
            sizes[current_field][0]+=1

# reduce values by multiplying them and then summing them
total=0
for borders,amount in sizes.items():
    total+=amount[0]*amount[1]
print(total)
