import math
import numpy as np

def skewness(data):
    n = len(data)
    mean_val = np.mean(data)
    variance = np.var(data)
    std_dev = math.sqrt(variance)
    skew_value = sum((x - mean_val) ** 3 for x in data) / (n * std_dev ** 3)
    return skew_value

def linear_regression(x, y):
    if len(x) != len(y):
        return "Error! The number of data points for x and y must be the same."

    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    regression_line = f"y = {slope} * x + {intercept}"
    return f"Slope: {slope}, Intercept: {intercept}\nRegression Line: {regression_line}"

def diagonalize_matrix(matrix):
    matrix = np.array(matrix)
    try:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        diagonal_matrix = np.diag(eigenvalues)
        print(f"Diagonal matrix (Eigenvalues):\n{diagonal_matrix}")
        print(f"Matrix of eigenvectors:\n{eigenvectors}")
    except np.linalg.LinAlgError:
        print("Error! The matrix is not diagonalizable.")

def Super_calculator():
    print("="*45)
    print(" "*12 + "Super Calculator" + " "*12)
    print("="*45)
    print("\nChoose operation:")

    print(" 1. Addition       |  2. Subtraction   |  3. Multiplication |  4. Division")
    print(" 5. Square Root    |  6. Power         |  7. Sin            |  8. Cos")
    print(" 9. Tan            | 10. Logarithm     | 11. Exponential    | 12. Sin Inverse")
    print("13. Cos Inverse    | 14. Tan Inverse   |")
    print("15. Matrix Addition | 16. Matrix Subtraction | 17. Matrix Multiplication")
    print("18. Matrix Power    | 19. Inverse Matrix    | 20. Determinant  | 21. Matrix Rank")
    print("22. Mean            | 23. Median      | 24. Mode          | 25. Standard Deviation | 26. Correlation | 27. Skewness | 28. Linear Regression")
    print("29. Matrix Diagonalization")
    print("="*45)

    while True:
        try:
            choice = int(input("\nEnter choice (1-29) or 0 to exit: ")) 
            
            if choice == 0:
                print("Exiting calculator.")
                break

            if choice == 1: 
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"{x} + {y} = {x + y}")

            elif choice == 2:  
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"{x} - {y} = {x - y}")

            elif choice == 3:  
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"{x} * {y} = {x * y}")

            elif choice == 4:  
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if y == 0:
                    print("Error! Division by zero.")
                else:
                    print(f"{x} / {y} = {x / y}")

            elif choice == 5: 
                x = float(input("Enter number: "))
                if x < 0:
                    print("Error! Negative numbers don't have real square roots.")
                else:
                    print(f"Square root of {x} = {math.sqrt(x)}")

            elif choice == 6: 
                x = float(input("Enter base: "))
                y = float(input("Enter exponent: "))
                print(f"{x} raised to the power of {y} = {math.pow(x, y)}")

            elif choice == 7: 
                x = float(input("Enter angle in degrees: "))
                print(f"Sin({x}) = {math.sin(math.radians(x))}")

            elif choice == 8: 
                x = float(input("Enter angle in degrees: "))
                print(f"Cos({x}) = {math.cos(math.radians(x))}")

            elif choice == 9: 
                x = float(input("Enter angle in degrees: "))
                print(f"Tan({x}) = {math.tan(math.radians(x))}")

            elif choice == 10: 
                x = float(input("Enter number: "))
                if x <= 0:
                    print("Error! Logarithm undefined for non-positive values.")
                else:
                    print(f"Log({x}) = {math.log10(x)}")

            elif choice == 11:  
                x = float(input("Enter number: "))
                print(f"Exponential of {x} = {math.exp(x)}")

            elif choice == 12:  
                x = float(input("Enter value for sin inverse (between -1 and 1): "))
                if x < -1 or x > 1:
                    print("Error! Value must be between -1 and 1.")
                else:
                    result = math.degrees(math.asin(x))
                    print(f"Sin inverse({x}) = {result} degrees")

            elif choice == 13:  
                x = float(input("Enter value for cos inverse (between -1 and 1): "))
                if x < -1 or x > 1:
                    print("Error! Value must be between -1 and 1.")
                else:
                    result = math.degrees(math.acos(x))
                    print(f"Cos inverse({x}) = {result} degrees")

            elif choice == 14:  
                x = float(input("Enter value for tan inverse: "))
                result = math.degrees(math.atan(x))
                print(f"Tan inverse({x}) = {result} degrees")

            elif choice == 15:  
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                print("Enter elements of first matrix:")
                matrix1 = [list(map(float, input(f"Row {i + 1}: ").split())) for i in range(rows)]
                print("Enter elements of second matrix:")
                matrix2 = [list(map(float, input(f"Row {i + 1}: ").split())) for i in range(rows)]
                matrix1 = np.array(matrix1)
                matrix2 = np.array(matrix2)

                if matrix1.shape != matrix2.shape:
                    print("Error! Matrices must have the same dimensions.")
                else:
                    result = np.add(matrix1, matrix2)
                    print(f"Result of addition:\n{result}")

            elif choice == 16:  
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                print("Enter elements of first matrix:")
                matrix1 = [list(map(float, input(f"Row {i + 1}: ").split())) for i in range(rows)]
                print("Enter elements of second matrix:")
                matrix2 = [list(map(float, input(f"Row {i + 1}: ").split())) for i in range(rows)]
                matrix1 = np.array(matrix1)
                matrix2 = np.array(matrix2)

                if matrix1.shape != matrix2.shape:
                    print("Error! Matrices must have the same dimensions.")
                else:
                    result = np.subtract(matrix1, matrix2)
                    print(f"Result of subtraction:\n{result}")

            elif choice == 17:  
                rows1 = int(input("Enter number of rows for first matrix: "))
                cols1 = int(input("Enter number of columns for first matrix: "))
                print("Enter elements of first matrix:")
                matrix1 = [list(map(float, input(f"Row {i + 1}: ").split())) for i in range(rows1)]
                
                rows2 = int(input("Enter number of rows for second matrix: "))
                cols2 = int(input("Enter number of columns for second matrix: "))
                print("Enter elements of second matrix:")
                matrix2 = [list(map(float, input(f"Row {i + 1}: ").split())) for i in range(rows2)] 

                matrix1 = np.array(matrix1)
                matrix2 = np.array(matrix2)

                if cols1 != rows2:
                    print("Error! Number of columns of the first matrix must equal the number of rows of the second matrix.")
                else:
                    result = np.dot(matrix1, matrix2)
                    print(f"Result of multiplication:\n{result}")

            elif choice == 18:  
                matrix_size = int(input("Enter the size of the matrix (n for n x n matrix): "))
                matrix = []
                print(f"Enter the elements of {matrix_size}x{matrix_size} matrix row by row:")
                for i in range(matrix_size):
                    row = list(map(float, input(f"Row {i + 1}: ").split()))
                    matrix.append(row)
                matrix = np.array(matrix)
                power = int(input("Enter the power to raise the matrix to: "))
                
                if power < 0:
                    print("Error! Power must be a non-negative integer.")
                else:
                    result = np.linalg.matrix_power(matrix, power)
                    print(f"Matrix raised to power {power}:\n{result}")

            elif choice == 19:  
                matrix_size = int(input("Enter the size of the matrix (n for n x n matrix): "))
                matrix = []
                print(f"Enter the elements of {matrix_size}x{matrix_size} matrix row by row:")
                for i in range(matrix_size):
                    row = list(map(float, input(f"Row {i + 1}: ").split()))
                    matrix.append(row)
                matrix = np.array(matrix)
                try:
                    matrix_inv = np.linalg.inv(matrix)
                    print(f"Inverse of the matrix:\n{matrix_inv}")
                except np.linalg.LinAlgError:
                    print("Error! The matrix is singular and cannot be inverted.")

            elif choice == 20:  
                matrix_size = int(input("Enter the size of the matrix (n for n x n matrix): "))
                matrix = []
                print(f"Enter the elements of {matrix_size}x{matrix_size} matrix row by row:")
                for i in range(matrix_size):
                    row = list(map(float, input(f"Row {i + 1}: ").split()))
                    matrix.append(row)
                matrix = np.array(matrix)
                try:
                    det = np.linalg.det(matrix)
                    print(f"Determinant of the matrix: {det}")
                except np.linalg.LinAlgError:
                    print("Error! Invalid matrix for determinant calculation.")
            
            elif choice == 21: 
                matrix_size = int(input("Enter the size of the matrix (n for n x n matrix): "))
                matrix = []
                print(f"Enter the elements of {matrix_size}x{matrix_size} matrix row by row:")
                for i in range(matrix_size):
                    row = list(map(float, input(f"Row {i + 1}: ").split()))
                    matrix.append(row)
                matrix = np.array(matrix)
                rank = np.linalg.matrix_rank(matrix)
                print(f"Rank of the matrix: {rank}")

            elif choice == 22: 
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                mean_value = np.mean(numbers)
                print(f"Mean of the numbers: {mean_value}")

            elif choice == 23:  
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                median_value = np.median(numbers)
                print(f"Median of the numbers: {median_value}")

            elif choice == 24:  
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                mode_value = np.argmax(np.bincount(np.array(numbers, dtype=int)))
                print(f"Mode of the numbers: {mode_value}")

            elif choice == 25: 
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                std_deviation = np.std(numbers)
                print(f"Standard Deviation of the numbers: {std_deviation}")

            elif choice == 26:  
                numbers1 = list(map(float, input("Enter first set of numbers separated by space: ").split()))
                numbers2 = list(map(float, input("Enter second set of numbers separated by space: ").split()))
                correlation_matrix = np.corrcoef(numbers1, numbers2)
                correlation = correlation_matrix[0, 1]
                print(f"Correlation coefficient between the two sets: {correlation}")

            elif choice == 27:
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                skew_value = skewness(numbers)
                print(f"Skewness of the numbers: {skew_value}")

            elif choice == 28:  
                x = list(map(float, input("Enter x values separated by space: ").split()))
                y = list(map(float, input("Enter y values separated by space: ").split()))
                regression_result = linear_regression(x, y)
                print(regression_result)

            elif choice == 29:  
                matrix_size = int(input("Enter the size of the matrix (n for n x n matrix): "))
                matrix = []
                print(f"Enter the elements of {matrix_size}x{matrix_size} matrix row by row:")
                for i in range(matrix_size):
                    row = list(map(float, input(f"Row {i + 1}: ").split()))
                    matrix.append(row)
                diagonalize_matrix(matrix)

            else:
                print("Invalid input. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

Super_calculator()