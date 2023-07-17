def column_sum(matrix,rows,columns):

    result=[]
    for i in range(columns):
        sum=0
        for j in range(rows):
            sum+=matrix[j][i]
        result.append(sum)
    return result

matrix=[]
rows=int(input("Enter number of rows : "))
columns=int(input("Enter number of columns : "))
for i in range(rows):
    n=list(map(int,input().split()))
    matrix.append(n)

print(column_sum(matrix,rows,columns))
