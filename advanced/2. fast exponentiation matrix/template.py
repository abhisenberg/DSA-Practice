
###### MATRIX FUNCTIONS ######
def fast_exponentiation(a, x):
    base = a
    res = identity_matrix(len(a))

    while x > 0:
        if x & 1 == 1:
            res = matrix_mul(res, base)    
        base = matrix_mul(base, base)      
        x >>= 1
    return res

def matrix_mul(a, b):
    m1, n1 = len(a), len(a[0])
    m2, n2 = len(b), len(b[0])

    if n1 != m2:
        raise IndexError("Indices of matrices not matching for multiplication")

    ans = [[0]*n2 for _ in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                ans[i][j] = (ans[i][j] + (a[i][k] * b[k][j]))
    return ans

def print_mat(mat):
    print()
    for arr in mat:
        print(arr)
    print()

def identity_matrix(n):
    return [[ (1 if i==j else 0) for j in range(n)] for i in range(n) ]
