"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

# f(a) + f(b) -> [indecies]



def f(x):
    return x * 4 + 6

# TODO: Implement me.

# get the sums
# don't know how to make this linear
# It should be possible to use the same for loops
# with a single dict being used in a function call
sums_dict = {}
for i, value1 in enumerate(q):
    for j, value2 in enumerate(q):
        my_sum = f(value1) + f(value2)
        # print(value1, value2, my_sum)
        if my_sum not in sums_dict:
            sums_dict[my_sum] = [i, j]

'''
if f(c) - f(d) in sums_dict
    then we have a whole set

'''
# [print(i, sums_dict[i]) for i in sums_dict]
quadruple = []

for i, value1 in enumerate(q):
    for j, value2 in enumerate(q):

        my_difference = f(value1) - f(value2)
        
        
        if my_difference in sums_dict:
            first_pair = sums_dict[my_difference]
            quadruple.append(
                (   q[first_pair[0]],
                    q[first_pair[1]],
                    value1,
                    value2))


print(quadruple)