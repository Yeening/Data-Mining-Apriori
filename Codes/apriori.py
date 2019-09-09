from main import *


def generate_item_set(transactions, support):
    support_count = support * len(transactions)
    item_dic = {}

    # get item set
    for transaction in transactions:
        for item in transaction:
            if item not in item_dic:
                item_dic[item] = 1
            else:
                item_dic[item] += 1

    fre_item_1 = {}
    for item in item_dic.keys():
        if item_dic[item] >= support_count:
            fre_item_1[item] = item_dic[item]

    print(len(fre_item_1),fre_item_1,'\n')
    generate(fre_item_1, support, 0, transactions)


def generate(item_dic, support, count, transactions):
    count += len(item_dic)
    support_count = support * len(transactions)
    next_dic = {}
    for item1 in item_dic.keys():
        for item2 in item_dic.keys():
            if item1 == item2:
                continue
            item_set1 = item1.split(',')
            item_set2 = item2.split(',')
            if item_set1[:-1] == item_set2[:-1]:
                temp_count = 0
                for transaction in transactions:
                    if contain(transaction,item_set1) and contain(transaction, item_set2):
                        temp_count += 1
                if temp_count >= support_count:
                    next_dic[item1+','+item2] = temp_count
    print(len(next_dic.keys()), next_dic)
    if len(next_dic) > 0:
        generate(next_dic, support, count, transactions)
    return count


def contain(transaction, item_set):
    for item in item_set:
        if item not in transaction:
            return False
    return True

generate_item_set(data_to_array(), 0.5)