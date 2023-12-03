# Создайте класс Матрица. Добавьте методы для:
# а. вывода на печать,
# б. сравнения,
# в. сложения,
# г. *умножения матриц

from UserException import MatrixError, SizeMatrixError, СompatibilityMatrixError, ElementsMatrixError

class Matrix():
    '''Операции с матрицами: печать, транспонирование, сравнение, сложение, умножение'''


    def __init__(self, matrix: list[list] | tuple[tuple]) -> None:
        len_ = len(matrix[0])
        check = True
        for i in matrix:
            if len(i) != len_:
                check = False
        if check == True:
            self.matrix = matrix
        else:
            raise MatrixError()


    def print_matrix(self):
        '''Печать матрицы'''
        for i in self.matrix: 
            print(i)


    def matrix_transposition(self) -> list[list]:
        '''Транспонирование матрицы'''
        lines = len(self.matrix)
        columns = len(self.matrix[0])
        result = []
        for i in range(columns):
            result.append([])
            for _ in range(lines):
                result[i].append(0)
        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[0])): 
                result[j][i] = self.matrix[i][j] 
        matr_tr = Matrix(result)
        return matr_tr
    

    def __eq__(self, other):
        '''Сравнение матриц'''
        result = True
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            result = False
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        result = False 
        return result
    

    def __add__(self, other):
        '''Сложение матриц: матрицы должны быть одного размера'''
        lines = len(self.matrix)
        columns = len(self.matrix[0])
        if lines != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise SizeMatrixError()
        else:
            result = []
            for i in range(lines):
                result.append([])
                for _ in range(columns):
                    result[i].append(0)
            for i in range(lines):
                for j in range(len(self.matrix[i])):
                    try:
                        result[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    except:
                        raise ElementsMatrixError()
        matr_sum = Matrix(result)
        return matr_sum
    

    def __mul__(self, other):
        '''Умножение матриц: матрицы должны быть совместимы(число столбцов первой матрицы длжно быть равно числу строк второй матрицы)'''
        lines1 = len(self.matrix)
        columns1 = len(self.matrix[0])
        lines2 = len(other.matrix)
        columns2 = len(other.matrix[0]) 
        if columns1 != lines2:
            raise СompatibilityMatrixError() 
        else:      
            result = []
            for i in range(lines1):
                    result.append([])
                    for _ in range(columns2):
                        result[i].append(0)        
            for i in range(lines1):
                for j in range(columns2):
                    sum = 0
                    for n in range(columns1):
                        try:
                            sum += self.matrix[i][n]*other.matrix[n][j]
                        except:
                            raise ElementsMatrixError()
                    result[i][j] = sum
        matr_mul = Matrix(result)
        return matr_mul
    

    def __str__(self):
        return f'{self.matrix}'
    

if __name__ == '__main__':
    matrix1 = ((1, 2, 3, 4),
               (4, 5, 5, 7),
               (7, 8, 9, 5),
               (1, 2, 3, 8))
    matrix2 = ((1, 2, 3, 5),
               (4, 5, 6, 6),
               (7, 8, 9, 7),
               (1, 2, 3, 8))
    matr1 = Matrix(matrix1)
    matr2 = Matrix(matrix2)
    matr1.print_matrix()
    print()
    matr1.matrix_transposition().print_matrix()
    print(matr1==matr2)
    (matr1+matr2).print_matrix()
    print()
    (matr1*matr2).print_matrix()



