# ask user for width and loop until they
# enter a number that is larger than zero
def int_check(question, low):

    error = "Please enter a number that is more than zero"

    while True :

        try:
            # ask user for a number
            response = int(input(question))
            #check number is more than zero
            if response >= 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

#main routine goes here
for item in range(0, 2):
    integer = int_check("integer: ", 0)
    print(integer)

for item in range(0, 2):
    width = int_check("width: ", 0)
    print(width)

print()

for item in range(0, 2):
    height = int_check("height: ", 1)
    print(height)
