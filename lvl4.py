def divide_and_multiply(x: int, y: int) -> int:
    """Return the product of integer division of x by 3 and y."""
    return (x // 3) * y

def process_pairs_from_file(filename: str):
    """Process pairs of integers from a file and create matrices."""
    matrices = []
    with open(filename, 'r') as file:
        num_pairs = int(file.readline().strip())
        for _ in range(num_pairs):
            x, y, _ = map(int, file.readline().strip().split())
            matrix = [['.' for _ in range(x)] for _ in range(y)]
            for col in range(0, x, 2):
                for row in range(0, y - 2, 4):
                    matrix[row][col:col + 3] = ['X'] * 3
            if all(cell == '.' for cell in matrix[-2]):
                for i in range(0, x - 2, 4):
                    if matrix[-1][i:i + 3] == ['.'] * 3:
                        matrix[-1][i:i + 3] = ['X'] * 3
            matrices.append(matrix)
    return matrices

def write_matrices_to_file(matrices, filename: str):
    """Write matrices to a specified output file."""
    with open(filename, 'w') as outfile:
        for matrix in matrices:
            outfile.write("\n".join("".join(row) for row in matrix) + "\n\n")

if __name__ == "__main__":
    input_filename = 'level4_1.in'
    output_filename = 'output.txt'
    output_results = process_pairs_from_file(input_filename)
    write_matrices_to_file(output_results, output_filename)
