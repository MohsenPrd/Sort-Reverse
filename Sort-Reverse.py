## Mohsen Pourdehghan

numbers_list=[]

for i in range(5):
    x = int(input('write a number randomly: '))
    numbers_list.append(x)
    
print(f'\nmain list : {numbers_list}')

numbers_list.sort()
print(f'\nsorted list : {numbers_list}')

numbers_list.reverse()
print(f'\nreversed list : {numbers_list}')
