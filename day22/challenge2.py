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

all_dict={}
for secret in secrets:
    orig=secret
    all_dict[orig]={}
    p=[]
    for i in range(2000):
        new_secret=get_next_value(secret)
        last_digit=new_secret%10
        p.append(last_digit-(secret%10))
        if len(p)>=4:
            tup=tuple(p[-4:])
            if tup not in all_dict[orig]:
                all_dict[orig][tup]=last_digit
        secret=new_secret

all_subkeys=set()
for key in all_dict:
    for subkey in all_dict[key]:
        all_subkeys.add(subkey)

best_key=None
best_value=0
for subkey in all_subkeys:
    value=0
    for key in all_dict:
        if subkey in all_dict[key]:
            value+=all_dict[key][subkey]
    if value>best_value:
        best_value=value
        best_key=subkey
    #print(subkey,value)
print(best_value)
print(best_key)

