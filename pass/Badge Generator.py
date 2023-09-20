#Badge Generator
print ("Hello, welcome. \nWe are glad to help you.")
print ()
FirstN = input("May I have your fist name? Please. ")
print ("Thank you.")
print ()
lastN = input("May I have your last name? Please. ")
print ()
input("Is your name: " + FirstN + " " + lastN + "? ")
print ("Thank your for confirming.")
print ()
Email = input("Please. intruduce your elmail address here: ")
Phone = input("Your phone number is also requested, please type it here: ")
print ("For continuing the process, you need to provide mext information:")
print ()
Job = input("Describe your job position: ")
Id = input("This is last step, please intriduce your ID Number: ")
print ()
print (" our system is verifying your inforamtion. \nNext window will show your details, please verify them.")
print ( )
#print (f"{lastN.upper()}, {FirstN.capitalize () }" )
print(f"{lastN.upper ()}, {FirstN.capitalize ()}")
print (Job.title ())
print (f"ID: {Id}")
print ()
print (Email.lower ())
print (Phone)

"""Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Software Architect
ID: 83-5558

janedoe@email.com
212212212
"""
