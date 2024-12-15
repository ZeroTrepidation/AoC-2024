def solution():
    print("Total Distance: {}, Similarity Score {}".format(solutionPart1(), solutionPart2()))


def solutionPart1():
    filepath = "../resources/inputs/day1_input.txt"

    array1 = []
    array2 = []

    with open(filepath) as file:

        for line in file:
            row = line.split()

            array1.append(row[0])
            array2.append(row[1])

    array1.sort()
    array2.sort()

    totalDistance = 0

    for i in range(len(array1)):
        totalDistance += abs(int(array1[i]) - int(array2[i]))

    return totalDistance


def solutionPart2():
    filepath = "../resources/inputs/day1_input.txt"

    leftNumbers = []
    rightDict = {}

    with open(filepath) as file:

        for line in file:
            row = line.split()
            r = row[1]

            leftNumbers.append(row[0])
            if rightDict.keys().__contains__(r):
                rightDict[r] = rightDict[r] + 1
            else:
                rightDict[r] = 1

    similarityScore = 0

    for i in range(len(leftNumbers)):
        search = leftNumbers[i]
        if rightDict.keys().__contains__(search):
            freq = rightDict[search]

            similarityScore += int(search) * int(freq)

    return similarityScore
