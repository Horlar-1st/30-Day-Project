# Duplicate Remover: Remove duplicates from a list and print the result.

# Function
def deplicate_remover(lst):
    '''
    Remove duplicates from a list and print the result.

    This function is used to remove duplicates from a list and print the result a list.

    Parameters
    ----------
    args : list
        A list of objects.

    Returns
    -------
    list
        A list of unique objects.

    Examples
    --------
    >>> deplicate_remover([2,4,1,5,2,3,4,2,1,3,3,4,5,1,6,7,4,1])
    [2, 4, 1, 5, 3, 6, 7]

    '''
    try:    
        result = []
        for el in lst:
            if el not in result:
                result.append(el)
        return result if isinstance(lst, list) else str(result) + " **Note: Make sure your entry is a list"
        
        
    except TypeError:
        print("Wrong input!! Make sure it is a list.")


## Example:
print(deplicate_remover([2,4,1,5,2,3,4,2,1,3,3,4,5,1,6,7,4,1]))  # [2, 4, 1, 5, 3, 6, 7]

print(deplicate_remover("3"))       # ['3'] **Note: Make sure your entry is a list
