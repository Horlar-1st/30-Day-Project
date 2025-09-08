# List Summer: Create a list of numbers and return their total sum.

def list_summer(*args):
    '''
    Create a list of numbers and return their total sum.

    This function is used create a list of numbers and return their total sum.

    Parameters
    ----------
    args : int
        A array of numbers.

    Returns
    -------
    int
        The sum of the list created.

    Examples
    --------
    >>> list_summer(1,2,3,4,5,6,8,9,10,7)
    55

    >>> list_summer(1345,34321,213347,78726)
    327739
    '''
    lst=[]
    for i in args:
        lst.append(i)
    
    total=0
    for i in lst:
        total+=i
    return total

# Example usage:
print(list_summer(1,2,3,4,5,6,8,9,10,7))

print(list_summer(1345,34321,213347,78726))
