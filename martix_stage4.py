def main():
    while True:
        choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: """)
        if choice == "1":
            Add_matrices()
        elif choice == "2":
            Multiply_constant()
        elif choice == "3":
            Multiply_matrices()
        elif choice == "4":
            Transpose_matrix()
        elif choice == "0":
            break


def Add_matrices():
    A = input("Enter size of first matrix: ").split()
    A = [int(i) for i in A]
    A_detail = []
    print("Enter first matrix:")
    for i in range(A[0]):
        A_detail.extend(input().split())
        A_detail.append("\n")
    A_detail = [float(i) if i != "\n" else "\n" for i in A_detail]

    B = input("Enter size of second matrix: ").split()
    B = [int(i) for i in B]
    B_detail = []
    print("Enter second matrix:")
    for i in range(B[0]):
        B_detail.extend(input().split())
        B_detail.append("\n")
    B_detail = [float(i) if i != "\n" else "\n" for i in B_detail]

    if A != B:
        print("The operation cannot be performed.\n")
    else:
        C = list(map(lambda a, b: a + b if (type(a) == float or type(a) == int) else "\n", A_detail, B_detail))
        C = [f"{str(i)} " if i != "\n" else "\n" for i in C]
        print("The result is:")
        print("".join(C))

def Multiply_constant():
    A = input("Enter size of matrix: ").split()
    A = [int(i) for i in A]
    A_detail = []
    print("Enter matrix:")
    for i in range(A[0]):
        A_detail.extend(input().split())
        A_detail.append("\n")
    multiper = float(input("Enter constant: "))
    A_detail = [float(i) * multiper if i != "\n" else "\n" for i in A_detail]
    A_detail = [f"{str(i)} " if i != "\n" else "\n" for i in A_detail]
    print("The result is:")
    print("".join(A_detail))

def Multiply_matrices():
    A = input("Enter size of first matrix: ").split()
    A = [int(i) for i in A]
    A_detail = []
    print("Enter first matrix:")
    for i in range(A[0]):
        A_detail.append(input().split())
    A_detail = [[float(j) for j in i] for i in A_detail]

    B = input("Enter size of second matrix: ").split()
    B = [int(i) for i in B]
    B_detail = []
    print("Enter second matrix:")
    for i in range(B[0]):
        B_detail.append(input().split())
    B_detail = [[float(j) for j in i] for i in B_detail]

    if A[-1] != B[0]:
        print("The operation cannot be performed.\n")
    else:
        print("The result is:")
        result = [[sum(x*y for x,y in zip(i,j)) for j in zip(*B_detail)] for i in A_detail]
        result = [[str(j) for j in i] for i in result]
        for i in result:
            print(" ".join(i))


def Transpose_matrix():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    transpose_choice = input("Your choice: ")
    size = input("Enter matrix size: ").split()
    size = [int(i) for i in size]
    print("Enter matrix: ")
    if transpose_choice == "1":
        Main_diagonal_transpose(size)
    elif transpose_choice == "2":
        Side_diagonal_transpose(size)
    elif transpose_choice == "3":
        Vertical_line_transpose(size)
    elif transpose_choice == "4":
        Horizontal_line_transpose(size)


def Main_diagonal_transpose(size):
    row, column = size[0], size[-1]
    martix = [input() for _ in range(row)]
    new_martix = martix.copy()
    new_martix = [i.split() for i in new_martix]
    final_list = []
    for i in new_martix:
        for j in i:
            final_list.append(j)
    print("The result is:")
    for i in range(row):
        print(" ".join(final_list[i::column]))


def Side_diagonal_transpose(size):
    row, column = size[0], size[-1]
    martix = [input() for _ in range(row)]
    new_martix = martix[::-1]
    new_martix = [i.split() for i in new_martix]
    new_martix = [i[::-1] for i in new_martix]
    final_list = []
    for i in new_martix:
        for j in i:
            final_list.append(j)
    print("The result is:")
    for i in range(row):
        print(" ".join(final_list[i::column]))


def Vertical_line_transpose(size):
    row, column = size[0], size[-1]
    martix = [input() for _ in range(row)]
    new_martix = [i.split() for i in martix]
    final_list = [i[::-1] for i in new_martix]
    print("The result is:")
    for i in final_list:
        print(" ".join(i))

def Horizontal_line_transpose(size):
    row, column = size[0], size[-1]
    martix = [input() for _ in range(row)]
    new_martix = martix[::-1]
    print("The result is:")
    for i in new_martix:
        print(i)

main()