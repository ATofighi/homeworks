import helper


# https://gist.github.com/j9ac9k/6b5cd12aa9d2e5aa861f942b786293b4
def gauss(A):
    m = len(A)
    assert all([len(row) == m + 1 for row in A[1:]]), "Matrix rows have non-uniform length"
    n = m + 1

    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k

        # Check for singular matrix
        assert A[i_max][k] == 1, "Matrix is singular! {}".format(A[i_max][k])

        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]

        for i in range(k + 1, m):
            f = A[i][k] // A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f
                A[i][j] %= 2
                A[i][j] += 2
                A[i][j] %= 2

            # Fill lower triangular matrix with zeros:
            A[i][k] = 0

    # Solve equation Ax=b for an upper triangular matrix A
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] // A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
            A[k][m] %= 2
            A[k][m] += 2
            A[k][m] %= 2
    return x


n = 51


def lfsr(a):
    new_s = [0] * n
    for i in range(n):
        new_s[i] = a[0][i] ^ a[9][i]
    new_a = []
    for i in range(1, n):
        new_a.append(a[i])
    new_a.append(new_s)
    return new_a


def I(size=n):
    a = []
    for i in range(size):
        a.append([0] * size)
        a[i][i] = 1
    return a


def get_value(x, y):
    res = 0
    for i in range(len(x)):
        res = (res + x[i] * y[i]) % 2
    return res


with open('q4-cipher.txt') as file:
    cipher = bin(int(file.readline().strip(), 16))[2:]


def main():
    a = I()
    A = []
    for i in range(len(cipher)):
        a = lfsr(a)
        if i % 16 == 0:
            s = []
            s.extend(a[0])
            s.append(int(cipher[i]))
            A.append(s)
            if len(A) == n:
                break
    x = gauss(A)

    plain_text = ''
    a = I()
    for i in range(len(cipher)):
        a = lfsr(a)
        plain_text += str((get_value(a[0], x) + int(cipher[i])) % 2)

    print(helper.to_bytes(int(plain_text, 2)))


main()
