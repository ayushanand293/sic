def binarySearch(array, search_element):
    high = len(array) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == search_element:
            return mid
        elif array[mid] < search_element:
            low = mid + 1
        else: 
            high = mid - 1    
    return None        