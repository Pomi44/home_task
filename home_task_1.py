import multiprocessing
import sys

def calculate_column_sum(args):
    matrix, column = args
    return sum(matrix[row][column] for row in range(len(matrix)))

def main():
    matrix_size_rows = int(input("Введите количество строк матрицы: "))
    matrix_size_cols = int(input("Введите количество столбцов матрицы: "))

    if matrix_size_rows <= 0 or matrix_size_cols <= 0:
        print("Размеры строк и столбцов должны быть положительными.")
        sys.exit(1)

    matrix = []
    for i in range(matrix_size_rows):
        row = []
        for j in range(matrix_size_cols):
            element = int(input(f"Введите элемент a({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)

    num_processes = matrix_size_cols
    pool = multiprocessing.Pool(processes=num_processes)

    column_sums = pool.map(calculate_column_sum, [(matrix, i) for i in range(matrix_size_cols)])
    
    pool.close()
    pool.join()

    total_column_sum = sum(column_sums)  # Итоговая сумма по столбцам

    print("Матрица:")
    for row in matrix:
        print(row)

    print("Суммы по столбцам:", column_sums)
    print("Итоговая сумма элементов матрицы по столбцам:", total_column_sum)

if __name__ == "__main__":
    main()