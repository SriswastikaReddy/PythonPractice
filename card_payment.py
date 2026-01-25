#card payment receipt project

card_no = '1423 4789 4656 7896'
amount = 1000
last_digit = card_no[15:]
four = 'x'* 4 + " "
disp_no = four * 3 + last_digit
print(f'your account is debit of amount {amount}.card no \n{disp_no}')