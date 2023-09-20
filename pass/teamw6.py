print ( )
with open ('hr_system.txt') as hrs:
    for line in hrs:
        line = line.split()
        name = line[0]
        id = int ( line[1] )
        tittle = line[2]
        salary = float ( line[3] )

        # core 1
        # print (line)
        # core 2
        # print (f'Name: {name}')
        # core 3
        # print ( f'Name: {name} Tittle: { tittle} ' )

        # Stretch Challenge
        # 1 
        # print ( f'Name: {name} (ID: {id}) Tittle { tittle} - ${salary:.2f} ' )
        # 2
        # print ( f'Name: {name} (ID: {id}) Tittle { tittle} - payment ${salary / 24 :.2f} ' )
        # 3
        if tittle != 'Engineer':
            print ( f'Name: {name} (ID: {id}) Tittle { tittle} - payment ${salary / 24:.2f} ' )
        else:
            print ( f'Name: {name} (ID: {id}) Tittle { tittle} - payment ${(salary / 24) + 1000:.2f} ' )
print ( )