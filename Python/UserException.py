class UserException(Exception):
    pass

        
class MatrixError(UserException):
    def __str__(self) -> str:
        return 'Аргумент не является матрицей. В матрице все строки должны быть одного размера'
    
class SizeMatrixError(UserException):
    def __str__(self) -> str:
        return 'Матрицы разного размера, сложение не возможно'
    
class СompatibilityMatrixError(UserException):
    def __str__(self) -> str:
        return 'Матрицы не совместимы, перемножение не возможно(число столбцов первой матрицы длжно быть равно числу строк второй матрицы)'
    
class ElementsMatrixError(UserException):
    def __str__(self) -> str:
        return 'Матрица содержит не числовые элементы'
    
