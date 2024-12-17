# test inputs
#registers=[729,0,0]
#program=[0,1,5,4,3,0]

# Example 1
#registers = [0, 0, 9]  # Register C contains 9
#program = [2, 6]
# Expected result: register B is set to 1

# Example 2
#registers = [10, 0, 0]  # Register A contains 10
#program = [5, 0, 5, 1, 5, 4]
# Expected result: output 0, 1, 2

# Example 3
#registers = [2024, 0, 0]  # Register A contains 2024
#program = [0, 1, 5, 4, 3, 0]
# Expected result: output 4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0 and leave 0 in register A

# Example 4
#registers = [0, 29, 0]  # Register B contains 29
#program = [1, 7]
# Expected result: register B is set to 26

# Example 5
#registers = [0, 2024, 43690]  # Register B contains 2024 and register C contains 43690
#program = [4, 0]
# Expected result: register B is set to 44354

# challenge input
registers=[45483412,0,0]
program=[2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0]


combo=[0,1,2,3,registers[0],registers[1],registers[2],None]
instructions={
    0: "adv",
    1: "bxl",
    2: "bst",
    3: "jnz",
    4: "bxc",
    5: "out",
    6: "bdv",
    7: "cdv"
}

pointer=0
while pointer<len(program):
    ins=instructions[program[pointer]]
    literal=program[pointer+1]
    comb=combo[literal]
    #print(f"Pointer: {pointer}, Instruction: {ins}, Combo: {comb}, Literal: {literal}, Registers: {combo[4:7]}")
    match ins:
        case "adv":
            combo[4]=combo[4]//(2**comb)
            pointer+=2
        case "bxl":
            combo[5]=combo[5]^literal
            pointer+=2
        case "bst":
            combo[5]=comb%8
            pointer+=2
        case "jnz":
            if combo[4]!=0:
                pointer=literal
            else:
                pointer+=2
        case "bxc":
            combo[5]=combo[5]^combo[6]
            pointer+=2
        case "out":
            print(f"{comb%8},", end="")
            pointer+=2
        case "bdv":
            combo[5]=combo[4]//(2**comb)
            pointer+=2
        case "cdv":
            combo[6]=combo[4]//(2**comb)
            pointer+=2
        case _:
            print("Invalid instruction")
            break
#print(f"Pointer: {pointer}, Instruction: {ins}, Combo: {comb}, Literal: {literal}, Registers: {combo[4:7]}")

print()