# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_fast(n, m):

    # setting the first and second f
    counter=2
    previous = 0
    current  = 1
    rem=[0,1]
    i=2
    while (rem[i-2]!=0 or rem[i-1]!=1) or (i==2) :
        previous, current = current, previous + current
    #getting the modulus
        
        rem.append(current % m)
        counter=counter+1
        i=i+1
    return rem[n%(counter-2)]

    
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
