import random

rand_list = [ random.randrange(1,20) for i in range(10) ]
print(rand_list)

list_comprehension_below_10 = [r for r in rand_list if r < 10 ]
print(list_comprehension_below_10)

list_comprehension_below_10 = list(filter(lambda x: x < 10, rand_list))
