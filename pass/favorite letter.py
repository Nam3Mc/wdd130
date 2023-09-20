#  variables
days = []
concets = []
amounts = []

incomes = []
incomes_dates = []
incomes_concect = []

expensives = []
expensives_dates = []
expensives_concets = []

highest_expensive = 0
lowest_expensive = -9999999
expensive_date_highest = None
expensive_date_lowest = None
expensive_name_highest = None
expensive_name_lowest = None

highest_income = 0
lowest_income = 9999999
income_date_highest = None
income_date_lowest = None
income_name_higest = None
income_name_lowset = None

with open ( 'Finances.csv' ) as file:
    print ( )
    next(file)

    for column_with in file:
        column_woithou = column_with.strip()
        column = column_woithou.split(',')

        days.append( int (column[0]))
        concets.append(column[1])
        amounts.append( float (column[2]))

    # total = sum(amounts)
    # print (f'Your valance is: {total:.2f}')
    print ( )

    for line in range ( len ( days ) ):
        day = days[line]
        concet = concets[line]
        amount = amounts[line]

        highest_amount = amounts[line]
        lowest_amount = amounts[line]

        if highest_amount > highest_income:
            highest_income = highest_amount
            income_name_higest = concet
            income_date_highest = day

        elif lowest_amount < lowest_income and lowest_amount > 0:
            lowest_income = lowest_amount
            income_name_lowset = concet
            income_date_lowest = day

        elif highest_amount < highest_expensive:
            highest_expensive = highest_amount
            expensive_date_highest = day
            expensive_name_highest = concet

        elif lowest_amount > lowest_expensive and lowest_amount < 0:
            lowest_expensive = lowest_amount
            expensive_date_lowest = day
            expensive_name_lowest = concet

    for value in amounts:
        if value < 0:
            expensives.append(float(value))
            total_expensives = sum(expensives)
        elif value > 0:
            incomes.append(float(value))
            total_incomes = sum(incomes)

print ( f'Your highest expensive was on {expensive_date_highest} for $ {highest_expensive} referent to {expensive_name_highest}' )
print ( )

print ( f'Your total incomes was {total_incomes}')
print ( f'Your total expensives was {total_expensives }')


