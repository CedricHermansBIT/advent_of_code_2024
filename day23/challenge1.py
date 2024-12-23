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

#print(connections)

three_way_connections=[]
for a, value in connections.items():
    for v in value:
        value_copy=value.copy()
        value_copy.remove(v)
        intersect=value_copy.intersection(connections[v])
        for i in intersect:
            combo = set([a,v,i])
            if combo not in three_way_connections:
                three_way_connections.append(combo)

print(three_way_connections)
three_way_connections_with_t=[]
for t in three_way_connections:
    for v in t:
        if v.startswith("t") and t not in three_way_connections_with_t:
            three_way_connections_with_t.append(t)
            break

print(three_way_connections_with_t)
print(len(three_way_connections_with_t))