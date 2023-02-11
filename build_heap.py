# python3

def heap(arr,n,i,swaps):

   # Builidng min heap
    smallest = i  
    l = 2 * i + 1     
    r = 2 * i + 2    
    #if   the root is bigger than the left child 
    if l < n and arr[l] < arr[smallest]: 
        smallest = l  
    #if   the root is bigger than the right child 
    if r < n and arr[r] < arr[smallest]: 
        smallest = r  
    if smallest != i:  
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        swaps.append([i,smallest])   #swap
        heap(arr, n, smallest,swaps)          


    return swaps
 



def build_heap(arr):

    swaps = []  # Creating Empty swaps array to send it by refernce to heapify
    n = len(arr)
    for i in range(n-1,-1,-1):
        heap(arr, n, i,swaps)  
 
    return swaps


def main():
    #####   DO NOT CHANGE THE CODE IN THIS PART #########
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
