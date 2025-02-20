import sys
def string_insertion_sort(input_string):
    arr = list(input_string.upper())
    for i in range(1, len(input_string)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    print('Sorted string is: ', end = '')    

    return "".join(arr)

print(string_insertion_sort(sys.argv[1]))