list1 = []
list2 = []

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        l1,l2 = line.split()
        list1.append(int(l1))
        list2.append(int(l2.strip()))
list1.sort()
list2.sort()

result = 0

for v1,v2 in zip(list1,list2):
    result += abs(v1-v2)
        
print(result)