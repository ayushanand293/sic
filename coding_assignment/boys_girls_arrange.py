def boys_girls_arrange(boys_list, girls_list):
    girls_list.sort()
    boys_list.sort()
    final_list = [0]
    i = 0
    flag = 0 if min(boys_list[0], girls_list[0]) is boys_list[0] else 1
    for i in range(len(boys_list)):
        if min(boys_list[i], girls_list[i]) == boys_list[i]:
            if flag == 0 and final_list[-1] <= boys_list[i] or girls_list[i] == boys_list[i]:
                final_list.extend([boys_list[i], girls_list[i]])
                
            else:
                break    
        else:
            if flag == 1 and final_list[-1] <= girls_list[i] or girls_list[i] == boys_list[i]:
                final_list.extend([girls_list[i], boys_list[i]])
                
            else:
                break    
    if len(final_list) == (2 * len(boys_list)) + 1:
        return 'YES'
    else:
        return 'NO'    

result_list = []
test_cases = int(input('Enter the number of test cases: '))
for test in range(test_cases):
    print(f'Test Case {test + 1}: ')
    print('Make sure the number of boys and girls are the same')
    boys = input('Enter the boys heights: ').split()
    girls = input('Enter the girls heights: ').split()
    boys_list = list(map(int, boys))
    girls_list = list(map(int, girls))
    result_list.append(boys_girls_arrange(boys_list, girls_list))
for i in range(len(result_list)):
    print(f'Test Case {i + 1}: {result_list[i]}')


