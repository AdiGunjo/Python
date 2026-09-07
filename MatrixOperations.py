def input_matrix(rows, cols, name):
    print(f"Enter elements for matrix {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def display_matrix(matrix, name):
    print(f"\nMatrix {name}:")
    for row in matrix:
        print(row)


def add_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    result = [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]
    return result


def subtract_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    result = [[m1[i][j] - m2[i][j] for j in range(cols)] for i in range(rows)]
    return result


def multiply_matrices(m1, m2):
    rows1 = len(m1)
    cols1 = len(m1[0])
    cols2 = len(m2[0])
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    return result


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = input_matrix(rows, cols, "A")
    matrix_b = input_matrix(rows, cols, "B")

    display_matrix(matrix_a, "A")
    display_matrix(matrix_b, "B")

    display_matrix(add_matrices(matrix_a, matrix_b), "A + B")
    display_matrix(subtract_matrices(matrix_a, matrix_b), "A - B")

    if cols == rows:
        display_matrix(multiply_matrices(matrix_a, matrix_b), "A x B")
    else:
        print("\nMultiplication skipped: columns of A must equal rows of B")

    display_matrix(transpose_matrix(matrix_a), "Transpose of A")


if __name__ == "__main__":
    main()