def sum_list(A, B) :
    for i in range (1, len(A)) :
        A[i] = A[i] + B[i]
    print(A)
    return A

def multiply_by(A, k) :
    size = len(A)
    for i in range (1, size+1) :
        A[i-1] = A[i-1] * k
    return A


def gauss_jordan(A) :
    size = len(A)
    for i in range (1, size+1) :
        if A[i-1][i-1] != 1 :
            A[i-1] = multiply_by(A[i-1], 1.0/A[i-1][i-1])
        for j in range (i, size) :
            if A[j][i-1] != 0 :
                print(A[0])
                temp0 = multiply_by(A[0], -1.0*A[j][i-1]/A[0][i-1])
                print("Mult: ", temp0)
                print("antes: ", A[j])
                print(sum_list(A[j], temp0))
                print("desp: ", A[j])
                #A[j-1] = A[j-1] - multiply_by(A[i-1], A[
    return A
