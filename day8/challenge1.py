from collections import defaultdict
# Note: a defaultdict is a dictionary that initializes the value to a default value
# This way you don't have to check if a key exists in the dictionary before adding a value to it
antennas=defaultdict(list)

# Create a dictionary of all antennas (per id) and their positions
# e.g. {'A': [(0, 0), (1, 1)], 'B': [(2, 2), (3, 3)]}

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for y,line in enumerate(ifile):
        for x,char in enumerate(line.strip()):
            if char!=".":
                antennas[char].append((x,y))

# Get the bounds of the grid based on the last line read
# Note: this is cheasy because in other languages, the line would be out of scope
# Thanks Python!
x_bound=len(line.strip())-1
y_bound=y

#print(antennas)

interference_points=set()
# id, positions
for k,v in antennas.items():
    # for each pair of positions (O(n*logn) complexity)
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            # get the two antenna positions we are comparing
            a1=v[i]
            a2=v[j]
            # Get the distance between the two antennas
            dx,dy=abs(a2[0]-a1[0]),abs(a2[1]-a1[1])
            #print(f"dx={dx},dy={dy},a1={a1},a2={a2},k={k}")
            # Calculate the new positions of the antennas based on the case (see each case below)
            if a1[0]<=a2[0] and a1[1]<=a2[1]:
                #print("case 1")
                # 1.
                # .2
                pos1_x,pos1_y=a1[0]-dx,a1[1]-dy
                pos2_x,pos2_y=a2[0]+dx,a2[1]+dy
            elif a1[0]<=a2[0] and a1[1]>=a2[1]:
                #print("case 2")
                # .2
                # 1.
                pos1_x,pos1_y=a1[0]-dx,a1[1]+dy
                pos2_x,pos2_y=a2[0]+dx,a2[1]-dy
            elif a1[0]>=a2[0] and a1[1]<=a2[1]:
                #print("case 3")
                # .1
                # 2.
                pos1_x,pos1_y=a1[0]+dx,a1[1]-dy
                pos2_x,pos2_y=a2[0]-dx,a2[1]+dy
            else:
                #print("case 4")
                # 2.
                # .1
                pos1_x,pos1_y=a1[0]+dx,a1[1]+dy
                pos2_x,pos2_y=a2[0]-dx,a2[1]-dy


            # Check if the new positions are within the bounds of the grid,
            # if so, add them to the set of interference points

            # Sets don't allow duplicates, so we don't have to worry about adding the same point twice

            #print(f"pos1=({pos1_x},{pos1_y}),pos2=({pos2_x},{pos2_y})")
            if pos1_x>=0 and pos1_y>=0 and pos1_x<=x_bound and pos1_y<=y_bound:
                interference_points.add((pos1_x,pos1_y))
            if pos2_x>=0 and pos2_y>=0 and pos2_x<=x_bound and pos2_y<=y_bound:
                interference_points.add((pos2_x,pos2_y))

# For debugging, print the grid with the interference points
for y in range(y_bound+1):
    for x in range(x_bound+1):
        if (x,y) in interference_points:
            print("#",end="")
        else:
            print(".",end="")
    print()

# Print the number of interference points
print(len(interference_points))