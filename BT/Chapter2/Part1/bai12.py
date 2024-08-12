def main():
   cost = float(input('Enter the cost of a meal at the restaurant : '))
   
   tip = cost * 0.18
   tax = cost * 0.05
   
   total = cost + tip + tax
   
   print(f"Cost of the meal: ${cost:.2f}")
   print(f"Tax amount: ${tax:.2f}")
   print(f"Tip amount: ${tip:.2f}")
   print(f"Total amount to be paid: ${total:.2f}")

if __name__ == '__main__':
    main()