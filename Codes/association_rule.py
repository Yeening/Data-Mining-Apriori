#creating association rules from previous apriori itemset
import itertools
from itertools import chain,combinations

stored_rules = {}

def generate_association_rule (frequent_sets, confidence_threshold):
    # start the loop from the back to have the parent set first
    # it stops at len(dict) = 2 (no point of going fewer than 2)
    for item_dict in frequent_sets[2:]:
        for combination in item_dict:
            word_array = combination.split(',')
            rhs = []
            get_deeper(word_array, rhs, stored_rules, confidence_threshold,frequent_sets) #storing association rules to it



#list all subset except empty set and the set itself
def all_possible_subsets(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(1,len(s))))



#apriori algorithm for association rule
def get_deeper(lhs, rhs, res, confidence_threshold,frequent_sets):
    parent_list = lhs
    for i in lhs:
        rhs.add(i)
        temp_lhs = intersection(lhs, rhs)
        if (confidence(parent_list, temp_lhs,frequent_sets) > confidence_threshold):
            res[','.join(lhs) + "->" + ','.join(rhs)] = 1 #adding the rules to the stored value
            get_deeper(lhs,rhs,res,confidence_threshold,frequent_sets)

#list intersection
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

#find the subset of a given number
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

#calculate confidence
def confidence(lst1, lst2, frequent_sets):
    count_lst1 = frequent_sets[len(lst1)].get(','.join(lst1))
    count_lst2 = frequent_sets[len(lst2)].get(','.join(lst2))
    return count_lst1/count_lst2

#output template 1
#input for position: RULE, HEAD, BODY
#input for number: ANY, NONE, 1,2,3,...,n
#input for combination: any combination
def template1(position, number, combination):
    position = position.upper() #avoid any lower case input
    if number == "None":
        
    elif number == "ANY":

    else:
        findsubsets(combination, number)


#output template 2

#output template 3