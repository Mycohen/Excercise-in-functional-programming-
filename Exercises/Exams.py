from functools import reduce

def f(L1, L2):
    def f_helper(x):
        return all(reduce(lambda n1, n2: n1 and x % n2 == 0,L2, True))
    return list(filter(f_helper, L1))





L1=range(20)
L2=range(3, 10,3)
print(f(L1, L2))