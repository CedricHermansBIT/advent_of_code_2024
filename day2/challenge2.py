state=-1
data=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        data.append(list(map(int,line.strip().split())))

result=0

def check_safety(spline,d=0):
    for i in range(1,len(spline)):
        if i==1:
            state = spline[i-1] > spline[i]
        
        if (state != (spline[i-1] > spline[i])) or (abs(spline[i-1] - spline[i]) > 3) or (spline[i-1] == spline[i]):
            if (check_safety(spline[:i]+spline[i+1:],1) 
                or check_safety(spline[:i-1]+spline[i:],1)
                or check_safety(spline[1:],1) 
                or check_safety(spline[:-1],1)) and d==0:
                print(spline)
                return 1
            else:
                return 0
    else:
        return 1

for spline in data:
    result+=check_safety(spline)
print(result)
