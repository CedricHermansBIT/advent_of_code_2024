# Similar to challenge1, check below for additional comments:

from collections import defaultdict

antennas=defaultdict(list)
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for y,line in enumerate(ifile):
        for x,char in enumerate(line.strip()):
            if char!=".":
                antennas[char].append((x,y))
x_bound=len(line.strip())-1
y_bound=y

# extract the function to get the new position of an antenna based on current position and dx,dy
def get_new_postion(a,dx,dy):
    return (a[0]+dx,a[1]+dy)


interference_points=set()
# id, positions
for k,v in antennas.items():
    # for each pair of positions (O(n*logn) complexity)
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            a1=v[i]
            a2=v[j]

            # Antennas themselves are interference points
            interference_points.add(a1)
            interference_points.add(a2)

            # Note: we could probably simplify by not using absolute values for dx,dy and do it with 2 checks
            # But I would need to draw this out or something to be sure

            dx,dy=abs(a2[0]-a1[0]),abs(a2[1]-a1[1])

            # Instead of calculating the new positions based on the case, we can calculate the relative directions

            #print(f"dx={dx},dy={dy},a1={a1},a2={a2},k={k}")
            if a1[0]<=a2[0] and a1[1]<=a2[1]:
                #print("case 1")
                # 1.
                # .2
                d1x,d1y=-dx,-dy
                d2x,d2y=dx,dy
            elif a1[0]<=a2[0] and a1[1]>=a2[1]:
                #print("case 2")
                # .2
                # 1.
                d1x,d1y=-dx,dy
                d2x,d2y=dx,-dy
            elif a1[0]>=a2[0] and a1[1]<=a2[1]:
                #print("case 3")
                # .1
                # 2.
                d1x,d1y=dx,-dy
                d2x,d2y=-dx,dy
            else:
                #print("case 4")
                # 2.
                # .1
                d1x,d1y=dx,dy
                d2x,d2y=-dx,-dy

            # Calculate the new positions of the antennas based on the relative directions
            pos1_x,pos1_y=get_new_postion(a1,d1x,d1y)
            while pos1_x>=0 and pos1_y>=0 and pos1_x<=x_bound and pos1_y<=y_bound:
                interference_points.add((pos1_x,pos1_y))
                # add the same offset to the new position, so we are going over the interference points
                # If we are out of bounds, we stop based on the while condition
                pos1_x,pos1_y=get_new_postion((pos1_x,pos1_y),d1x,d1y)

            pos2_x,pos2_y=get_new_postion(a2,d2x,d2y)
            while pos2_x>=0 and pos2_y>=0 and pos2_x<=x_bound and pos2_y<=y_bound:
                interference_points.add((pos2_x,pos2_y))
                pos2_x,pos2_y=get_new_postion((pos2_x,pos2_y),d2x,d2y)

for y in range(y_bound+1):
    for x in range(x_bound+1):
        if (x,y) in interference_points:
            print("#",end="")
        else:
            print(".",end="")
    print()

print(len(interference_points))