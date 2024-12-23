from itertools import permutations
from functools import lru_cache
# test input
#codes=["029A","980A","179A","456A","379A"]

# challenge input
codes=["593A","283A","670A","459A","279A"]
def distance(layout):
    distances={}
    for y,row in enumerate(layout):
        for x,cell in enumerate(row):
            for y2,row2 in enumerate(layout):
                for x2,cell2 in enumerate(row2):
                    if cell !=" " and cell2!=" ":
                        if cell not in distances:
                            distances[cell] = {}
                        distances[cell][cell2] = (x2-x,y2-y, abs(x2-x)+abs(y2-y))
    return distances

numpad=[[" ","0","A"],["1","2","3"],["4","5","6"],["7","8","9"]]
numpad.reverse()

distance_numpad = distance(numpad)
#print(distance_numpad)

keypad=[["<","v",">"],[" ","^","A"]]
keypad.reverse()
distance_keypad = distance(keypad)

@lru_cache
def get_moves_needed(dx,dy):
    moves_needed=[]
    if dx < 0:
        moves_needed += ["<"]*abs(dx)
    else:
        moves_needed += [">"]*abs(dx)
    if dy < 0:
        moves_needed += ["^"]*abs(dy)
    else:
        moves_needed += ["v"]*abs(dy)
    return moves_needed

def filter_paths(paths,start,layout):
    filtered_paths=[]
    for path in paths:
        s=start
        for symbol in list(path):
            #print(symbol,s)
            match symbol:
                case "v":
                    s = (s[0],s[1]+1)
                case "^":
                    s = (s[0],s[1]-1)
                case ">":
                    s = (s[0]+1,s[1])
                case "<":
                    s = (s[0]-1,s[1])
            if layout[s[1]][s[0]] == " ":
                break
        else:
            filtered_paths.append(path)
    return filtered_paths

total=0
from tqdm import tqdm
for code in codes:
    position1="A"
    possible_paths=[]
    for symbol in list(code):
        dx,dy,d = distance_numpad[position1][symbol]
        moves_needed=get_moves_needed(dx,dy)
        position1 = symbol
        paths=list(set(["".join(y) for y in [list(x) for x in list(permutations(moves_needed))]]))
        if possible_paths == []:
            possible_paths = [path+"A" for path in paths]
        else:
            tp1=[]
            for x in possible_paths:
                for y in paths:
                    tp1.append(x+y+"A")
            possible_paths = tp1
    possible_paths = filter_paths(possible_paths,(2,3),numpad)
    # sort
    # keep only shortest paths
    shortest=min(len(x) for x in possible_paths)
    possible_paths = [x for x in possible_paths if len(x) == shortest]
    possible_paths2=[]
    for possible_path in possible_paths:
        #print(possible_path)
        position2="A"
        possible_paths2.append([])
        for symbol in list(possible_path):
            dx,dy,d = distance_keypad[position2][symbol]  
            moves_needed=get_moves_needed(dx,dy)
            position2 = symbol
            paths=list(set(["".join(y) for y in [list(x) for x in list(permutations(moves_needed))]]))
            if possible_paths2[-1] == []:
                possible_paths2[-1] = [path+"A" for path in paths]
            else:
                tp2=[]
                for x in possible_paths2[-1]:
                    for y in paths:
                        tp2.append(x+y+"A")
                possible_paths2[-1] = tp2
    # flatten
    possible_paths2 = [x for y in possible_paths2 for x in y]
    possible_paths2 = filter_paths(possible_paths2,(2,0),keypad)
    # keep only shortest paths
    shortest=min(len(x) for x in possible_paths2)
    possible_paths2 = [x for x in possible_paths2 if len(x) == shortest]
    #print(possible_paths2)
    possible_paths3=[]
    for possible_path2 in tqdm(possible_paths2):
        #print(possible_path2)
        possible_paths3.append([])
        position3="A"
        for symbol in list(possible_path2):
            dx,dy,d = distance_keypad[position3][symbol]
            moves_needed=get_moves_needed(dx,dy)
            position3 = symbol
            paths=list(set(["".join(y) for y in [list(x) for x in list(permutations(moves_needed))]]))
            if possible_paths3[-1] == []:
                possible_paths3[-1] = [path+"A" for path in paths]
            else:
                tp3=[]
                for x in possible_paths3[-1]:
                    for y in paths:
                        tp3.append(x+y+"A")
                possible_paths3[-1] = tp3
    # flatten
    possible_paths3 = [x for y in possible_paths3 for x in y]
    possible_paths3 = filter_paths(possible_paths3,(2,0),keypad)
    #print(possible_paths3)
    # keep only shortest paths
    shortest=min(len(x) for x in possible_paths3)
    total+=shortest*int(code[:-1])
    print(shortest)
        #print("----")
print(total)
