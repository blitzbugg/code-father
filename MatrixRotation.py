def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[i][j] = matrix[n-j-1][i] 
    
    return rotated
 print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))


 # Expected: [[7,4,1],[8,5,2],[9,6,3]]