with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    line=ifile.readline().strip()

entire_sequence=[]
index=0
file=True
for c in line:
    if file:
        entire_sequence+=[(index,int(c))]
        index+=1
        file=False
    else:
        if c!="0":
            entire_sequence+=[(-1,int(c))]
        file=True

#print(entire_sequence)
pos_later=len(entire_sequence)-1
while pos_later>0:
#pos_later, (id_later, amount_later) in enumerate(entire_sequence[::-1]):
    id_later, amount_later = entire_sequence[pos_later]
    #pos_later=len(entire_sequence)-1-pos_later
    
    if id_later != -1:
        #print(pos_later, id_later,amount_later)
        for pos_earlier, (id_earlier,amount_earlier) in enumerate(entire_sequence):
            if id_earlier == -1 and pos_later>pos_earlier:
                if amount_earlier >= amount_later:
                    # replace the first element with the second element
                    entire_sequence[pos_earlier]=(id_later,amount_later)
                    # replace the second element with missing (-1,value)
                    entire_sequence[pos_later]=(-1,amount_later)
                    # add remaining missing elements
                    if amount_earlier != amount_later:
                        entire_sequence=entire_sequence[:pos_earlier+1]+[(-1,amount_earlier-amount_later)]+entire_sequence[pos_earlier+1:]
                        pos_later+=1
                    #print(entire_sequence)
                    break
    pos_later-=1
#print(entire_sequence)
total=0       
index=0
for id,amount in entire_sequence:
    if id != -1:
        for i in range(amount):
            print(id,end="")
            #print(index,id)
            total+=index*id
            #print(total)
            index+=1
    else:
        index+=amount
        #print(index,0)
        print("."*amount,end="")
print()
print(total)