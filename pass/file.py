with open ('books.txt') as books_list:

    for line in books_list:

        book = line.split()
        
        print (book[0:2])