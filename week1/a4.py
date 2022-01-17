from itertools import chain
from collections import defaultdict

dict_first = {"apple" : 30, "pear" : 15, "persimmom" : 10, "grape" : 10}
dict_second = {"apple" : 5, "persimmon" : 25, "pear" : 15, "mandarin" : 25}

def merge_dict(input_dict1, input_dict2):
    output_dict = defaultdict(list) #define the dict stored the list as element
    for k, v in chain(input_dict1.items(), input_dict2.items()): #loop based on the input dicts
        output_dict[k].append(v) #append the list
    
    for k, v in output_dict.items():
        output_dict[k] = sum(v) #sum of the list elements
    
    return output_dict 
        
print(merge_dict(dict_first, dict_second))