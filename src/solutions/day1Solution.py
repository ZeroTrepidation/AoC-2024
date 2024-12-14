def solution():

    print("Welcome to my Advent of Code Program")

    filepath = "../resources/inputs/day1_input.txt"

    lines = open(filepath)

    array1 = []
    array2 = []

    for line in lines:
        row = line.split()

        array1.append(row[0])
        array2.append(row[1])

    array1.sort()
    array2.sort()

    totalDistance = 0

    for i in range(len(array1)):
        totalDistance += abs(int(array1[i]) - int(array2[i]))

    return totalDistance
