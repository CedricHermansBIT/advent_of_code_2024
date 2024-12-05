rules=dict()
pages=[]

# same as challenge 1
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    in_rules = True
    for line in ifile:
        if line.strip() == "":
            in_rules = False
            continue
        if in_rules:
            before, after = map(int,line.strip().split("|"))
            if after in rules:
                rules[after].append(before)
            else:
                rules[after] = [before]
        else:
            pages.append(line.strip())

#print(rules)

# extract the function that checks if it is correct
def check_and_fix(items: list, rules,d=0):
    for i, item in enumerate(items):
        if item in rules:
            for rule in rules[item]:
                if rule in items[i+1:]:
                    # swap the item with the first item that is not in the rules

                    # find the first item index that is breaking the rule
                    wrong_item_id=items.index(rule)
                    # swap the items
                    items[i], items[wrong_item_id] = items[wrong_item_id], items[i]
                    # recursive strategy to fix the items
                    return check_and_fix(items, rules,d+1)
                    #print(f"{page}: Invalid")
            else:
                continue
    # we only need incorrect pages, so if depth > 0, we fixed something
    if d!=0:
        #print(f"Fixed {d} items")
        #print(items)
        # return the middle element of the fixed list
        return items[len(items)//2]
    # else we just return 0
    return 0

#print(rules)
total=0
for page in pages:
    items=list(map(int,page.split(",")))
    total+=check_and_fix(items, rules)
print(total)