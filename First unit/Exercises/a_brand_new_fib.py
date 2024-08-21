class MatrixFibonacci:
    Q = [[1, 1],
         [1, 0]]

    def __init__(self):
        self.__memo = {}

    def __multiply_matrices(self, m1, m2):
        # size 2x2

        a11 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        a12 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
        a21 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        a22 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]

        return [[a11, a12],
                [a21, a22]]

    def __get_matrix_power(self, matrix, power):
        if power == 1:
            return matrix
        if power in self.__memo:
            return self.__memo[power]
        K = self.__get_matrix_power(matrix, power // 2)
        R = self.__multiply_matrices(K, K)
        self.__memo[power] = R
        return R

    def get_number(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        powers = [2**b for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']

        matrices = [self.__get_matrix_power(MatrixFibonacci.Q, power)
                    for power in powers]

        while len(matrices) > 1:
            matrix1, matrix2 = matrices.pop(), matrices.pop()
            R = self.__multiply_matrices(matrix1, matrix2)
            matrices.append(R)
        return matrices[0][0][0]


if __name__ == '__main__':

    mfib = MatrixFibonacci()
    for n in range(0, 256):
        num = mfib.get_number(n)
        print(f'fib({n})  \t= {num}')