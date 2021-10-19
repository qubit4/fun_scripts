### itertools, permutations, timeit

import timeit
import itertools

start = timeit.default_timer()


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number_ofpermutations = 0

result = itertools.permutations(data)

for each in result:
    print(each)
    number_ofpermutations += 1

print("Number of permutations of the following list: {} is {}.".format(data, number_ofpermutations))
    

stop = timeit.default_timer()
execution_time = stop - start

print("This program was executed in {} seconds. So fast!".format(execution_time)) 
