exampleTuple = 3, 6, 8, 8, 8, 20
exampleList = [4, 5, 6, 7, 7, 5, 9, 11, 12, 14]
stringList = ['Rehan', 'Ajay', 'Brandon', 'Akash', 'Aniket']
# iterating tuple to find 4th element in the tuple
print(exampleTuple[3])

# iterating the list to find the 7th element
print(exampleList[6])

# accesing multiple elements in the list and tuple
print(exampleTuple[1], exampleTuple[4])
print(exampleList[0], exampleList[5])
# slicing from the 5th element to the 10th or the last element(between)
print(exampleList[5:10])

# last element
print(exampleList[-1])

# second last element
print(exampleList[-2])

# finding the index of an value in the list(this is where is the given number in the list)
print(exampleList.index(7))

# sorting the list
exampleList.sort()
print(exampleList)

# sorting string list
stringList.sort()
print(stringList)
