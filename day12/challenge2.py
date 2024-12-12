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
# first element is borders and second is amount
sizes=defaultdict(lambda: [0,0])

#vertical borders
for y in range(0,len(fields)):
    for x in range(0,len(fields[y])):
        field=fields[y][x]
        sizes[field][1]+=1
        if y==0:
            if x==0:
                # top is for sure border
                sizes[field][0]+=1
                if field==3:
                    print("top",x,y,field)
                if field != fields[y+1][x]:
                    # bottom is also for sure border
                    sizes[field][0]+=1
                    if field==3:
                        print("bottom",x,y,field)
            else:
                # top is for sure border if field is different from field to the left
                if field != fields[y][x-1]:
                    sizes[field][0]+=1
                    if field==3:
                        print("top",x,y,field)
                # check the bottom
                if field != fields[y+1][x] and ((fields[y+1][x-1] == fields[y][x-1]) or (field != fields[y][x-1])):
                    sizes[field][0]+=1
                    if field==3:
                        print("bottom",x,y,field)
        elif x==0:
            # top is for sure border if field is different from field above
            if field != fields[y-1][x]:
                sizes[field][0]+=1
                if field==3:
                    print("top",x,y,field)
            # check the bottom
            if y!=len(fields)-1 and field != fields[y+1][x]:
                sizes[field][0]+=1
                if field==3:
                    print("bottom",x,y,field)
        else:
            # left is for sure border if field is different from field above
            # and if field to the left was the same as field above the left
            # 12
            # 11  <- example of bottom right 1, it has border at top
            if (field != fields[y-1][x] and fields[y-1][x-1] == fields[y][x-1] and field == fields[y][x-1]) \
                or \
                (field != fields[y][x-1] and field != fields[y-1][x]):
                sizes[field][0]+=1
                if field==3:
                    print("top",x,y,field)
            #bottom
            if y!=len(fields)-1 and \
                ((field != fields[y+1][x] and fields[y+1][x-1] == fields[y][x-1] and field == fields[y][x-1])\
                or \
                (field != fields[y+1][x] and field != fields[y][x-1])):
                sizes[field][0]+=1
                if field==3:
                    print("bottom",x,y,field)
        if y==len(fields)-1:
            if x==0:
                # bottom is for sure border
                sizes[field][0]+=1
                if field==3:
                    print("bottom",x,y,field)
            # bottom is for sure border if field is different from field to the left
            elif field != fields[y][x-1]:
                sizes[field][0]+=1
                if field==3:
                    print("bottom",x,y,field)


#horizontal borders
for x in range(0,len(fields[y])):
    for y in range(0,len(fields)):
        field=fields[y][x]
        if x==0:
            if y==0:
                # left is for sure border
                sizes[field][0]+=1
                if field==3:
                    print("left",x,y,field)
                if field != fields[y][x+1]:
                    # right is also for sure border
                    sizes[field][0]+=1
                    if field==3:
                        print("right",x,y,field)
            else:
                # left is for sure border if field is different from field above
                if field != fields[y-1][x]:
                    sizes[field][0]+=1
                    if field==3:
                        print("left",x,y,field)
                # check the right
                if field != fields[y][x+1] and ((fields[y-1][x+1] == fields[y-1][x]) or (field != fields[y-1][x])):
                    sizes[field][0]+=1
                    if field==3:
                        print("right",x,y,field)
        elif y==0:
            # left is for sure border if field is different from field to the left
            if field != fields[y][x-1]:
                sizes[field][0]+=1
                if field==3:
                    print("left",x,y,field)
            # check the right
            if x!=len(fields[y])-1 and field != fields[y][x+1]:
                sizes[field][0]+=1
                if field==3:
                    print("right",x,y,field)
        else:
            # top is for sure border if field is different from field to the left
            # and if field above was the same as field to the left above
            # 11
            # 12  <- example of bottom right 1, it has border at left
            if (field != fields[y][x-1] and fields[y-1][x-1] == fields[y-1][x] and field == fields[y-1][x]) \
                or \
                (field != fields[y-1][x] and field != fields[y][x-1]):
                sizes[field][0]+=1
                if field==3:
                    print("left",x,y,field)
            #right
            if x!=len(fields[y])-1 and \
                ((field != fields[y][x+1] and fields[y-1][x+1] == fields[y-1][x] and field == fields[y-1][x])\
                or \
                (field != fields[y][x+1] and field != fields[y-1][x])):
                sizes[field][0]+=1
                if field==3:
                    print("right",x,y,field)
        if x==len(fields[y])-1:
            if y==0:
                # right is for sure border
                sizes[field][0]+=1
                if field==3:
                    print("right",x,y,field)
            # right is for sure border if field is different from field above
            elif field != fields[y-1][x]:
                sizes[field][0]+=1
                if field==3:
                    print("right",x,y,field)
print(sizes)
# reduce values by multiplying them and then summing them
total=0
for borders,amount in sizes.items():
    total+=amount[0]*amount[1]
print(total)
