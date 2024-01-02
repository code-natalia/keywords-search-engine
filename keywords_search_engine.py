import sys
from functools import reduce, cmp_to_key


def generate_reduce_func(required):
    def reduce_func(aggr, word):
        return aggr[0] + (1 if word in required else 0), aggr[1] - (1 if word not in required else 0)
    return reduce_func

def generate_comapre(req_set):
    def compare(lcoll, rcoll):
        l = reduce(generate_reduce_func(req_set), set(lcoll), (0, 0))
        r = reduce(generate_reduce_func(req_set), set(rcoll), (0, 0))
        return (l > r) - (l < r)
    return compare

def open_file(file_name):
    with open(file_name, "r") as f:
        return [line.split() for line in f]
    
print(sorted(
    open_file(sys.argv[1]),
    key=cmp_to_key(generate_comapre(set(input("Podaj wymagana elementy(słowa) oddzielone spacją:\n").split()))), 
    reverse=True
))