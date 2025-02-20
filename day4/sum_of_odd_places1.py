import sys

def sum_of_odd_places(input_number):
    input_number = int(input_number)
    sum1 = 0
    sum2 = 0
    count = 0
    flag = True
    remainder = 0
    power = 1
    while remainder != input_number :
        temp = ((input_number % (10 ** power)) - remainder) // 10 ** (power - 1)
        if flag :
            sum1 += temp
            flag = not flag
        else:
            sum2 += temp
            flag = not flag
        remainder = (input_number % (10 ** power))     
        power += 1        
    print('The sum of the digits in odd places is: ', end = '') 
    if flag:
        return sum2
    else:
        return sum1           

print(sum_of_odd_places(sys.argv[1]))
