#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    # bubble sorting
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if(a[i] > a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    for i in range(0,len(b)):
        for j in range(0,len(b)):
            if(b[i] > b[j]):
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
#   the dot product
    for i in range(0,len(a)):
        res+=a[i]*b[i]
    return res
#    the complixity is n^2
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
