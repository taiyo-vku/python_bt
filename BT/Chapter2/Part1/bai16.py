import math
def main():
   d = float(input('Nhap vao chieu cao cua vat duoc tha roi : '))
   v0 = 0
   a = 9.8
   
   v1 = math.sqrt(math.exp(v0) + 2 * a * d)

   print(f'Toc do cua mot vat khi tha roi tu do cao {d} la : {v1:.2f}')



if __name__ == '__main__':
    main()