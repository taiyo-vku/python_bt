import math

def main():

    a = 3
    b = 4
    c = 5
    A = math.pi / 2
    B = math.pi / 3
    C = math.pi / 6

    # a = float(input("Enter the length of side a: "))
    # b = float(input("Enter the length of side b: "))
    # c = float(input("Enter the length of side c: "))
    
    # A = float(input("Enter the value of angle A (in radians): "))
    # B = float(input("Enter the value of angle B (in radians): "))
    # C = float(input("Enter the value of angle C (in radians): "))
    

    S_ABC = 0.5 * a * b * math.sin(C)
    S_BCA = 0.5 * b * c * math.sin(A)
    S_CAB = 0.5 * c * a * math.sin(B)

    if (S_ABC == S_BCA ) and ( S_BCA == S_CAB) :
        print('The area of the triangle is: {S_ABC:.2f}')


if __name__ == '__main__':
    main()