l1 = [5,9,3,2,1]
l2 = [5,14,17,19,20]

def sortList(l):        # Bubble Sort
    n = len(l)
    for i in range(n):      # Traverse through all array elements
        for j in range(0, n-i-1):   # Last i elements are already in place
            if l[j] > l[j+1]:           # Traverse the array from 0 to n-i-1
                l[j], l[j+1] = l[j+1], l[j]     # Swap if the element found is greater than the next element
    return l

l3 = sortList(l1)
print(l3)
l4 = sortList(l2)
print(l4)