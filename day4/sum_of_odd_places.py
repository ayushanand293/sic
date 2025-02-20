import sys

def sum_of_odd_places(input_number):
    sum = 0
    input_string = str(input_number)
    for i in range(0, len(input_string),2):
        sum += int(input_string[i])
    
    print('Sum of all the digits in odd places is: ', end ='')
    return sum   

print(sum_of_odd_places(sys.argv[1]))     