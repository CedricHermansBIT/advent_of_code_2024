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
            x=int(spline[0].split("=")[1]) + 10000000000000
            y=int(spline[1].split("=")[1]) + 10000000000000
            machines[-1].append((x,y))

#xg=n*x1+m*x2 -> n=(xg-m*x2)/x1
#yg=n*y1+m*y2
#yg=((xg-m*x2)/x1)*y1+m*y2
# m = (xg*y1 -x1*yg )/ (x2*y1-x1*y2)
# Then we can find n and check if they are integers and positive

total=0
for machine in machines:
    x1,y1=machine[0]
    x2,y2=machine[1]
    xg,yg=machine[2]
    m=(xg*y1-x1*yg)/(x2*y1-x1*y2)
    n=(xg-m*x2)/x1
    if m%1==0 and n%1==0 and m>0 and n>0:
        total+=n*3+m
        print(machine,m,n)
print(total)