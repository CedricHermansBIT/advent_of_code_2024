from PIL import Image
class Guard:
    def __init__(self, line):
        #p=0,4 v=3,-3
        p=line.split(" ")[0][2:].split(",")
        v=line.split(" ")[1][2:].split(",")
        self.position=(int(p[0]),int(p[1]))
        self.velocity=(int(v[0]),int(v[1]))

    def move(self,w,h):
        self.position=((self.position[0]+self.velocity[0])%(w),(self.position[1]+self.velocity[1])%(h))

    def __str__(self):
        return f"Guard at {self.position} with velocity {self.velocity}"

class Board:
    def __init__(self,width,height):
        self.guards=[]
        self.width=width
        self.height=height
        self.halfwidth=self.width//2
        self.halfheight=self.height//2

    def addGuard(self,line):
        self.guards.append(Guard(line))

    def moveGuards(self):
        for guard in self.guards:
            guard.move(self.width,self.height)
    
    def printGuards(self):
        for guard in self.guards:
            print(guard)

    def return_guards_per_quadrant(self):
        q1=0
        q2=0
        q3=0
        q4=0
        for guard in self.guards:
            if guard.position[0]<self.halfwidth and guard.position[1]<self.halfheight:
                q1+=1
            elif guard.position[0]>self.halfwidth and guard.position[1]<self.halfheight:
                q2+=1
            elif guard.position[0]<self.halfwidth and guard.position[1]>self.halfheight:
                q3+=1
            elif guard.position[0]>self.halfwidth and guard.position[1]>self.halfheight:
                q4+=1
        return (q1,q2,q3,q4)

    def saveImage(self,filename):
        img=Image.new("RGB",(self.width,self.height),"black")
        for guard in self.guards:
            img.putpixel(guard.position,(255,255,255))
        img.save(filename)

board=Board(101,103)
with open("challengeinput.txt","r") as ifile:
#board=Board(11,7)
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        board.addGuard(line)

#board.printGuards()
#board.printBoard()
counter=0
while counter<10000:
    counter+=1
    board.moveGuards()
    if counter==7344:
        board.saveImage(f"images/output{counter}.png")

qs=board.return_guards_per_quadrant()
#multiply all 
from math import prod
print(prod(qs))
