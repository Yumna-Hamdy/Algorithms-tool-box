# Uses python3
import sys
def merge(a, b, left,ave, right):
    #the first subarray pointer
    i=left
    #the second subarray pointer
    j=ave
    k=left
    newi=left
    #inversion counter
    number_of_inversions = 0
    
    while (i<(ave) and j<right):
        #check if the first subarray item is smaller than the second subarray item
        if a[i]<=a[j]:
            #if yes put the first subarray item in the new array
            b[k]=a[i]
            #increase the pointer index of the first subarray
            i+=1
            #increase the pointer index of the new array
            k+=1
        else:
            #if not put the second subarray item in the new array
            b[k]=a[j]
            #increase the pointer index of the second subarray
            j+=1
            #increase the pointer index of the new array
            k+=1
            #increase the inversions counter
            number_of_inversions +=(ave-i)
            #if there is any items remaining in the first fubarray copy them at the end of the new array
    while i<(ave):
         b[k]=a[i]
         i+=1
         k+=1
         #if there is any items remaining in the second fubarray copy them at the end of the new array
    while j<right:
        b[k]=a[j]
        j+=1
        k+=1
    
    #copying all the sorted elements in a new array
    while newi<right:
        a[newi]=b[newi]
        newi+=1
    
    return number_of_inversions


def get_number_of_inversions(a, b, left, right):
    #write your code here
    
    ## Helpful pseudocode
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions+=merge(a, b, left,ave, right)
    return number_of_inversions

if __name__ == '__main__':
    # DO NOT change this code
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
