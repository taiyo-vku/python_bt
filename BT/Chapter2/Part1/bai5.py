st = input('Enter your string: ')
first_five_character = st[:5]
last_five_character = st[len(st) - 5:]
four_str_1_line = 4 * (st + " ")
four_str_4_line = 4 * (st + "\n")

# In ra màn hình
print('First five characters are: ' + first_five_character)
print('Last five characters are: ' + last_five_character)
print('Four strings of one line are: ' + four_str_1_line)
print('Four strings of four line are: ' + four_str_4_line)