import manual
import transport_function


def main():
    while True:
        try:
            counter = int(input('1 - Manual input. 2 - calculate the problem from the condition: '))
            break
        except ValueError:
            print("ERROR! length of the vector - must be integer value. Try again...")
    if counter == 1:
        while True:
            try:
                length_a = int(input('Input length of the vector a: '))
                break
            except ValueError:
                print("ERROR! length of the vector - must be integer value. Try again...")
        while True:
            try:
                length_b = int(input('Input length of the vector b: '))
                break
            except ValueError:
                print("ERROR! length of the vector - must be integer value. Try again...")
        while True:
            try:
                print('Enter matrix C - array of coefficients (transport cost): ')
                matrix_C = []
                for i in range(length_a):
                    for j in range(length_b):
                        matrix_C.append(float(input('Enter c_{0}_{1}: '.format(i + 1, j + 1))))
                break
            except ValueError:
                print('ERROR! Coefficient must be float value. Try again...')
        print(matrix_C)
        vector_a = []
        while True:
            try:
                print('Input vector a:')
                for i in range(length_a):
                    a = float(input("Enter a_{0}: ".format(i + 1)))
                    vector_a.append(a)
                break
            except ValueError:
                print("ERROR! Coefficient must be float value. Try again...")
        print(vector_a)
        vector_b = []
        while True:
            try:
                print('Input vector b:')
                for i in range(length_b):
                    b = float(input("Enter b_{0}: ".format(i + 1)))
                    vector_b.append(b)
                break
            except ValueError:
                print("ERROR! Coefficient must be float value. Try again...")
        print(vector_b)
        manual.etaps()
        transport_function.transport_solve(matrix_C, vector_a, vector_b)
    elif counter == 2:
        matrix_C = [5, 15, 3, 6, 10,
                    23, 8, 13, 27, 12,
                    27, 14, 14, 10, 18,
                    8, 26, 7, 28, 9]
        vector_a = [9, 11, 15, 16]
        vector_b = [8, 9, 13, 8, 12]
        manual.etaps()
        transport_function.transport_solve(matrix_C, vector_a, vector_b)
main()