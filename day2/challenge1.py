state=-1
data=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        data.append(list(map(int,line.strip().split())))

result=0

for spline in data:
    for i in range(1,len(spline)):
        if i==1:
            state = spline[i-1] > spline[i]
        
        if (state != (spline[i-1] > spline[i])) or (abs(spline[i-1] - spline[i]) > 3) or (spline[i-1] == spline[i]):
            #print(i)
            break
    else:
        print(spline)
        result += 1
print(result)
