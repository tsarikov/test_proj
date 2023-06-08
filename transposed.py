def transposed(matrix):
    if len(matrix) == 1 and type(matrix[0] != 'list'):
        return matrix
    elif len(matrix) > 1: #and len(matrix[0]) > 1:
        final_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                final_matrix[j][i] = matrix[i][j]
        return final_matrix
    





print(transposed([[1,4],[3,9],[9,8]]))