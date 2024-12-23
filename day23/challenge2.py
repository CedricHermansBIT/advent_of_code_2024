connections={}
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        a,b=line.strip().split("-")
        if a not in connections:
            connections[a]=set()
        if b not in connections:
            connections[b]=set()
        connections[a].add(b)
        connections[b].add(a)

print(connections)

def test_intersection(intersection,interconnected,n=2):
    #print(intersection,n)
    if len(intersection)!=0:
        for v in intersection:
            interconnected.append(v)
            return test_intersection(intersection.intersection(connections[v]),interconnected,n+1)
    else:
        return n,interconnected
longest=0
lon_connections=[]
for key in connections:
    for v in connections[key]:
        n,c = test_intersection(connections[key].intersection(connections[v]),[key,v])
        if n>longest:
            longest=n
            lon_connections=c

lon_connections.sort()
print(longest,",".join(lon_connections))
