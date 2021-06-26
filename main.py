# This Python file uses the following encoding: utf-8


def GoodiesSelection( noOfEmployees = 0):
    f = open("sample_input.txt", "r")
    #neglecting first line
    f.readline()

    goodiesList = dict()

    #reading from file
    for x in f:
        item, price = x.split(":")
        goodiesList[item] = int(price)

    f.close()

    sortedGoodies = list(sorted(goodiesList.items(), key=lambda x: x[1]))
    minDiff = (sortedGoodies[len(sortedGoodies)-1][1] - sortedGoodies[0][1])
    start = 0
    end = 0

    if noOfEmployees > 1:
        for i in range(len(sortedGoodies)-noOfEmployees+1):
            diff = (sortedGoodies[i+ noOfEmployees-1][1] - sortedGoodies[i][1])
            if diff < minDiff:
                minDiff = diff
                end  = i+ noOfEmployees - 1
                start = i

        f = open("sample_output.txt", "w")
        f.write("Here the goodies that are selected for distribution are:\n")


        for item in range(start, end+1):
            f.write(sortedGoodies[item][0]+" : {}\n".format(sortedGoodies[item][1]))

        f.write("And the difference between the chosen goodie with highest price and the lowest price is {}\n".format(minDiff))
        f.close()
    else:
        f = open("sample_output.txt", "w")
        f.write("Should have atleast two employees\n")
        f.close()

GoodiesSelection(2)
