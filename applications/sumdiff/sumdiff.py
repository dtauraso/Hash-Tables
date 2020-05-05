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

sums_dict = {}
a_i = 0
b_i = 1
while b_i < len(q):

    my_sum = q[a_i] + q[b_i]
    if my_sum not in sums_dict:
        sums_dict[my_sum] = [a_i, b_i]

'''
if f(c) - f(d) in sums_dict
    then we have a whole set

'''
quadruple = []
c_i = 0
d_i = 1

while d_i < len(q):
    my_difference = q[c_i] - q[d_i]
    if my_difference in sums_dict:
        first_pair = sums_dict[my_difference]
        quadruple.append(
            (   q[first_pair[0]],
                q[first_pair[1]],
                q[c_i],
                q[d_i]))
                