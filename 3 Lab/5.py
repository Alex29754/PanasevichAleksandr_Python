mat = [list(map(int, input().split())) for i in range(3)]
n = 0
if mat[0][3] == None:
    detmat = (mat[0][0] * mat[1][1] * mat[2][2] + mat[0][1] * mat[1][2] * mat[2][0] + mat[0][2] * mat[1][0] * mat[2][1]) - mat[0][2] * mat[1][1] * mat[2][0] - mat[0][0] * mat[1][2] * mat[2][1] - mat[0][1] * mat[1][0] * mat[2][2]
    if detmat == 0:
        print("Столбцы линейно зависимы ")
        for i in mat:
            for j in i:
                print(j, end = " ")
            print()
