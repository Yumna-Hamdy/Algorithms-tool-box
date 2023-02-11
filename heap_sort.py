#python3
import sys
import random


def heapify(arr,n,i):

    # Building max heap

    biggest = i  
    l = 2 * i + 1     
    r = 2 * i + 2   
    #if   the root is smaller than the left child 
    if l < n and arr[biggest] < arr[l]: 
        biggest = l   
    #if   the root is smaller than the right child  
    if r < n and arr[biggest] < arr[r]: 
        biggest = r  
    if biggest != i:  
        arr[i], arr[biggest] = arr[biggest], arr[i]  # swap
        heapify(arr, n, biggest) 
 

def heap_sort(arr):
    n = len(arr) 
    
    for i in range(n//2 - 1,  -1): # Building the heap itself
        heapify(arr, n, i)
 
    
    for i in range(n-1, 0, -1):  #Sorting the heap 
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)





### DO NOT CHANGE INPUT/OUTPUT FORMAT ####

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    heap_sort(a)
    for x in a:
        print(x, end=' ')

