with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    line=ifile.readline().strip()

entire_sequence=[]
index=0
file=True
for i,c in enumerate(line):
    if file:
        entire_sequence+=[index]*int(c)
        index+=1
        file=False
    else:
        entire_sequence+=["."]*int(c)
        file=True

x=""
for i,c in enumerate(entire_sequence):
    if c==".":
        while entire_sequence[-1]==".":
            entire_sequence.pop()
        entire_sequence[i]=entire_sequence.pop()
print(entire_sequence)

total=0
for i,c in enumerate(entire_sequence):
    total+=i*c
print(total)