def main():
   a = float(input('Enter the length of the room: '))
   b = float(input('Enter the width of the room: '))

   if a < b :
        print("Warning: The length of the room is less than the width.") 
   else : 
        S = a * b
        print(f'The area of the room is {S:.2f}')





if __name__ == '__main__':
    main() 