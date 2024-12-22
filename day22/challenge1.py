secrets=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        secrets.append(int(line.strip()))
        

def get_next_value(value):
    t1=(value^(value*64))%16777216
    t2=t1^(t1//32)%16777216
    t3=t2^(t2*2048)%16777216
    return t3

t=0
for secret in secrets:
    for i in range(2000):
        secret=get_next_value(secret)
    t+=secret
print(t)