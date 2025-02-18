def next_biggest_number(n):
    list_n=list(n)
    swap=False
    i = 0
    for i in range(len(list_n)-1,0,-1):
        if list_n[i] > list_n[i-1]:
            temp=list_n[i]
            list_n[i]=list_n[i-1]
            list_n[i-1]=temp
            swap=True
            break       
    if swap == True:
        final_n = list_n[:i] + sorted(list_n[i:])
        return int(''.join(final_n))
    else:
        return None
input_number = input('Enter the number: ')
print(next_biggest_number(input_number))

