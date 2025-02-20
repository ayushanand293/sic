import sys

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


numbers = list(map(int,sys.argv[1:]))
bubble_sort(numbers)
print(f'Sorted array is: {numbers}')
