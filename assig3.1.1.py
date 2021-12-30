''''Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''

def summ():
    '''Taking digits in a given string as separate number'''

    num=input('enter comman separated numbers in a list: ')

    '''converting given string into list of integers'''
    x = [int(a) for a in str(num)]
    print(x)

    sum=0
    '''adding all numbers in a list one by one ufing for loop'''
    for i in x:
        sum=sum+i
    return sum
print(summ())



