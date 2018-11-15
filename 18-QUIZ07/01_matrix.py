#std35: Phitchawat Lukkanathiti 6110503371
#date: 15NOV2018
#program: 01_matrix.py
#description: do matrix operation with computer

MATRIX_PATH = "MATRIX/"

def loadMatrix(file_name):
    matrix = []
    f = open(MATRIX_PATH+file_name)
    while True:
        line = f.readline()
        if not line:
            break
        matrix.append([float(x) for x in line.split()])
    return matrix

def multiplyNumber(a, num):
    for j in range(len(a)):
        for i in range(len(a[0])):
            a[j][i]*=num
    return a

def addMatrix(a, b):
    output = [[None for j in range(len(a[0]))] for i in range(len(a))]
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return (None, True)
    for j in range(len(a)):
        for i in range(len(a[0])):
            output[j][i]=a[j][i]+b[j][i]
    return output

def transposeMatrix(a):
    output = [[None for j in range(len(a))] for i in range(len(a[0]))]
    for j in range(len(a)):
        for i in range(len(a[0])):
            output[i][j]=a[j][i]
    return output

def crossMatrix(a, b):
    if len(b)!=len(a[0]):
        return "Dimension Error"
    n_row = len(a)
    n_col = len(b[0])
    n_cross = len(b)
    output = [[0 for j in range(n_col)] for i in range(n_row)]
    for j in range(n_row):
        for i in range(n_col):
            for k in range(n_cross):
                output[j][i] += a[j][k]*b[k][i]
    return output

if __name__ == "__main__":
    A = loadMatrix("A.txt")
    B = loadMatrix("B.txt")
    C = loadMatrix("C.txt")
    
    q1 = crossMatrix(C,addMatrix(transposeMatrix(C),multiplyNumber(A,2)))
    print(q1)
    q2 = addMatrix(transposeMatrix(crossMatrix(A,B)),multiplyNumber(C,-1))
    print(q2)
    q3 = crossMatrix(crossMatrix(B,B),B)
    print(q3)
    q4 = addMatrix(transposeMatrix(A),multiplyNumber(C,7))
    print(q4)
