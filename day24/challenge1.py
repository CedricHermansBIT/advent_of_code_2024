outputs={}
inputs={}

in_outputs=True
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        line=line.strip()
        if line=="":
            in_outputs=False
        elif in_outputs:
            a,b=line.split(": ")
            outputs[a]=int(b)
        else:
            a,gate,b,arrow,c=line.split(" ")
            inputs[tuple([a,b,c])]=gate

print(outputs)
print(inputs)

while len(inputs)>0:
    keys = inputs.keys()
    #print(list(keys))
    for key in list(keys):
        a,b,c=key
        if a in outputs and b in outputs:
            #print(a,b)
            gate=inputs[key]
            if gate=="AND":
                outputs[c]=outputs[a] and outputs[b]
            elif gate=="OR":
                outputs[c]=outputs[a] or outputs[b]
            elif gate=="XOR":
                outputs[c]=outputs[a]^outputs[b]
            del inputs[key]

output_keys = list(outputs.keys())
filtered_keys=filter(lambda x: x.startswith("z"), output_keys)
sorted_keys=list(filtered_keys)
sorted_keys.sort(reverse=True)
binary_string=""
for key in sorted_keys:
    binary_string+=str(outputs[key])

print(int(binary_string,2))