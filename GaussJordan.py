from matriz import *

def multiply_i_rows_by(A, B, i, q) :
    A.multiply_i_row_by(i, q)
    B.multiply_i_row_by(i, q)

def imprime(A, B) :
	A.imprime()
	print()
	B.imprime()

def gauss_jordan(A, B) :
    if A.rows() != B.rows() or A.rows() != A.columns() :
        print("Matriz inválida")
        return 0
    
    for i in range (0, A.columns()) :
        k = A.at(i)
        if k != 1 :
            if k == 0 : #Si elemento A[i][i] es igual a 0
                for j in range (i+1, A.rows()) :
                    if A.at_(j, i) != 0 : #Encontrar A[i][i] != 0
                        A.exchange_rows(i, j)
                        B.exchange_rows(i, j)
                        k = A.at(i)
                if k == 0 :
                    print("Muchas soluciones")
                    imprime(A, B)
                    return
            q = 1.0 / k
            multiply_i_rows_by(A, B, i, q)

        for j in range (i+1, A.rows()) :
            t = A.at_(j,i)
            if A.at_(j,i) != 0 :
                r = -1.0 * t
                A.add_i_to_j(i, j, r)
                B.add_i_to_j(i, j, r)

    for i in range (A.columns() - 1, -1, -1) :
        if A.at(i) == 0 :
            print("Muchas soluciones")
            imprime(A, B)
            return
        for j in range (i - 1, -1, -1) :
            t = A.at_(j,i)
            if A.at_(j,i) != 0 :
                r = -1.0 * t
                A.add_i_to_j(i, j, r)
                B.add_i_to_j(i, j, r)

    imprime(A, B)
