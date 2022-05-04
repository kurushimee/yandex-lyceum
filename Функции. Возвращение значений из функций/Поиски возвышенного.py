def find_mountain(heightsMap):
    maximum = (0, 0)
    for i in range(len(heightsMap)):
        if max(heightsMap[i]) > maximum[0]:
            maximum = (max(heightsMap[i]), i)
    return (maximum[1], heightsMap[maximum[1]].index(maximum[0]))
