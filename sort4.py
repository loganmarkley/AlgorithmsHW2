#Author : Logan Markley
#Due Date : 12 / 4 / 2023
#Course : CS 2500 (Algorithms)
#Semester : Fall 2023
#Professor : Dr. Morales

def bubbleSort(inputArr: list[int], size: int) -> None:   # I print in the function itself
    numKeyComparisons = 0
    numArraySwaps = 0
    for i in range(size):
        for j in range(size - 1 - i):
            if inputArr[j+1] < inputArr[j]:
                inputArr[j], inputArr[j+1] = inputArr[j+1], inputArr[j]
                numArraySwaps += 1
            numKeyComparisons += 1
    print(f"{numKeyComparisons} {numArraySwaps}")
    return

def selectionSort(inputArr: list[int], size: int) -> None:   # I print in the function itself
    numKeyComparisons = 0
    numArraySwaps = 0
    for i in range(size-1):
        min = i
        for j in range(i+1, size):
            if inputArr[j] < inputArr[min]:
                min = j
            numKeyComparisons += 1
        inputArr[i], inputArr[min] = inputArr[min], inputArr[i]
        numArraySwaps += 1
        
    print(f"{numKeyComparisons} {numArraySwaps}")
    return

def insertionSort(inputArr: list[int], size: int) -> None:   # I print in the function itself
    numKeyComparisons = 0
    numArrayAssignments = 0
    for i in range(1, size):
        v = inputArr[i]
        j = i-1
        while(j >= 0):
            numKeyComparisons += 1
            if(inputArr[j] > v):
                inputArr[j+1] = inputArr[j]
                numArrayAssignments += 1
                j -= 1
            else:
                break
        inputArr[j+1] = v
        numArrayAssignments += 1
        
    print(f"{numKeyComparisons} {numArrayAssignments}")
    return

def mergeSort(inputArr: list[int]) -> int:  # return the number of key comparisons in the iteration
    numKeyComparisons = 0
    if len(inputArr) > 1:
        midIndex = len(inputArr) // 2
        leftSide = inputArr[:midIndex]
        rightSide = inputArr[midIndex:]
        
        numKeyComparisons += mergeSort(leftSide)
        numKeyComparisons += mergeSort(rightSide)
        
        i = j = k = 0
        while i < len(leftSide) and j < len(rightSide):
            numKeyComparisons += 1
            if leftSide[i] <= rightSide[j]:
                inputArr[k] = leftSide[i]
                i += 1
            else:
                inputArr[k] = rightSide[j]
                j += 1
            k += 1
            
        while i < len(leftSide):
            inputArr[k] = leftSide[i]
            i += 1
            k += 1
        
        while j < len(rightSide):
            inputArr[k] = rightSide[j]
            j += 1
            k += 1
            
    return numKeyComparisons



arraySize = int(input())
arr = []
for i in range(arraySize):
    arr.append(int(input()))

bubbleCopy = arr.copy()
selectionCopy = arr.copy()
insertionCopy = arr.copy()
mergeCopy = arr.copy()

bubbleSort(bubbleCopy, arraySize)
selectionSort(selectionCopy, arraySize)
insertionSort(insertionCopy, arraySize)

numComparisons = mergeSort(mergeCopy)
print(numComparisons)