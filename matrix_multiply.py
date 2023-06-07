# Matrix multiply
def is_matrix(matrix):
    pass

def possibility(matrix_A, matrix_B):
    return len(matrix_A[0]) == len(matrix_B) and True
    


def multiply_matrix(matrix_A: list, matrix_B: list) -> list:
    if is_matrix(matrix_A) and is_matrix(matrix_B) and possibility(matrix_A, matrix_B):
        matr_A_lines = len(matrix_A)
        matr_b_lines = len(matrix_B)
        matr_A_rows = len(matrix_A[0])
        matr_B_rows = len(matrix_B[0])
        for line in range(matr_A_lines):
            for row in range(matr_B_rows):
    pass 

m1 = [[1,3],[2,8]]
m2 = [[1,5,9],[3,8,6]]

possibility(m1,m2)