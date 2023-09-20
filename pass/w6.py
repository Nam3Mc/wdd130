people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# The list of people is included in the program.
# The program can iterate through each string in the list.
# The program can split the string into the appropriate pieces.S
# The youngest age is identified.
# The name of the youngest person is identified.

print ( )
youngest = 150
name = ''


for line in people:
    line = line.split()
    person = line [0]
    age = int ( line[1] )
    print ( f'Name {person} is {age} Years old.' )

    if age < youngest:
        youngest = age
        name = person

print ( )
print ( f'The youngest age is: {youngest} ' )
print ( f'The youngest person is: {name} ' )
print ( )