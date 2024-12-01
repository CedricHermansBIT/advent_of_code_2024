list1 = []
list2 = []

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        l1,l2 = line.split()
        list1.append(int(l1))
        list2.append(int(l2.strip()))

result = 0

for v1 in list1:
    n=list2.count(v1)
    result += abs(v1*n)
        
print(result)