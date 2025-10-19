#ask users for file type
def get_filetype():

    while True:
        response = input("File type: ").lower()

        #check for i or xxx response
        if response == "xxx" or response == "i":
            return response

        #Check if integer
        elif response in ['integer', 'int', 'i']:
            return "integer"

        #check for image
        elif response in ['image' 'picture', 'img', 'p']:
            return "picture"

        #check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        #If the input is wrong output error
        else:
            print("Please enter a valid file type")
            return None


#main routine goes
while True:
    file_type = get_filetype()
    print(f"You chose {file_type}")
    if file_type == "xxx":
        break