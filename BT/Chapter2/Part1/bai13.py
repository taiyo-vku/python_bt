def main():
   n = int(input('Enter a positive integer : '))

   S = ( n * (n+1) ) / 2

   print(f'The sum of the first {n} positive integers is : {S}')

if __name__ == '__main__':
    main()