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
        while(j >= 0 and inputArr[j] > v):
            numKeyComparisons += 1
            numArrayAssignments += 1
            inputArr[j+1] = inputArr[j]
            j -= 1
        inputArr[j+1] = v
        numArrayAssignments += 1
        
    print(f"{numKeyComparisons} {numArrayAssignments}")
    return

def mergeSort(inputArr: list[int], size: int) -> None:   # I print in the function itself
    numKeyComparisons = 0
    
    print(numKeyComparisons)
    return



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
mergeSort(mergeCopy, arraySize)