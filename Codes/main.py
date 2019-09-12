from apriori import *


def data_to_array():
    # Generate a transaction list from the data
    # transactions is list of transaction dictionaries
    file = open('../Data/associationruletestdata.txt', 'r')
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

#answer_Q1()
transactions = data_to_array()
print("Part 2, Q1")
template1("RULE", "ANY", {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("RULE", "NONE", {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("RULE", 1, {'G59_UP', 'G10_Down'}, 0.7, 0.5, True, transactions)
template1("HEAD", "ANY", {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("HEAD", "NONE", {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("HEAD", 1, {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("BODY", "ANY", {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("BODY", "NONE", {'G59_UP'}, 0.7, 0.5, True, transactions)
template1("BODY", 1, {'G59_UP', 'G10_DOWN'}, 0.7, 0.5, True, transactions)
print("Part 2, Q2")
template2("rule", 3, 0.7, 0.5, True, transactions)
template2("head", 2, 0.7, 0.5, True,transactions)
template2("body", 1, 0.7, 0.5, True, transactions)

print("Part 2, Q3")
template3(transactions,0.7, 0.5, "1or1", "HEAD", "ANY", {"G10_DOWN"}, "BODY", 1, {"G59_UP"})
template3(transactions,0.7, 0.5, "1and1", "HEAD", "ANY", {"G10_DOWN"}, "BODY", 1, {"G59_UP"})
template3(transactions,0.7, 0.5, "1or2", "HEAD", "ANY", {"G10_DOWN"}, "BODY", 2)
template3(transactions,0.7, 0.5, "1and2", "HEAD", "ANY", {"G10_DOWN"}, "BODY", 2)
template3(transactions,0.7, 0.5, "2or2", "HEAD", 1, "BODY", 2)
template3(transactions,0.7, 0.5, "2and2", "HEAD", 1, "BODY", 2)



# answer_Q1()
# run_Q1(0.7)
# run_Q1(0.5)