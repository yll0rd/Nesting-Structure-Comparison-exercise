def islist(n): return isinstance(n, list)

def same_structure_as(arr1, arr2): 
    if not islist(arr1) or not islist(arr2): return False
    if len(arr1) != len(arr2): return False
    for i in range(len(arr1)):
        if islist(arr1[i]) != islist(arr2[i]): return False
        if islist(arr1[i]) and islist(arr2[i]): return same_structure_as(arr1[i], arr2[i])
    return True
                
print(same_structure_as([ 1, [ 1, 1 ] ], [2, [ 2, 3,4]]))
