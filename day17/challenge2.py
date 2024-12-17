
# challenge input
registers=[45483412,0,0] # we ignore this because we are trying to find the initial value of A that copies the program
program=[2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0]
#2,4: B=A%8
#1,3: B=B^3
#7,5: C=A//(2**B)
#0,3: A=A//(2**3) <- only thing that determines A thus if output needs to be 16 long, we need to have A at least (8**15)
#4,1: B=B^C
#1,5: B=B^5
#5,5: output B%8
#3,0: if A!=0 jump to 0

# simplify program
# B=(A%8)^3
# C=A//(2**B)
# A=A//8
# B=B^C^5
# output B%8
# if A!=0 jump to 0


bits=[1 if i==0 else 0 for i in range(16)]
print(bits)


combo=[0,1,2,3,registers[0],registers[1],registers[2],None]


def simplified_program(A):
    l=[]
    B,C=0,0
    while A!=0:
        B=(A%8)^3
        C=A//(2**B)
        A=A//8
        B=B^C^5
        l.append(B%8)
    return l

#turn bits into a number
def to_number(bits):
    n=bits[0]
    for i in range(1,len(bits)):
        #shift left 3 times
        n=n<<3
        #add the next 3 bits
        n+=bits[i]
    return n



print(to_number(bits))

res=simplified_program(to_number(bits))
print(res)
# Honestly I am not sure how it works, but it does?
while res!=program:
    for i in range(len(res)):
        if res[len(res)-1-i]!=program[len(program)-1-i]:
            bits[i]+=1
            # especially this part does not make sense to me
            # So apparently it doesn't matter if the bit goes over 8 or something? Because it probably cumulates with the other ones
            # but we need to recheck the other numbers or something?
            # Maybe I just got lucky with my numbers 🤷‍♂️ anyways, I somehow got it 🤪
            if i!=0 and bits[i]==8:
                # reset bit 0
                bits[0]=0
            break
    res=simplified_program(to_number(bits))
    print(to_number(bits),bin(to_number(bits)),res,program)