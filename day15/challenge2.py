map=[]
moves=""
in_map=True
start=None
replace_dict={"#": ["#","#"], "O": ["[","]"], ".": [".","."], "@": ["@","."]}
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for n,line in enumerate(ifile):
        if line.strip() == "":
            in_map=False
        if in_map:
            map.append([])
            for c in line.strip():
                map[-1]+=replace_dict[c]
            if "@" in line:
                start=(n,line.index("@")*2)
        else:
            moves+=line.strip()
#print("number_of_boxes",sum([row.count("[") for row in map]))
#input()
#print(map)
#print(moves)
#print(start)

def check_move(map,position,direction,move_list):
    #print(position)
    if map[position[0]][position[1]] == "#":
        #print("Hit wall")
        return False, position, move_list
    if map[position[0]][position[1]] == ".":
        #print("Empty")
        return True, position, move_list
    py=position[0]
    px=position[1]
    pyn=py
    pxn=px
    current_symbol=map[py][px]
    match direction:
        case "^":
            if current_symbol in ["[","]"]:
                if current_symbol == "[":
                    left_half_moveable,_, move_list=check_move(map,(py-1,px),direction,move_list)
                    right_half_moveable,_, move_list=check_move(map,(py-1,px+1),direction,move_list)
                    #print(position)
                    #print("left_half_moveable",left_half_moveable)
                    #print("right_half_moveable",right_half_moveable)
                    can_move=left_half_moveable and right_half_moveable
                    if can_move:
                        move_list.add(position)
                        move_list.add((py,px+1))
                elif current_symbol == "]":
                    left_half_moveable,_, move_list=check_move(map,(py-1,px-1),direction,move_list)
                    right_half_moveable,_, move_list=check_move(map,(py-1,px),direction,move_list)
                    #print(position)
                    #print("left_half_moveable",left_half_moveable)
                    #print("right_half_moveable",right_half_moveable)
                    can_move=left_half_moveable and right_half_moveable
                    if can_move:
                        move_list.add(position)
                        move_list.add((py,px-1))
            else:
                # this is always @
                can_move,_,move_list=check_move(map,(py-1,px),direction,move_list)
                if can_move:
                    pyn-=1
                    move_list.add(position)
                    # sort list on y
                    ml=list(move_list)
                    ml.sort(key=lambda x: x[0])
                    print("move_list",move_list)
                    # update all positions
                    for pos in ml:
                        map[pos[0]-1][pos[1]]=map[pos[0]][pos[1]]
                        map[pos[0]][pos[1]]="."
                        #input()
                    move_list=[]
        case "v":
            if current_symbol in ["[","]"]:
                if current_symbol == "[":
                    left_half_moveable,_, move_list=check_move(map,(py+1,px),direction,move_list)
                    right_half_moveable,_, move_list=check_move(map,(py+1,px+1),direction,move_list)
                    #print(position)
                    #print("left_half_moveable",left_half_moveable)
                    #print("right_half_moveable",right_half_moveable)
                    can_move=left_half_moveable and right_half_moveable
                    if can_move:
                        move_list.add(position)
                        move_list.add((py,px+1))
                elif current_symbol == "]":
                    left_half_moveable,_, move_list=check_move(map,(py+1,px-1),direction,move_list)
                    right_half_moveable,_, move_list=check_move(map,(py+1,px),direction,move_list)
                    #print(position)
                    #print("left_half_moveable",left_half_moveable)
                    #print("right_half_moveable",right_half_moveable)
                    can_move=left_half_moveable and right_half_moveable
                    if can_move:
                        move_list.add((py,px-1))
                        move_list.add(position)
            else:
                # this is always @
                can_move,_,move_list=check_move(map,(py+1,px),direction,move_list)
                if can_move:
                    pyn+=1
                    move_list.add(position)
                    ml=list(move_list)
                    ml.sort(key=lambda x: x[0], reverse=True)
                    #print("move_list",ml)
                    # update all positions
                    for pos in ml:
                        #print("pos",pos)
                        map[pos[0]+1][pos[1]]=map[pos[0]][pos[1]]
                        map[pos[0]][pos[1]]="."
                        #print("\n".join(["".join(row) for row in map]))
                        #input()
                    move_list=[]
        case ">":
            can_move,_,_=check_move(map,(py,px+1),direction,move_list)
            if can_move:
                pxn+=1
                map[py][px+1]=map[py][px]
                map[py][px]="."
        case "<":
            can_move,_,_=check_move(map,(py,px-1),direction,move_list)
            if can_move:
                pxn-=1
                map[py][px-1]=map[py][px]
                map[py][px]="."
    return can_move, (pyn,pxn),move_list


for move in moves:
    print("\033[2J")
    print("\033[H")
    print(start,move)
    moved,start,_=check_move(map,start,move,set())
    # escape code for top left corner
    print("\n".join(["".join(row) for row in map]))
    #sleep(0.1)
    if not moved:
        print("Hit wall with move",move)
        #sleep(0.5)
    #print(start,move)
    #input()
result=0
for y,row in enumerate(map):
    for x,c in enumerate(row):
        if c == "[":
            result+=y*100+x

print(result)
print("number_of_boxes",sum([row.count("[") for row in map]))
print("number_of_boxes",sum([row.count("]") for row in map]))
