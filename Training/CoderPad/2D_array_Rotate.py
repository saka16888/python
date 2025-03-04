def print_matrix(matrix):
    for row in matrix:
        print(row)

def right_rotate_matrix_90(matrix):
    print("Original Matrix:")
    print_matrix(matrix)
    n = len(matrix)
    m = len(matrix[0])
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            print(i,j)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            #print("swap",i,j)
    print("after swap",matrix)
    # Reverse each row
    for row in matrix:
        row.reverse()
    print("after reverse",matrix)
    return matrix

def left_rotate_matrix_90(matrix):
    print("Original Matrix:")
    print_matrix(matrix)

    n = len(matrix)
    # Transpose the matrix

    # Reverse each row
    for row in matrix:
        row.reverse()
    print("after reverse",matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            #print("swap",i,j)
    print("after swap",matrix)
    return matrix

def up_flip_matrix(matrix):
    print("Original Matrix:")
    print_matrix(matrix)
    n=len(matrix)
    for i in range(n//2) :
        matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
    return matrix

def right_flip_matrix(matrix):
    print("Original Matrix:")
    print_matrix(matrix)
    for row in matrix:
        row.reverse()
    return matrix


def rotate_non_square_matrix_90(matrix):
    print("Original Matrix:")
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with swapped dimensions
    rotated_matrix = [[0] * rows for _ in range(cols)]

    # Fill the new matrix with rotated values
    for r in range(rows):
        for c in range(cols):
            rotated_matrix[c][rows - 1 - r] = matrix[r][c]
    return rotated_matrix

def rotate_matrix_in_place(matrix):
    print("Original Matrix:")
    print_matrix(matrix)
    if not matrix:
        return
    m, n = len(matrix), len(matrix[0])
    # Number of layers to process
    layers = min(m, n) // 2

    for layer in range(layers):
        first = layer
        last_row = m - layer - 1
        last_col = n - layer - 1

        # Rotate layer elements
        for i in range(last_col - first):
            print("i,layer",i,layer)
            # Save top element
            top = matrix[first][first + i]
            # Left -> Top
            matrix[first][first + i] = matrix[last_row - i][first]
            # Bottom -> Left
            matrix[last_row - i][first] = matrix[last_row][last_col - i]
            # Right -> Bottom
            matrix[last_row][last_col - i] = matrix[first + i][last_col]
            # Top -> Right
            matrix[first + i][last_col] = top
    print_matrix(matrix)

# Example usage
matrix = [
    [1, 2, 3, 4, 5],
    [4, 5, 6, 9, 21],
    [7, 8, 9, 10, 22],
    [11, 12, 13, 14,23],
    [15,16,17,18,19]
]

matrix2 = [
    [1, 2, 3, 5, 6],
    [4, 5, 6, 9, 21],
    [7, 8, 9, 10, 22],
    [11, 12, 13, 14,23],
]

print("\nRight rotate")
right_rotate_matrix_90(matrix)

print("\nRight rotate")
right_rotate_matrix_90(matrix2)

print("Left rotate")
left_rotate_matrix_90(matrix)

print("Up flip")
up_flip_matrix(matrix)

print("Right flip")
right_flip_matrix(matrix)

print("\nRight rotate_matrix_in_place")
rotate_matrix_in_place(matrix)

print("\nRight rotate_matrix_in_place")
rotate_matrix_in_place(matrix)

print("\nRight rotate_matrix_in_place")
rotate_matrix_in_place(matrix2)