#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 =[] 
    for row in matrix:
        rows =[]
        for i in row:
            i = pow(i, 2)
            rows.append(i)
        matrix2.append(rows)    
    return matrix2