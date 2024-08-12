def main():
   a = float(input('Enter the length of the field: '))
   b = float(input('Enter the width of the field: '))

   if a < b :
        print("Warning: The length of the field is less than the width.") 
   else : 
        S = a * b
        S_acres = S / 4046.86
        print(f'The area of the field is {S_acres:.2f}')
        





if __name__ == '__main__':
    main()