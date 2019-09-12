from main import data_to_array


count = 0
frequent_sets = []
heads = []
bodies = []


def generate_item_set(transactions, support):
    global count, frequent_sets
    count = 0
    frequent_sets = []
    support_count = support * len(transactions)
    item_dic = {}

    # get item set
    for transaction in transactions:
        for item in transaction:
            if item not in item_dic:
                item_dic[item] = 1
            else:
                item_dic[item] += 1

    # filter the item set for the first time
    # get the frequent item set with length 1
    fre_item_1 = {}
    for item in item_dic:
        if item_dic[item] >= support_count:
            fre_item_1[item] = item_dic[item]

    # print(len(fre_item_1),fre_item_1,'\n')
    generate(fre_item_1, support_count, 0, transactions, 1)
    return frequent_sets, count


def generate(item_dic, support_count, _count, transactions, length):
    # add the count of current frequent item set
    global count,frequent_sets
    count += len(item_dic)
    frequent_sets.append(item_dic)
    # print("number of length-" + str(length) + " frequent itemsets: ")
    # frequent item set of next level
    next_dic = {}
    for item1 in item_dic:
        for item2 in item_dic:
            if item1 >= item2:  # skip equal
                continue
            # get list from string
            item_set1 = item1.split(',')
            item_set2 = item2.split(',')
            # only combine when set1 and set2 have same items except the last one
            if item_set1[:-1] == item_set2[:-1]:
                temp_count = 0
                for transaction in transactions:
                    # transaction contains both set1 and set2
                    if contain(transaction, item_set1) and contain(transaction, item_set2):
                        temp_count += 1
                if temp_count >= support_count:
                    next_dic[item1+','+str(item_set2[-1])] = temp_count
    # print(len(next_dic.keys()), next_dic)
    if len(next_dic) > 0:
        generate(next_dic, support_count, count, transactions, length+1)
    # return count


def contain(transaction, item_set):
    for item in item_set:
        if item not in transaction:
            return False
    return True


def confidence(rule_set, head_set, frequent_sets):
    if len(head_set) == 0 or len(rule_set) == len(head_set):
        return 0
    # print(frequent_sets[len(lst1)-1])
    count_lst1 = float(frequent_sets[len(rule_set)-1].get(','.join(rule_set)))
    # print(frequent_sets[len(lst2) - 1])
    count_lst2 = float(frequent_sets[len(head_set)-1].get(','.join(head_set)))
    return count_lst1 / count_lst2


# # apriori algorithm for association rule
# def get_deeper(lhs, rhs, res, confidence_threshold, frequent_sets):
#     parent_list = lhs
#     for i in lhs:
#         rhs.add(i)
#         temp_lhs = intersection(lhs, rhs)
#         if (confidence(parent_list, temp_lhs, frequent_sets) > confidence_threshold):
#             res[','.join(lhs) + "->" + ','.join(rhs)] = 1  # adding the rules to the stored value
#             get_deeper(lhs, rhs, res, confidence_threshold, frequent_sets)


def get_deeper(left, right, _confidence, associations, frequent_sets):
    if len(left) == 0:
        return
    rule = left + right
    rule.sort()
    left.sort()
    if confidence(rule, left, frequent_sets) > _confidence:
        associations.add(str(left+['-']+right))
    for item in left:
        left.remove(item)
        right.append(item)
        get_deeper(left,right,_confidence, associations, frequent_sets)
        left.append(item)
        right.remove(item)


def generate_associations(_confidence, support, transactions):
    frequent_sets, _count = generate_item_set(data_to_array(), support)
    associations = set({})
    for item_sets in frequent_sets[1:]:
        for i in item_sets:
            item_set = i.split(',')
            left = item_set
            right = []
            get_deeper(left, right, _confidence, associations, frequent_sets)
    # print(associations)
    return associations

def ass_str_to_list(s):
    s1 = s.strip('[').strip(']')
    l = s1.split(',')
    left = []
    right = []
    block = 0
    for i in range(len(l)):
        if '-' in l[i]:
            block = i
    for i in range(len(l)):
        if i < block:
            left.append(l[i].lstrip()[1:-1])
        if i > block:
            right.append(l[i].lstrip()[1:-1])
    return left, right

#Part 2 template 1
def template1(position, number, combination): #combination should be a set
    local_rules = set({})
    position = position.upper()  # avoid any lower case input
    if (type(number) == str): #change number to all upper case letters
        number.upper()

    if number == "NONE":
        if position == "RULE":
            counter = 0
            for i in range(len(heads)):
                head_line = [item for item in heads[i] if item in combination]
                body_line = [item for item in bodies[i] if item in combination]
                if (len(head_line) > 0 or len(body_line) > 0):
                    counter += 1
                else:
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))
                    
            print("Template 1 output: " + str(len(heads) - counter) + ". (Ignore this output for template 3.)")

        elif position == "HEAD":
            counter = 0
            for i in range(len(heads)):
                head_line = [item for item in heads[i] if item in combination]
                if (len(head_line) > 0):
                    counter += 1
                else:
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))
                    
            print("Template 1 output: "  + str(len(heads) - counter) + ". (Ignore this output for template 3.)")

        elif position == "BODY":
            counter = 0
            for i in range(len(bodies)):
                body_line = [item for item in heads[i] if item in combination]
                if (len(body_line) > 0):
                    counter += 1
                else:
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

            print("Template 1 output: " + str(len(heads) - counter) + ". (Ignore this output for template 3.)")

    elif number == "ANY":
        if position == "RULE":
            counter = 0
            for i in range(len(heads)):
                head_line = [item for item in heads[i] if item in combination]
                body_line = [item for item in bodies[i] if item in combination]
                if (len(head_line) > 0 or len(body_line) > 0):
                    counter += 1
                    
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))
                    
            print("Template 1 output: " + str(counter) + ". (Ignore this output for template 3.)")

        elif position == "HEAD":
            counter = 0
            for i in range(len(heads)):
                head_line = [item for item in heads[i] if item in combination]
                if (len(head_line) > 0):
                    counter += 1
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

            print("Template 1 output: " + str(counter) + ". (Ignore this output for template 3.)")

        elif position == "BODY":
            counter = 0
            for i in range(len(bodies)):
                body_line = [item for item in heads[i] if item in combination]
                if (len(body_line) > 0):
                    counter += 1
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

            print("Template 1 output: " + str(counter) + ". (Ignore this output for template 3.)")
            
    else:
        if position == "RULE":
            counter = 0
            for i in range(len(heads)):
                head_line = [item for item in heads[i] if item in combination]
                body_line = [item for item in bodies[i] if item in combination]
                if (len(head_line) + len(body_line) == number):
                    counter += 1
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

            print("Template 1 output: " + str(counter) + ". (Ignore this output for template 3.)")

        elif position == "HEAD":
            counter = 0
            for i in range(len(heads)):
                head_line = [item for item in heads[i] if item in combination]
                if (len(head_line) == number):
                    counter += 1
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

            print("Template 1 output: " + str(counter) + ". (Ignore this output for template 3.)")

        elif position == "BODY":
            counter = 0
            for i in range(len(bodies)):
                body_line = [item for item in heads[i] if item in combination]
                if (len(body_line) == number):
                    counter += 1
                    local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

            print("Template 1 output: " + str(counter) + ". (Ignore this output for template 3.)")
        
        return local_rules

#Part 2 Template 2
def template2(position, number):
    local_rules = set({})

    position = position.upper()

    if position == "RULE":
        counter = 0
        for i in range (len(heads)):
            if (len(heads[i]) + len(bodies[i]) >= number):
                counter += 1
                local_rules.add(str(heads[i]) + '->' + str(bodies[i]))
            
        print("Template 2 output: " + str(counter) + ". (Ignore this output for template 3.)")

    elif position == "HEAD":
        counter = 0
        for i in range(len(heads)):
            if (len(heads[i]) >= number):
                counter += 1
                local_rules.add(str(heads[i]) + '->' + str(bodies[i]))
        print("Template 2 output: " + str(counter) + ". (Ignore this output for template 3.)")

    else:
        counter = 0
        for i in range(len(bodies)):
            if (len(bodies[i]) >= number):
                counter += 1
                local_rules.add(str(heads[i]) + '->' + str(bodies[i]))

        print("Template 2 output: " + str(counter) + ". (Ignore this output for template 3.)")

    return local_rules

#Part 2 template 3
def template3 (arg1, *args):
    if (arg1 == "1or1"):
        rule1 = template1(args[1], args[2], args[3])
        rule2 = template1(args[4], args[5], args[6])
        print("Template 3 output: " + str(len(rule1.union(rule2))))

    elif(arg1 == "1and1"):
        rule1 = template1(args[1], args[2], args[3])
        rule2 = template1(args[4], args[5], args[6])
        print("Template 3 output: " + str(len(rule1.intersection(rule2))))

    elif(arg1 == "1or2"):
        rule1 = template1(args[1], args[2], args[3])
        rule2 = template2(args[4], args[5])
        print("Template 3 output: " + str(len(rule1.union(rule2))))

    elif(arg1 == "1and2"):
        rule1 = template1(args[1], args[2], args[3])
        rule2 = template2(args[4], args[5])
        print("Template 3 output: " + str(len(rule1.intersection(rule2))))

    elif(arg1 == "2or2"):
        rule1 = template1(args[1], args[2])
        rule2 = template2(args[3], args[4])
        print("Template 3 output: " + str(len(rule1.union(rule2))))

    elif(arg1 == "2and2"):
        rule1 = template1(args[1], args[2])
        rule2 = template2(args[3], args[4])
        print("Template 3 output: " + str(len(rule1.intersection(rule2))))



# s = "['G82_DOWN', '-', 'G72_UP', 'G59_UP']"
#
# left,right = ass_str_to_list(s)
# print(left,right)
associations = generate_associations(0.7, 0.5, generate_item_set(data_to_array(), 0.5))
# associations= generate_associations(0.7, 0.5, generate_item_set())
for association in associations:
    left, right = ass_str_to_list(association)
    heads.append(left)
    bodies.append(right)

counter = 0
for i in range(len(heads)):
    counter += 1
    print(str(heads[i]) + "->" + str(bodies[i]))
print(counter)

template1("RULE", "NONE", {"G96_DOWN", "G59_UP"})

template2("rule", 3)
