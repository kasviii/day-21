def search_2d_matrix(matrix, target):
    if not matrix:
        return False

    # Start from the top-right corner
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            # Move downwards if current element is less than target
            row += 1
        else:
            # Move leftwards if current element is greater than target
            col -= 1

    return False

# Take input for the matrix
print("Enter the elements of the matrix separated by spaces (row-wise):")
matrix = []
for i in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

# Take input for the target value
target = int(input("Enter the target value: "))

# Search for the target value
result = search_2d_matrix(matrix, target)

if result:
    print("True")
else:
    print("False")


