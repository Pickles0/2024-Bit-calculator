#Generates Headings
def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")

#Display instructions
def instructions():
    statement_generator("Instructions", "-")
    print("instructions go here...")

    print(""""
Instructions go here
-instruction 1
-instruction 2
-instruction 3
    """)

#main routine goes here
want_instructions=input("Press <enter> to read the instructions " "or any key to continue")

#Display instructions if required
if want_instructions == "":
    instructions()

print("Program continues")