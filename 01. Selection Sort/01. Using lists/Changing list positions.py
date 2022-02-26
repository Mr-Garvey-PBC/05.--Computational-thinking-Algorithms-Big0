num = 10

def addOnesToTestList(num):
    testList = []
    for i in range(0, num):
        testList.append(1)
        print(testList)
    return testList

print("O(n): ")
addOnesToTestList(num)
print()

num = 10

def deductOne(num):
    num -= 1
    return num
    
print("O(1): ", "\n", deductOne(num), "\n")

# O(n**2)
testList = [1, 43, 31, 21, 6, 96, 48, 13, 25, 5]

def bubbleSort(testList):
    for i in range(len(testList)):
        for j in range(i+1, len(testList)):
            if testList[j] < testList[i]:
                testList[j], testList[i] = testList[i], testList[j]
            print(testList)

print("O(n**2): ")
bubbleSort(testList)
