print ( 'Loand study: ' )
large_of_loan = int ( input ( 'From 1 to 10, How large is the loan? ' ) )
if large_of_loan >= 5:
    loan = True
else:
    loan = False
credit_history = int ( input ( 'From 1 to 10, How good is your credit history? ' ) )
incomes_rate = int ( input ('From 1 to 10, How high is your income? ' ) )
large_of_payment = int ( input ( 'From 1 to 10, How large is your down payment? ' ) )
print ( )
if loan and ( credit_history >= 7 or incomes_rate >= 7 ) and large_of_payment >= 5:
    loan_state = True
else:
    loan_state = False
if loan_state:
    print ( 'yes' )
else:
    print ( 'no' )