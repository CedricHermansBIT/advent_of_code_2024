machines=[[]]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        if line.strip() == "":
            machines.append([])
            continue
        spline=line.strip().split(",")
        if 'Button' in line:
            x=int(spline[0].split("+")[1])
            y=int(spline[1].split("+")[1])
            machines[-1].append((x,y))
        else:
            x=int(spline[0].split("=")[1])
            y=int(spline[1].split("=")[1])
            machines[-1].append((x,y))
total=0
for machine in machines:
    print(machine)
    cheapest=0
    for i in range(101):
        if (machine[2][0]-machine[0][0]*i)%machine[1][0]==0 and (machine[2][1]-machine[0][1]*i)%machine[1][1]==0\
            and (machine[2][0]-machine[0][0]*i)//machine[1][0] == (machine[2][1]-machine[0][1]*i)//machine[1][1]:
            j=(machine[2][1]-machine[0][1]*i)//machine[1][1]
            if (cheapest==0 or i*3+j<cheapest) and j<101 and j>=0:
                print(i,j)
                cheapest=i*3+j
    total+=cheapest
print(total)