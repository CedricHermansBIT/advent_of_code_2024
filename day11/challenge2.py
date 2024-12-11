from collections import defaultdict

numbers={510613:1, 358:1, 84:1, 40702:1, 4373582:1, 2:1, 0:1, 1584:1}
#numbers={125:1, 17:1}
# just keep track of the amount you have of same numbers, don't handle them individually

for i in range(75):
    new_numbers=defaultdict(int)
    for n in numbers.keys():
        if n == 0:
            new_numbers[1]+=numbers[n]
        elif len(str(n))%2==0:
            n1=int(str(n)[:len(str(n))//2])
            n2=int(str(n)[len(str(n))//2:])
            new_numbers[n1]+=numbers[n]
            new_numbers[n2]+=numbers[n]
        else:
            new_numbers[n*2024]+=numbers[n]
    numbers=new_numbers
    print(i, len(numbers))
print(sum(numbers.values()))