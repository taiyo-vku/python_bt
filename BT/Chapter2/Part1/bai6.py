import math

def main():
    r = float(input('Enter the radius of the cyclinder : '))
    h = float(input('Enter the height of the cyclinder: '))

    V = math.pi * r*r*h
    print(f'Volume of the cyclinder is : {V:.2f}')


if __name__ == "__main__":
    main()
