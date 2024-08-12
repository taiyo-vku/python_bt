import math

def main():
    r = float(input('Enter the radius of the cyclinder : '))
    h = float(input('Enter the height of the cyclinder: '))

    v = math.pi * r*r*h
    print('Volume of the cyclinder is : ' + str(round(v)))


if __name__ == "__main__":
    main()
