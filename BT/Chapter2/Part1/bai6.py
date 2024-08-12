import math

def main():
    r = float(input('Enter the radius of the cyclinder : '))
    h = float(input('Enter the height of the cyclinder: '))

    s = math.pi * r*r*h
    print('Volume of the cyclinder is : ' + str(round(s)))


if __name__ == "__main__":
    main()
