# Matrix multiply
def is_matrix(matrix):
    lines = len(matrix)
    if lines > 1 and type(matrix[0]) == 'list':
        rows = len(matrix[0])
        answer = True
        for line in matrix:
            if len(line) != rows:
                answer = False
        return answer
    elif lines == 1:
        return True
    else:
        return False      

def possibility(matrix_A, matrix_B):
    return len(matrix_A[0]) == len(matrix_B) and True # проверяем равно ли количество столбцов 1-матрицы и кол-во строк во второй

def multiply_matrix(matrix_A: list, matrix_B: list) -> list:
    matr_A_lines = len(matrix_A)
    matr_B_lines = len(matrix_B)
    matr_A_rows = len(matrix_A[0])
    matr_B_rows = len(matrix_B[0])
    result = [[0 for x in range(matr_B_rows)] for y in range(matr_A_lines)]
    
    # if is_matrix(matrix_A) and is_matrix(matrix_B) and possibility(matrix_A, matrix_B):
    if possibility(matrix_A, matrix_B):
        for i in range(matr_A_rows):
            for j in range(matr_B_lines):
                for k in range(matr_B_rows):
                    result[i][k] += matrix_A[i][j] * matrix_B[j][k]

        # for line in range(matr_A_lines):
        #     for row in range(matr_B_rows):
    return result 

m1 = [[1,2],[0,1]]
m2 = [[2,5,1],[6,7,1]]
m3 = [1,2]

print(possibility(m1,m2))
print(is_matrix(m3))
print(multiply_matrix(m1,m2))