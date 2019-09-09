# from main import *


count = 0
frequent_sets = []


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


# print(generate_item_set(data_to_array(), 0.5))

