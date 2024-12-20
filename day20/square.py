# Additional file for testing purposes, to determine a diamond area around a center point with a given radius.

center=(20,20)
radius=6

def manhattan_distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def is_inside_square(center,radius,point):
    return manhattan_distance(center,point)<=radius

for y in range(41):
    for x in range(40):
        if is_inside_square(center,radius,(x,y)):
            if center==(x,y):
                print('O',end='')
            else:
                print('*',end='')
        else:
            print(' ',end='')
    print()

for y in range(center[0]-radius,center[0]+radius+1):
    for x in range(center[1]-radius,center[1]+radius+1):
        if is_inside_square(center,radius,(x,y)):
            if center==(x,y):
                print('O',end='')
            else:
                print('*',end='')
        else:
            print(' ',end='')
    print()
