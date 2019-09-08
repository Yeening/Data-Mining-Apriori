

def data_to_array():
    file = open('../Data/associationruletestdata.txt', 'r')
    transactions = []
    for line in file:
        transactions.append(line.split())
    return transactions

