# (a ** 2) = (b) + (2 * a) - 1

def equation(Aa, Bb):
    return ((Bb) + (2 * Aa) - 1)

def square_root():
    squared_a = int(input("Enter the value for which you want to find the square root:\n"))

    A = 1
    B = 0

    while True:
        if equation(A, B) == squared_a:
            break

        B = equation(A, B)
        A += 1

    print("The square root of {} is {}.".format(squared_a, A))

def square():
    a_ = int(input("Enter the value for which you want to find the square:\n"))

    A = 1
    B = 0

    while True:
        if A == a_:
            break

        B = equation(A, B)
        A += 1

    print("The square of {} is {}.".format(a_, equation(a_, B)))

def main():
    option = input("Type 1 to calculate the square root of a number or 2 to calculate the square of a number:\n")

    if option == "1":
        square_root()

    elif option == "2":
        square()

    else:
        print("Invalid option!")
        main()

main()
