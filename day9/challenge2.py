with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    line=ifile.readline().strip()

entire_sequence=[]
length_per_id=dict()
index=0
file=True
for i,c in enumerate(line):
    if file:
        entire_sequence+=[index]*int(c)
        length_per_id[index]=int(c)
        index+=1
        file=False
    else:
        entire_sequence+=["."]*int(c)
        file=True

def calculate_missing(sequence):
    keys=[]
    length_per_missing={}
    missing=0
    for i,c in enumerate(sequence):
        if c==".":
            missing+=1
        else:
            if missing>0:
                keys.append(i-missing)
                length_per_missing[i-missing]=missing
                missing=0
    return keys,length_per_missing

keys,length_per_missing=calculate_missing(entire_sequence)

print(length_per_id)
print(length_per_missing)

for id_key in sorted(length_per_id.keys(),reverse=True):
    print(id_key)
    n=0
    while n<len(length_per_missing.keys()):
        missing_key=keys[n]  
        i=entire_sequence.index(id_key)
        if length_per_id[id_key]<=length_per_missing[missing_key] and i>missing_key:
            # replace id_key in entire_sequence with "."s
            for i,c in enumerate(entire_sequence):
                if c==id_key:
                    entire_sequence[i]="."
            for i in range(length_per_id[id_key]):
                entire_sequence[missing_key+i]=id_key
            keys,length_per_missing=calculate_missing(entire_sequence)
            #print(entire_sequence)
            n=0
        else:
            n+=1
            
print(entire_sequence)

total=0
for i,c in enumerate(entire_sequence):
    if c!=".":
        total+=i*c
print(total)