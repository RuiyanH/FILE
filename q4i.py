import numpy as np

def determinant(M):
    if len(M) == 2:
        return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    else:
        sign = -1
        result = 0
        for i in range(len(M)):
            m = []
            for j in range(1, len(M)):
                mm = []
                for k in range(len(M)):
                    if k != i:
                        mm.append(M[j][k])
                m.append(mm)
            sign *= -1
            sum += sign * M[0][i] * determinant(m)
    return result

test_matrix = [[1,-2,3],[0,-3,-4],[0,0,-3]]

print(determinant(test_matrix))
