def matmult(m1, m2):
    result = []
    for i in range(len(m1)):
        t = []
        for j in range(len(m2[0])):
            sum1 = 0
            k = 0
            while(k < len(m1[0])):
                sum1 = sum1 + m1[i][k] * m2[k][j]
                k = k + 1
            t.append(sum1)
        result.append(t)
    return result


list1 = list(eval(input('List 1 = ')))
list2 = list(eval(input('List 2 = ')))
pdt = matmult(list1, list2)
print('Product = ', pdt)