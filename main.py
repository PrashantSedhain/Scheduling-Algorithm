file = open("file.txt", "r")

line = file.readline()
splicedInput = line.split()
pageFaults = 0
pageFaultsLRU = 0
lruCounter = 1
inputForLRU = arrayOfInput = [[0, 0, 0], [0, 0, 0]]
arrayOfInput = [0, 0, 0]
arrayOfInput2 = [0, 0, 0]
i = 0
print("Answers for FIFO scheduling: ")
for item in splicedInput:
    if item in arrayOfInput:
        # leave the array as it is and print
        output = ""

        for element in arrayOfInput:
            output = output + element + " "
        print(output)

    elif i > 2:
        first = arrayOfInput[0]
        second = arrayOfInput[1]
        third = arrayOfInput[2]
        arrayOfInput[0] = second
        arrayOfInput[1] = third
        arrayOfInput[2] = item

        pageFaults += 1
        output = ""
        for element in arrayOfInput:
            output = output + element + " "
        print(output)

    else:
        arrayOfInput[i] = item
        output = ""
        for element in arrayOfInput:
            output = output + str(element) + " "
        print(output)
        i = i + 1
        pageFaults = pageFaults + 1

print(("Pagefaults for FIFO = " + str(pageFaults)))

i = 2


# ----------------------------------------------------------------------------------------#
def findIndexOfItem(inputArray, val):
    for k in range(0, 3):
        if val == inputArray[k]:
            return k


print("Answers for LRU scheduling: ")

for item in splicedInput:
    if item in arrayOfInput2:
        output = ""
        for element in arrayOfInput2:
            index = findIndexOfItem(arrayOfInput2, item)
            # print("Index is " + str(index))
            if index == 1:
                a = arrayOfInput2[0]
                b = arrayOfInput2[1]
                arrayOfInput2[1] = a
                arrayOfInput2[0] = b

            if index == 2:
                a = arrayOfInput2[0]
                b = arrayOfInput2[1]
                c = arrayOfInput2[2]
                arrayOfInput2[0] = c
                arrayOfInput2[1] = a
                arrayOfInput2[2] = b
        for value in arrayOfInput2:
            output = output + value + " "
        print(output)

    elif i < 0:
        first = arrayOfInput2[0]
        second = arrayOfInput2[1]
        third = arrayOfInput2[2]
        arrayOfInput2[2] = second
        arrayOfInput2[1] = first
        arrayOfInput2[0] = item

        pageFaultsLRU = pageFaultsLRU + 1
        output = ""
        for element in arrayOfInput2:
            output = output + element + " "
        print(output)

    else:
        pageFaultsLRU = pageFaultsLRU + 1
        arrayOfInput2[i] = item
        output = ""
        for element in arrayOfInput2:
            output = output + str(element) + " "
        print(output)
        i = i - 1

print(("Pagefaults for LRU = " + str(pageFaultsLRU)))
