""""class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Matrix must be 3x3.")
        self.data = data

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def add(self, other):
        result = [
            [
                self.data[i][j] + other.data[i][j]
                for i in range(3)
            ]
            for j in range(3)
        ]
        return Matrix(result)

    def multiply(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)


# Example usage
if __name__ == "__main__":
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    B = Matrix([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])

    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    print("\nA + B:")
    print(A.add(B))

    print("\nA * B:")
    print(A.multiply(B))

    print("\nTranspose of A:")
    print(A.transpose())""""
class Matrix:
    def __init__(self, data):
        self.data = data  # 2D list for 3x3 matrix

    def display(self):
        for row in self.data:
            print(row)

    def __add__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                sum = 0
                for k in range(3):
                    sum += self.data[i][k] * other.data[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[j][i])
            result.append(row)
        return Matrix(result)


# Sample matrices
mat1 = Matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

mat2 = Matrix([[9, 8, 7],
               [6, 5, 4],
               [3, 2, 1]])

print("Matrix 1:")
mat1.display()

print("\nMatrix 2:")
mat2.display()

# Addition
print("\nMatrix Addition:")
add_result = mat1 + mat2
add_result.display()

# Multiplication
print("\nMatrix Multiplication:")
mul_result = mat1 * mat2
mul_result.display()

# Transpose
print("\nTranspose of Matrix 1:")
transpose_result = mat1.transpose()
transpose_result.display()
