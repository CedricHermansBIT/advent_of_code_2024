numbers=[510613, 358, 84, 40702, 4373582, 2, 0, 1584]

def get_numbers(number):
    new_numbers=[]
    if n == 0:
        new_numbers.append(1)
    elif len(str(n))%2==0:
        n1=int(str(n)[:len(str(n))//2])
        n2=int(str(n)[len(str(n))//2:])
        new_numbers.append(n1)
        new_numbers.append(n2)
    else:
        new_numbers.append(n*2024)
    return new_numbers

for i in range(25):
    new_numbers=[]
    for n in numbers:
        if n == 0:
            new_numbers.append(1)
        elif len(str(n))%2==0:
            n1=int(str(n)[:len(str(n))//2])
            n2=int(str(n)[len(str(n))//2:])
            new_numbers.append(n1)
            new_numbers.append(n2)
        else:
            new_numbers.append(n*2024)
    numbers=new_numbers
    print(i, len(numbers))

# just keep track of the amount you have of same numbers, don't handle them individually