map=[]
moves=""
in_map=True
start=None
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for n,line in enumerate(ifile):
        if line.strip() == "":
            in_map=False
        if in_map:
            map.append([c for c in line.strip()])
            if "@" in line:
                start=[n,line.index("@")]
        else:
            moves+=line.strip()

print(map)
print(moves)
print(start)

def check_move(map,position,direction):
    print(position)
    if map[position[0]][position[1]] == "#":
        return False, position
    if map[position[0]][position[1]] == ".":
        return True, position
    py=position[0]
    px=position[1]
    pyn=py
    pxn=px
    match direction:
        case "^":
            res,_=check_move(map,(py-1,px),direction)
            if res:
                pyn-=1
                map[py-1][px]=map[py][px]
                map[py][px]="."
        case "v":
            res,_=check_move(map,(py+1,px),direction)
            if res:
                pyn+=1
                map[py+1][px]=map[py][px]
                map[py][px]="."
        case ">":
            res,_=check_move(map,(py,px+1),direction)
            if res:
                pxn+=1
                map[py][px+1]=map[py][px]
                map[py][px]="."
        case "<":
            res,_=check_move(map,(py,px-1),direction)
            if res:
                pxn-=1
                map[py][px-1]=map[py][px]
                map[py][px]="."
    return res, [pyn,pxn]
            

for move in moves:
    start=check_move(map,start,move)[1]
    print("\n".join(["".join(row) for row in map]))
    print(start)

result=0
for y,row in enumerate(map):
    for x,c in enumerate(row):
        if c == "O":
            result+=y*100+x

print(result)