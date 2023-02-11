# Uses python3
import numpy as np
import math
def matrix_mult_fast(padded_array, padded_array_2, n):

    if len(padded_array)==1:
        return padded_array*padded_array_2
    # Write your BONUS code here
    A11=matrix_mult_fast(padded_array[0:round(n/2),0:round(n/2)], padded_array_2[0:round(n/2),round(n/2):n]-padded_array_2[n//2:n,n//2:n], n//2)
    A12=matrix_mult_fast(padded_array[0:round(n/2),0:round(n/2)]+padded_array[0:n//2,n//2:n], padded_array_2[n//2:n,round(n/2):n],  n//2)
    A21=matrix_mult_fast(padded_array[n//2:n,0:n//2]+padded_array[n//2:n,n//2:n], padded_array_2[0:round(n/2),0:round(n/2)], n//2)
    A22=matrix_mult_fast(padded_array[n//2:n,n//2:n], padded_array_2[n//2:n,0:n//2]-padded_array_2[0:round(n/2),0:round(n/2)],  n//2)
    B11=matrix_mult_fast(padded_array[0:round(n/2),0:round(n/2)]+padded_array[n//2:n,n//2:n], padded_array_2[0:n//2,0:n//2]+padded_array_2[n//2:n,n//2:n], n//2)
    B12=matrix_mult_fast(padded_array[0:n//2,n//2:n]-padded_array[n//2:n,n//2:n], padded_array_2[n//2:n,0:n//2]+padded_array_2[n//2:n,n//2:n], n//2)
    B21=matrix_mult_fast(padded_array[0:n//2,0:n//2]-padded_array[n//2:n,0:n//2], padded_array_2[0:n//2,0:n//2]+padded_array_2[0:n//2,n//2:n], n//2)
    

    c11 = B11 + A22 - A12 + B12
    c12 = A11 + A12          
    c21 = A21 + A22           
    c22 = A11 + B11 - A21 - B21 

    first_row=np.concatenate((c11,  c21), axis=0)
    second_row=np.concatenate((c12,  c22 ), axis=0)
    output=np.concatenate((first_row,  second_row), axis=1)
    return output

    


def matrix_mult(padded_array, padded_array_2, n):
    if len(padded_array)==1:
        return padded_array*padded_array_2
    A00B00=matrix_mult(padded_array[0:round(n/2),0:round(n/2)], padded_array_2[0:round(n/2),0:round(n/2)], n//2) #
    A10B00=matrix_mult(padded_array[round(n/2):n,0:round(n/2)], padded_array_2[0:round(n/2),0:n//2],  n//2) #
    A00B01=matrix_mult(padded_array[0:n//2,0:n//2], padded_array_2[0:n//2,n//2:n], n//2) #
    A10B01=matrix_mult(padded_array[n//2:n,0:n//2], padded_array_2[0:n//2,n//2:n],  n//2) #
    A01B11=matrix_mult(padded_array[0:n//2,n//2:n], padded_array_2[n//2:n,n//2:n], n//2) #
    A11B11=matrix_mult(padded_array[n//2:n,n//2:n], padded_array_2[n//2:n,n//2:n], n//2) #
    A01B10=matrix_mult(padded_array[0:n//2,n//2:n], padded_array_2[n//2:n,0:n//2], n//2) #
    A11B10=matrix_mult(padded_array[n//2:n,n//2:n], padded_array_2[n//2:n,0:n//2], n//2) #
    
    C11= A00B00+A01B10
    C12= A00B01 + A01B11
    C21=A10B00 + A11B10
    C22=A10B01 + A11B11

    a = np.array(C11)
    b= np.array(C21)
    first_row=np.concatenate((a,  b), axis=0)
    second_row=np.concatenate((C12,  C22), axis=0)
    output=np.concatenate((first_row,  second_row), axis=1)
    #print(first_row,second_row)
    return output
    


      
if __name__ == '__main__':
    n = int(input())
    A = []
    B = []
    # Enter matrix 1 values, press enter after each row
    # Matrix 1 filling
    for i in range(n):
        A.append([int(j) for j in input().split()]) 

    # Enter matrix 2 values, press enter after each row
    # Matrix 2 filling
    for i in range(n):
        B.append([int(j) for j in input().split()]) 

    A = np.array(A)
    B = np.array(B)


    complixity=math.log(n,(2)) 
    if complixity%1!=0:
       power= math.ceil(complixity)
       new_size= 2**power
       shape = np.shape(A)
       padded_array = np.zeros((new_size, new_size))
       padded_array[:shape[0],:shape[1]] = A

       shape_2 = np.shape(B)
       padded_array_2 = np.zeros((new_size, new_size))
       padded_array_2[:shape_2[0],:shape_2[1]] = B
    else:
       padded_array=A
       padded_array_2=B
       new_size=n
       
    print(matrix_mult(padded_array,padded_array_2, new_size))

    ''' UNCOMMENT this line if you will submit BONUS'''
    print(matrix_mult_fast(padded_array, padded_array_2, new_size))
