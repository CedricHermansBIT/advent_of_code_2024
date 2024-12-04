import re

# Tried to include a bit more comments in this one :)

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    # Read entire file into memory and then strip of newlines
    lines=ifile.readlines()
lines=[list(x.strip()) for x in lines]

convolutions=[]
# This is a hand-made 3x3 convolution that boils down to a 9-character string
# e.g

# XMAS
# MASX
# ASXM
# SXMA

# Draw basically a 3x3 grid and draw the 4 possible patterns -> 4 strings of 9 characters

for i in range(len(lines)-2):
    for j in range(len(lines[0])-2):
        for x in range(3):
            for y in range(3):
                if x==0 and y==0:
                    convolutions.append(lines[i+x][j+y])
                else:
                    convolutions[-1]+=lines[i+x][j+y]

# There are only 4 valid patterns for the X-MASses, so we can convert them to regexes
# (This is because the . positions don't matter, they can be whatever.)
valid_patters=[
    "M.M.A.S.S",
    "M.S.A.M.S",
    "S.S.A.M.M",
    "S.M.A.S.M",
]
count=0
for conv in convolutions:
    for p in valid_patters:
        if re.match(p,conv):
            count+=1

print(count)
