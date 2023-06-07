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
    # if is_matrix(matrix_A) and is_matrix(matrix_B) and possibility(matrix_A, matrix_B):
    if possibility(matrix_A, matrix_B):
        matr_A_lines = len(matrix_A)
        matr_B_lines = len(matrix_B)
        matr_A_rows = len(matrix_A[0])
        matr_B_rows = len(matrix_B[0])
        sum = 0
        for i in range(matr_A_rows):
            for j in range(matr_A_lines):
                

        # for line in range(matr_A_lines):
        #     for row in range(matr_B_rows):
    pass 

m1 = [[1,3],[2,8]]
m2 = [[1,5,9],[3,8,6]]
m3 = [1,2]

print(possibility(m1,m2))
print(is_matrix(m3))