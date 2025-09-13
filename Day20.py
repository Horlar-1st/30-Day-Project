# 20 Second Largest: Find the second largest number in a list without using 'sort()'.

# function for sorting a list and selecting the second largest number in the list
def second_largest(lst):
    '''
    To find the second largest number in a list without using 'sort()'.

    This function is used to sort a list and the return the second largest number in a list without using ‘sort()‘.

    Parameters
    ----------
    args : list
        List of numbers

    Returns
    -------
    int/float
        The second largest number

    Examples
    --------
    >>> lst = [7,2,4,12,5,9,1,8]
    >>> second_largest(lst)
    9

    >>> lst2 = [0.8,0,-2,-4,0.12,0.65,-9,1.045,-38]
    >>> second_largest(lst2)
    0.8

    '''
    for j in range(len(lst)-1,1,-1):
        i = 0
        while i < j:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            else:
                lst[i], lst[i+1] = lst[i], lst[i+1]
            i +=1
    return lst[-2]


# examples
print(lst := [7,2,4,12,5,9,1,8])
print(second_largest(lst))                          # Answer 9


print(lst2 := [0.8,0,-2,-4,0.12,0.65,-9,1.045,-38])
print(second_largest(lst2))                          # Answer 0.8
