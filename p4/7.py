points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}



def calculate_distance(coordinates):
    if len(coordinates) < 2:
        return 0
    dis = 0
    for i in range(len(coordinates) - 1):
        start, finish = sorted([coordinates[i], coordinates[i + 1]])
        dis += points.get((start, finish), 0)
    return dis