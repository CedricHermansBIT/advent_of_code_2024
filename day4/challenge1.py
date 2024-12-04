import numpy as np
# Tried to include a bit more comments in this one :)

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    # Read entire file into memory and then strip of newlines
    lines=ifile.readlines()
Hlines=[x.strip() for x in lines]

# Get the width and height of the grid (is the same in challenge input)
w=len(Hlines[0])
h=len(Hlines)

# We could reverse the lines to get the opposite search string, however
# we can also just reverse the pattern we search for
searchStrings=["XMAS","SAMX"]

# Get the diagonal lines
# first construct empty strings for each diagonal line
Dlines=["" for _ in range(w+h-1)]
for i in range(w+h-1):
    for j in range(h):
        if i-j>=0 and i-j<w:
            # Add the character to the diagonal line
            Dlines[i]+=Hlines[j][i-j]

# To get reverse diagonal lines, we could change the entire loop logic
# this requires a lot of thinking, and maybe some drawing to get it right
# Instead: just mirror the input lines and get the diagonal lines again :)
rev_Hlines = [x[::-1] for x in Hlines]

RDlines=["" for x in range(w+h-1)]
for i in range(w+h-1):
    for j in range(h):
        if i-j>=0 and i-j<w:
            RDlines[i]+=rev_Hlines[j][i-j]

# Vertical lines are just the columns of the input, so we can just transpose the input
# Transpose can be easily done with numpy, but we could also do it manually
Vlines = np.transpose([list(x) for x in Hlines]).tolist()
Vlines = ["".join(x) for x in Vlines]

count=0
# In all possible cases (H,V,D,RD), we can just loop over all lines and count the occurences
for lines in [Hlines,Vlines,Dlines,RDlines]:
    for line in lines:
        for s in searchStrings:
            # Overlapping counts are allowed, count doesn't do overlap
            # however, XMAS can never overlap... so we don't need to worry about that :)
            count+=line.count(s)
print(count)