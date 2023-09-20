data_list = []

countries = []
years = []
expectancies = []

found_countries = []
found_years = []
found_expectancies = []

highest_country = None
highest_year = 0
highest_expectancy = 0

highest_country_found = None
highest_year_found = 0
highest_expectancy_found = 0

lowest_country = None
lowest_year = 0
lowest_expectancy = 9999999

lowest_country_found = None
lowest_year_found = 0
lowest_expectancy_found = 9999999

search = None
lowest_year_search = 999999

menu = [ '1. Display the highest Life Expectancy.', 
        '2. Display the lowest Life Expectancy.', 
        '3. Search for year.', '0. quit.', 
        ]
menu_2 = [ '1. Find average Life Expectancy.',
          '2.Find the highest Life Expectancy.',
          '3. the lowest Life Expectancy.']
search = None

with open ('life-expectancy.csv') as data:
    
    next(data)

# to clean and separate
    for line_with in data:
        line_without = line_with.strip()
        line = line_without.split ( ',' )

# assining each element to a list
        countries.append ( line[0] )
        years.append ( int (line[2]) )
        expectancies.append ( float(line[3]) )

#  setting index 
    for index in range ( len(countries) ):
        country = countries[index]
        year = years[index]
        expectancy = expectancies[index]
        highest = expectancies[index]
        lowest = expectancies[index]

# higest
        if highest > highest_expectancy: 
            highest_expectancy = highest
            highest_year = year
            highest_country = country

# lowest 
        elif lowest < lowest_expectancy:
            lowest_expectancy = lowest
            lowest_year = year
            lowest_country = country    

while search != 0:

    for line in menu:
        print ( line )   
    search = int ( input ( 'Type your choose: ' ) )
    print ( )

    if search == 1:
        print ( f'{highest_country} Is the country with the highest Life Expectancy. ' )
        print ( f'Whit {max(expectancies)} in {highest_year} ' )
        print ( )

    elif search == 2:
        print ( f'{lowest_country} Is the country with the lowest Life Expectancy. ' )
        print ( f'With {min(expectancies)} in {lowest_year} ' )
        print ( )

    elif search == 3:
        search = int ( input ( 'Enter the year of interest: ' ) )
        print ( )

        if search < min(years) or search > max(years):
            print ( f'The year is not in the list. Type a year between {min(years)} and {max(years)}: ' )
            search = int ( input ( 'Enter the year of interest: ' ) )
            print ( )
        
        elif search >= min(years) or search <= max(years):

            for year in range ( len ( years )):
                if years[year] == search:
                    found_countries.append(countries[year])
                    found_years.append(years[year])
                    found_expectancies.append(expectancies[year])
    
            for index in range ( len ( found_countries ) ):
                country = found_countries[index]
                year = found_years[index]
                expectancy = found_expectancies[index]
                
                if expectancy > highest_expectancy_found:
                    highest_country_found = country
                    highest_year_found = year
                    highest_expectancy_found = expectancy
                
                elif expectancy < lowest_expectancy_found:
                    lowest_country_found = country
                    lowest_year_found = year
                    lowest_expectancy_found = expectancy
                
            averange = sum(found_expectancies) / len(found_expectancies)

            print ( f'For the year {search}: ' )
            print ( f'The average life expectancy across all countries was: { averange :.2f} ' )
            print ( )
        
            print ( f'{highest_country_found} Is the country with the highest Life Expectancy. ' )
            print ( f'Whit {highest_expectancy_found :.2f}' )
            print ( f'In {highest_year_found } ' )
            print ( )

            print ( f'{lowest_country_found} Is the country with the lowest Life Expectancy. ' )
            print ( f'With {lowest_expectancy_found :.2f}' )
            print ( f'In {lowest_year_found } ' )
            print ( )       

    elif search == 0:
        print ( 'Good bye! ' )