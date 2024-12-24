outputs={}
inputs={}

in_outputs=True
with open("challengeinput.txt","r") as ifile, open("dotfile.dot","w") as ofile:
#with open("testinput.txt","r") as ifile:
    ofile.write("digraph G {\n")
    for line in ifile:
        line=line.strip()
        if line=="":
            in_outputs=False
        elif in_outputs:
            a,b=line.split(": ")
            outputs[a]=int(b)
            ofile.write(f"{a} [label=\"{a}={b}\"];\n")
        else:
            a,gate,b,arrow,c=line.split(" ")
            inputs[tuple([a,b,c])]=gate
            ofile.write(f"{a},{b} -> {c} [label=\"{gate}\"];\n")
    ofile.write("}\n")

print(outputs)
print(inputs)


def solve(inputs,outputs):
    plen=len(inputs)
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
        if len(inputs)==plen:
            return None
        plen=len(inputs)

    output_keys = list(outputs.keys())
    filtered_keys=filter(lambda x: x.startswith("z"), output_keys)
    sorted_keys=list(filtered_keys)
    sorted_keys.sort(reverse=True)
    binary_string=""
    for key in sorted_keys:
        binary_string+=str(outputs[key])

    return int(binary_string,2)

get_x_outputs = filter(lambda x: x.startswith("x"), outputs.keys())
x_outputs = list(get_x_outputs)
x_outputs.sort(reverse=True)
x_str = ""
for x in x_outputs:
    x_str+=str(outputs[x])
get_y_outputs = filter(lambda x: x.startswith("y"), outputs.keys())
y_outputs = list(get_y_outputs)
y_outputs.sort(reverse=True)
y_str = ""
for y in y_outputs:
    y_str+=str(outputs[y])

expected_out=int(x_str,2)+int(y_str,2)
print(expected_out)

tested_keys=[]

input_keys = list(inputs.keys())

if solve(inputs,outputs)==expected_out:
    print("Success")
