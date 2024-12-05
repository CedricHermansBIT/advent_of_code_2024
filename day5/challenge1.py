rules=dict()
pages=[]

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    # This is just parsing the input file
    in_rules = True
    for line in ifile:
        # If we reach an empty line, we are in the pages, not in the rules anymore
        if line.strip() == "":
            in_rules = False
            continue
        # If we are in the rules, we are adding the rules to the rules dictionary
        # e.g. 53 should be after [47,75,61,97] in the testinput.txt
        if in_rules:
            before, after = map(int,line.strip().split("|"))
            if after in rules:
                # if key is present, elongate the list e.g. 53 should be after [47,75]
                rules[after].append(before)
            else:
                # first value, e.g. 53 should be after [47]
                rules[after] = [before]
        else:
            # if we are in the pages, we are adding the pages to the pages list, we will parse them later
            pages.append(line.strip())

#print(rules)
total=0
for page in pages:
    # parse the page into a list of integers
    items=list(map(int,page.split(",")))
    for i, item in enumerate(items):
        # for each item in the list, check if it is in the rules
        if item in rules:
            # if it is in the rules, there should not be a number in the rest of the list that is in the rules
            # e.g. if 53 then there should not be 47, 75, 61, 97 in the rest of the list, if there is, the page is invalid
            for rule in rules[item]:
                if rule in items[i+1:]:
                    #print(f"{page}: Invalid")
                    break
            else:
                # If you break out of the loop, you don't reach the else, so you continue to the next item
                continue
            # if we broke out of this loop, also break out of the outer loop
            break
    else:
        # if we didn't break out of the loop, the page is valid and we add the middle element to the total
        total+=items[len(items)//2]

print(total)