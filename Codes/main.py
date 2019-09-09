# from apriori import *


def data_to_array():
    # Generate a transaction list from the data
    file = open('../Data/associationruletestdata.txt', 'r')
    transactions = []
    for line in file:
        item_set = line.split()
        transaction = {}
        for i in range(100):
            # item_set[i] = 'G' + str(i+1) + '_' + item_set[i].upper()
            transaction['G' + str(i+1) + '_' + item_set[i].upper()] = 1
        transaction[item_set[100]] = 1
        transactions.append(transaction)
    return transactions


# data_to_array()
# print(data_to_array())
