from apriori import *
from pathlib import Path
import os


def data_to_array():
    # Generate a transaction list from the data
    # transactions is list of transaction dictionaries
    grand_parent_path = Path(__file__).parents[1] #change it so the program runs on any platform/os
    file = open(os.path.join(grand_parent_path, "Data", "associationruletestdata.txt"), 'r')
    transactions = []
    for line in file:
        item_set = line.split()
        transaction = {}
        for i in range(100):  # add the count of Genes
            transaction['G' + str(i+1) + '_' + item_set[i].upper()] = 1
        # add diseases
        transaction[item_set[100]] = 1
        transactions.append(transaction)
    return transactions


def run_Q1(support):
    res, _count = generate_item_set(data_to_array(), support)
    print("Support is set to be "
          + str(support*100)
          + "%")
    for item_sets in res:
        print("number of length-"
              + str(len(list(item_sets.keys())[0].split(',')))
              + " frequent itemsets: "
              + str(len(item_sets)))
    print("number of all lengths frequent itemsets: "
           + str(_count) + '\n')


def answer_Q1():
    supports = [0.3, 0.4, 0.5, 0.6, 0.7]
    for support in supports:
        run_Q1(support)


#Sample Running

#answer_Q1()
#run_Q1(0.7)
