class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_max_min(self):
        flat_matrix = [item for sublist in self.matrix for item in sublist]
        max_value = max(flat_matrix)
        min_value = min(flat_matrix)
        return max_value, min_value

    def transpose_matrix(self):
        transposed_matrix = [
            [self.matrix[j][i] for j in range(len(self.matrix))]
            for i in range(len(self.matrix[0]))
        ]
        return transposed_matrix

    def multiply_matrices(self, matrix2):
        result_matrix = [
            [0 for _ in range(len(matrix2[0]))] for _ in range(len(self.matrix))
        ]

        for i in range(len(self.matrix)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result_matrix[i][j] += self.matrix[i][k] * matrix2[k][j]

        return result_matrix

    def add_matrices(self, matrix2):
        result_matrix = [
            [0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))
        ]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = self.matrix[i][j] + matrix2[i][j]

        return result_matrix


if __name__ == "__main__":
    matrix_a = Matrix([[34, 100, 12], [72, 24, 55], [61, 20, 19]])

    # Menghitung element terbesar dan terkecil
    max_value, min_value = matrix_a.find_max_min()
    print("Elemen terbesar:", max_value)
    print("Elemen terkecil:", min_value)
    print()

    # Transpose matrix
    transposed_matrix = matrix_a.transpose_matrix()
    print("Matrix transpos (T):")
    for row in transposed_matrix:
        print(row)
    print()

    # Menghitung perkalian matrix (A) dan (T)
    matrix_b = Matrix(transposed_matrix)
    multiplied_matrix = matrix_a.multiply_matrices(matrix_b.matrix)
    print("Hasil perkalian matrix (A) dan (T):")
    for row in multiplied_matrix:
        print(row)
    print()

    # Menghitung penjumlahan matrix (T) dan (A)
    added_matrix = matrix_a.add_matrices(matrix_b.matrix)
    print("Hasil penjumlahan matrix (T) dan (A):")
    for row in added_matrix:
        print(row)