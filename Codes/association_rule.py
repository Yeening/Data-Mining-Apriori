#creating association rules from previous apriori itemset
import itertools
from itertools import chain,combinations

stored_rules = []

def generate_association_rule (frequent_sets):
    # start the loop from the back to have the parent set first
    # it stops at len(dict) = 2 (no point of going fewer than 2)
    for item_dict in frequent_sets[:1:-1]:
        for combination in item_dict:
            word_array = combination.split(',')
            all_subsets = all_possible_subsets(word_array)
            for



#list all subset except empty set and the set itself
def all_possible_subsets(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(1,len(s))))

#just pseudo code for now
def get_deeper(lhs, rhs, res):
    for i in lhs:
        rhs.add(i)
        temp_lhs =