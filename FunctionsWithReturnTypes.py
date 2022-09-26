#Functions with Return Types

def format_name(f_name, l_name):
    #Docstrings - definition has to go on the first line after declarations
    #Docstrings explain what a function does
    #you can do multi line comments in docstrings
    """Take a first and last name and format it to the title case version
    of the name."""
    full_name = (f_name.title() + " " + l_name.title() )
    return full_name
    #or
    #return f"{f_name.title()} {f_name.title()}"

firstname = (input("Enter your first name: "))
lastname = (input("Enter your last name: "))
print("Your name is " + format_name(firstname, lastname))