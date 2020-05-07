cache = {}
def expensive_seq(x, y, z):
    # Implement me
    global cache

    if x <= 0:
        return y + z
    if x > 0:
        # print(x, y, z)
        # [print(i, cache[i]) for i in cache]
        first_tuple = (x - 1, y + 1, z)
        second_tuple = (x - 2, y + 2, z * 2)
        third_tuple = (x - 3, y + 3, z * 3)

        # allows the result of one of the tuples to have an answer dependent
        # on a previous tuple being calculated

        if  first_tuple not in cache:
            cache[first_tuple] = expensive_seq(x - 1, y + 1, z)
        if second_tuple not in cache:
            cache[second_tuple] = expensive_seq(x - 2, y + 2, z * 2)
        if third_tuple not in cache:
            cache[third_tuple] = expensive_seq(x - 3, y + 3, z * 3)

        return  cache[first_tuple] + \
                cache[second_tuple] + \
                cache[third_tuple]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
