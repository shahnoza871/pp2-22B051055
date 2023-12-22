import numpy as np
import sympy as sp

class Matrix:
    def __init__(self, mat):
        self.mat = np.array(mat)
        self.rows = len(self.mat)
        self.cols = len(self.mat[0])

    def print_mat(self):
        print(self.mat)

    def minor(self, row, col):
        return Matrix(np.delete(np.delete(self.mat, row, axis=0), col, axis=1))

    def Determinant(self):
        if self.rows != self.cols:
            return "Matrix dimensions must be NxN!"

        if self.rows == 1:
            return self.mat[0, 0]

        det = 0
        for col in range(self.cols):
            x = pow(-1, col) * self.mat[0, col] * self.minor(0, col).Determinant()
            det += x

        return det

    def Eigenvalues(self):
        lmbd = sp.symbols('lambda')
        sym_matrix = sp.Matrix(self.mat)
        
        for i in range(self.rows):
            sym_matrix[i, i] -= lmbd

        numpy_matrix = Matrix(sym_matrix)
        if self.rows != self.cols:
            return "Matrix dimensions must be NxN!"
        det = numpy_matrix.Determinant()
        eigenvalues = sp.solve(det, lmbd)
        return eigenvalues

    def Eigenvectors(self):
        if self.rows != self.cols:
            return "Matrix dimensions must be NxN!"

        lmbd = self.Eigenvalues()
        variables = sp.symbols([f'x{i}' for i in range(self.rows)])
        res = []
        for l in lmbd:
            copied_matrix = self.mat.copy()
            for i in range(self.rows):
                copied_matrix[i][i] -= l
            system_of_equations = []
            for row in copied_matrix:
                equation = sp.Eq(sum(coeff * var for coeff, var in zip(row, variables)), 0)
                system_of_equations.append(equation)
            solution = sp.linsolve(system_of_equations, variables)
            res.append(solution)
        return res

    def transpose(self):
        matrix = self.mat
        transposed = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(matrix[j][i])
            transposed.append(row)
        return transposed

    def Cholesky_Decomposition(self):
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.mat[i][j] != self.mat[j][i]:
                    raise ValueError("Matrix is not symmetric")

        for k in range(self.rows):
            sub_matrix = self.mat[:k+1, :k+1]
            if np.linalg.det(sub_matrix) <= 0:
                raise ValueError("Matrix is not positive definite")

        L = [[0 for x in range(self.rows)] for y in range(self.rows)]
        for i in range(self.rows):
            for j in range(i + 1):
                if i == j:
                    L[i][j] = sp.sqrt(self.mat[i][j] - sum(L[i][k] ** 2 for k in range(j)))
                else:
                    L[i][j] = (1 / L[j][j]) * (self.mat[i][j] - sum(L[i][k] * L[j][k] for k in range(j)))
        return sp.Matrix(L), sp.Matrix(Matrix(L).transpose())


    @staticmethod
    def create_matrix(n, m):
        # n x m = row x column
        print('Enter elements of the matrix.')
        matrix = []
        for i in range(n):
            row = []
            for j in range(m):
                x = int(input(f'Enter element of row {i+1} and column {j+1}: '))
                row.append(x)
            matrix.append(row)
        return matrix

    # row swapping function
    @staticmethod
    def swap(matrix, i, j):
        row = matrix[i].copy()
        matrix[i] = matrix[j]
        matrix[j] = row
        return matrix

    # Since not all pivotal elements are on the main diagonal, we need this function to determine the indeces of the pivotal elements of a matrix
    @staticmethod
    def pivots(matrix):
        row, column = matrix.shape
        rows = []
        columns = []      
        for i in range(0, row):
            for j in range(0, column):
                if matrix[i][j] != 0:
                    rows.append(i)
                    columns.append(j)
                    break
        pivotal_els = []
        for i in range(len(rows)):
            l = []
            l.append(rows[i])
            l.append(columns[i])
            pivotal_els.append(l)
        return pivotal_els

    # generates an identity matrix with specified number of rows and columns
    @staticmethod
    def identity_matrix(row, column):
        shape = (row, column)
        identity = np.empty(shape)
        for i in range(0, row):
            for j in range(0, column):
                if i==j:
                    identity[i][j] = 1
                else:
                    identity[i][j] = 0
        return identity

    def get_matrix(self):
        matrix = ''
        for row in self.mat:
            str_row = ''
            for el in row:
                str_row += f' {el}'
            matrix += str_row+'\n'
        return matrix

    def transpose(self):
        matrix = self.mat
        transposed = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(matrix[j][i])
            transposed.append(row)
        return transposed
        

    def multiply(self, other):
        result = []
        matrix2 = other.transpose()
        for k in range(self.rows):
            row = []
            for i in range(self.rows):
                el = 0
                for j in range(self.cols):
                    el += self.mat[k][j]*matrix2[i][j]
                row.append(el)
            result.append(row)
        matrix = ''
        for row in result:
            str_row = ''
            for el in row:
                str_row += f' {el}'
            matrix += str_row+'\n'
        return matrix


    # Row Echelon Form of a matrix
    def REF(self):
        matrix = np.array(self.mat, float)
        rows, columns = matrix.shape

        column = 0
        for row in range(rows):
            # make all pivots = 1
            if column >=columns:
                break
            r_nonzero_pivot = row
            while r_nonzero_pivot<rows and matrix[r_nonzero_pivot, column] == 0:
                r_nonzero_pivot+=1
            
            if r_nonzero_pivot<rows:
                matrix = Matrix.swap(matrix, r_nonzero_pivot, row)

            if matrix[row][column] != 0:
                matrix[row] = matrix[row]/matrix[row][column]

            # all elements under pivots = 0
            for i in range(row + 1, rows):
                if matrix[row][column] != 0:
                    factor = matrix[i][column] / matrix[row][column]
                else: 
                    factor=0
                matrix[i] = matrix[i] - factor * matrix[row]

            column += 1

        return matrix

    # Reduced Row Echelon Form of a matrix
    def RREF(self):
        matrix = np.array(self.REF())
        row, column = matrix.shape
        
        # This part of a function simply subtracts from [the following row] [the row before multiplied by the factor of elements under a pivot]
        pivotal_els = Matrix.pivots(matrix)
        for i,j in pivotal_els[::-1]:
            for k in range(i)[::-1]:
                factor = matrix[k][j]
                matrix[k] -= factor*matrix[i]

        return matrix
    
    def Inverse(self):
            
        matrix = np.array(self.mat, float)
        rows, columns = matrix.shape

        identity = Matrix.identity_matrix(rows, columns)
        test = identity.copy()

        if rows != columns:
            return 'The matrix is not invetable.'
        elif len(Matrix.pivots(matrix)) < rows:
            return 'The matrix is not invetable.'
        elif self.Determinant() == 0:
            return 'The matrix is not invetable.'

        # REF
        column = 0
        for row in range(rows):
            # make all pivots = 1
            if column >=columns:
                break
            r_nonzero_pivot = row
            while r_nonzero_pivot<rows and matrix[r_nonzero_pivot, column] == 0:
                r_nonzero_pivot+=1
            
            # operation (1) of swapping the rows in case pivotal element is zero
            if r_nonzero_pivot<rows:
                matrix = Matrix.swap(matrix, r_nonzero_pivot, row)
                identity = Matrix.swap(identity, r_nonzero_pivot, row)

            # operation (2) of making pivots = 1
            if matrix[row][column] != 0:
                matrix[row] = matrix[row]/matrix[row][column]
                identity[row] = identity[row]/matrix[row][column]

            # operation (3) of making all elements under pivots = 0
            for i in range(row + 1, rows):
                if matrix[row][column] != 0:
                    factor = matrix[i][column] / matrix[row][column]
                else: 
                    factor=0
                matrix[i] = matrix[i] - factor*matrix[row]
                identity[i] = identity[i] - factor*identity[row]

            column += 1

        # RREF
        # operation (4) of subtraction from [the following row] [the row before multiplied by the factor of elements under a pivot]
        pivotal_els = Matrix.pivots(matrix)
        for i,j in pivotal_els[::-1]:
            for k in range(i)[::-1]:
                factor = matrix[k][j]
                matrix[k] -= factor*matrix[i]
                identity[k] -= factor*identity[i]
        
        return identity
    
    def SLE_solution(self):
        aug_matrix = np.array(self.RREF(), float)
        coef_matrix = np.empty((aug_matrix.shape[0], aug_matrix.shape[1]-1))

        for row in range(coef_matrix.shape[0]):
            for column in range(coef_matrix.shape[1]):
                coef_matrix[row][column] = aug_matrix[row][column]
            
        rows, columns = coef_matrix.shape

        # associate augmented matrix with no zero rows
        for row in range(rows-1, -1, -1): # iterating in reverse order to avid UnboundLocalError
            if np.all(coef_matrix[row]==0):
                aug_matrix = np.delete(aug_matrix, row, axis = 0)
                coef_matrix = np.delete(coef_matrix, row, axis = 0)

        rows, columns = coef_matrix.shape

        # infinitely many solutions
        if columns>rows:
            return 'This SLE has infinitely many solutions.'
        
        solution = []
        for x in range(rows):
            solution.append(aug_matrix[x][aug_matrix.shape[1]-1])
            
            

        return solution


# mat = [
#     [5, 2],
#     [2, 8]
# ]
# matrix = Matrix(mat)
# matrix.print_mat()

# print(matrix.eigenvalue())
# print(matrix.eigenvectors())

# print("\nCholesky Decomposition:")
# Matrix(matrix.Cholesky_Decomposition()).print_mat()
# m1_rows = int(input('Enter the number of rows of the matrix: '))
# m1_columns = int(input('Enter the number of colums of the matrix: '))
# m2_rows = int(input('Enter number of rows of the second matrix: '))
# m2_columns = int(input('Enter number of colums of the second matrix: '))

# matrix1 = Matrix(n = m1_rows, m = m1_columns)
# matrix2 = Matrix(m2_rows, m2_columns)

# print(f'The matrix: \n{matrix1.get_matrix()}')
# print(f'The second matrix: \n{matrix2.get_matrix()}')
# print(f'Result of the multiplication of matrices is: \n{matrix1.multiply(matrix2)}')    

# print(f'Row Echelon Form matrix: \n{matrix1.REF()}')
# print(f'Reduced Row Echelon Form: \n{matrix1.RREF()}')
# print(f'Identity matrix: \n{matrix1.Inverse()}')
# print(f'Solution of SLE: \n{matrix1.SLE_solution()}')

