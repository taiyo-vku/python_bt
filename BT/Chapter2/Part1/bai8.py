import math

def main():
    
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # tinh nua chu vi
    s = (a + b + c ) / 2

    # Dien tich heron
    S = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print(f'The are fo the triangle is : {S:.2f}')

if __name__ == '__main__':
    main()