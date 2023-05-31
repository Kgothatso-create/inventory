# Importing tabulate module from tabulate library
from tabulate import tabulate
#========The beginning of the class==========
class Shoe:
    # Constructor method to initialize the instance variables
    def __init__(self, country, code, product, cost, quantity):
        # The country where the shoe is manufactured
        self.country=country

        # A unique identifier code for the shoe
        self.code=code

        # The name of the shoe product
        self.product=product

        # The cost of the shoe
        self.cost=cost

        # The quantity of the shoe available in stock
        self.quantity=quantity

    # Method to get the cost of the shoe
    def get_cost(self):
        return self.cost
    
    # Method to get the quantity of the shoe available in stock
    def get_quantity(self):
        return self.quantity
        
    # Method to return a string representation of the shoe object
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
    
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
Creaded a header variable to store first line of text in text file as shoe object
'''
header=Shoe("Country","Code","Product","Cost","Quantity")
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    # Function will open the file inventory.txt and read the data from this file 
    # Using try for error handling
    try:
        with open ("inventory.txt","r") as file:
            # Skip first line
            next(file)

            for line in file:
                    # Split the line and remove new line characters
                    temp=line.strip().split(",")

                    # Creating a shoe object and appending it to the list
                    shoe_list.append(Shoe(temp[0], temp[1],temp[2], float(temp[3]),int(temp[4])))

    # Handling the errors that can occur when working wit files
    # Did reaserch on the possible errors and how to handle them
    # https://www.pythonforbeginners.com/error-handling/python-try-and-except
    # https://docs.python.org/3/library/exceptions.html

    # File is not found
    except FileNotFoundError:
        print(f"File not found.")

    # Do not have permission to read the file
    except PermissionError:
        print(f"Permission denied to read file.")

    # If the file cannot be opened.
    except IOError:
        print(f"File cannot be opened.")

    # Read a file that contains characters that are not supported by the current encoding
    except UnicodeDecodeError:
        print(f"Inventory file is incoded.")

    # Read a blank file
    except StopIteration:
        print("File is blank")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Print a separator line to make the output more readable
    print("-"*50)
    # Print a header for the add product section
    print("\t\tAdd new shoe to stock")
    print("-"*50)

    # Prompt the user to enter the country of origin for the shoe and capitalize it
    country=input("Enter country of origin: ").capitalize()

    # Prompt the user to enter the code for the shoe and convert it to uppercase
    code= input("Enter shoe code: ").upper()

    # Prompt the user to enter the name of the product
    product=input("Enter shoe name: ")

    # Use a while loop to ensure that the user enters a valid float value for the cost of the product
    while True:
        try:
            cost=float(input("Enter shoe price: "))
            break
        except ValueError:
            print("incorrect input")

    # Use a while loop to ensure that the user enters a valid integer value for the quantity of the product
    while True:
        try:
            quantity=int(input("Enter shoe quantity: "))
            break
        except ValueError:
            print("incorrect input")

    # Append the shoe details to the shoe_list object
    shoe_list.append(Shoe(country,code,product,cost,quantity))

    # Open the inventory.txt file in write mode and write the header and shoe details to it
    with open ("inventory.txt","w") as file:
        file.write(str(header)+"\n")
        for line in shoe_list:
            file.write(str(line)+"\n")
    # Print a message to confirm that the shoe details have been captured successfully        
    print("_"*45)
    print("Shoe details have been captured succesfully")
    print()

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    # Print a separator line to make the output more readable
    print("-"*50)
    # Print a header for the product in stock section
    print("\t\tAll shoes in Stock")
    print("-"*50)

    # Print header row
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]

    # create a list of tuples containing information about each shoe in the shoe_list
    rows = [(shoe.country, shoe.code, shoe.product, f"R {shoe.cost}", shoe.quantity) for shoe in shoe_list]

    # generate a table from the list of tuples using the headers and the "fancy_grid" table format
    table = tabulate(rows, headers=headers, tablefmt="fancy_grid")

    # print the table to the console
    print(table)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # This loop continuously checks for shoes that are low in stock and asks the user if they want to add more stock or not
    while True:
        # Prints a divider line and a header for the low stock products table
        print()
        print("-"*100)
        print("\t\t\t\tShoe low on stock")
        print("-"*100)

        # Creates a list of stock quantities for all the shoes in the inventory
        stock=[shoe.quantity for shoe in shoe_list]
        # Finds the lowest quantity in the stock list
        low_stock=min(stock)

        # Loops through all the shoes in the inventory and prints out the ones with the lowest stock quantity
        for shoe in shoe_list:
            if shoe.quantity == low_stock:
                # Formats the shoe data into a table row and prints it
                print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Made in", "Product code","Product","Product price","Product quantity"))
                print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(shoe.country, shoe.code,shoe.product,f"R {shoe.cost}",shoe.quantity))
                print()
        
        # Asks the user if they want to add more stock
        top_up_option=input("Would you like to add to stock quantity (Y/N )? ").capitalize()
        if top_up_option == "Y":
            # Prompts the user for the name of the shoe in case there are two shoe items with the same quantity and the quantity to add to the stock
            name_product=input("\nEnter shoe name: ")
            add_stock=int(input("Enter quantitiy to be added: "))

            # Loops through all the shoes in the inventory and updates the stock quantity for the product with the lowest stock and the given name
            for shoe in shoe_list:
                if shoe.quantity == low_stock and name_product== shoe.product:
                    shoe.quantity=shoe.quantity + add_stock
                    print()
                    # Prints out the updated shoe data in a table row
                    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Made in", "Product code","Product","Product price","Product quantity"))
                    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(shoe.country, shoe.code,shoe.product,shoe.cost,shoe.quantity))
                    print("_"*17)
                    print("Quantity updated")
                    # Breaks out of the loop after the first match is found
                    break
            # If no shoe match the given name and lowest stock quantity, prints an error message
            else:
                print(f"No shoe matching '{name_product}' and with quantity '{low_stock}' were found.")
            
            # Writes the updated inventory data to a file
            with open ("inventory.txt","w") as file:
                # Writes the header line
                file.write(str(header)+"\n")
                # Writes each shoe's data as a separate line
                for line in shoe_list:
                    file.write(str(line)+"\n")

        # If the user does not want to add more stock, breaks out of the loop
        elif top_up_option=="N":
            break

        # If the user enters an invalid option, prints an error message
        else:
            print("Invalid entry")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Print a separator line to make the output more readable
    print("-"*50)
    # Print a header for the search for a product
    print("\t\tSearch for shoe")
    print("-"*50)

    # Prompt the user to enter a product code and convert the input to uppercase
    product_code = input("Enter shoe code: ").upper()

    # Print a blank line for spacing
    print()

    # Iterate over each shoe in the shoe_list
    for shoe in shoe_list:
        # Check if the shoe's code matches the user's input
        if product_code == shoe.code:
            # Print a table header with column labels
            print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Made in", "Product code", "Product", "Product price", "Product quantity"))
            # Print the shoe's information in a table row format
            print("{:<20}{:<20}{:<20}R {:<20}{:<20}".format(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity))
            # Print a blank line for spacing
            print()
            # Exit the loop once a match is found
            break
    else:
        # If no match is found, print a message indicating so
        print("No shoe with that product code was found.")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Print a separator line to make the output more readable
    print("-"*50)

    # Print a header for the Value of all products in stock
    print("\t\tValue of all shoes in stock")
    print("-"*50)

    # Create empty lists to hold product names and values
    result = []
    product = []

    # Loop through each shoe object in the shoe_list
    for shoe in shoe_list:
        # Calculate the value of the current shoe by multiplying its cost and quantity
        value = shoe.get_cost() * shoe.get_quantity()

        # Add the current shoe's product name and value to the corresponding lists
        product.append(shoe.product)
        result.append(value)

    # Define the headers for the table
    header = ("Product", "Value")

    # Create a list of tuples representing each row in the table
    # Each tuple contains a product name and its corresponding value
    row = [(product[i], f"R {result[i]}") for i in range(len(product))]

    # Generate the table using the tabulate module
    table = tabulate(row, headers=header, tablefmt="fancy_grid")

    # Print the table
    print(table)

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Create a list of the quantity of each shoe in the shoe_list
    stock = [shoe.quantity for shoe in shoe_list]

    # Find the maximum quantity in the stock list
    high_stock = max(stock)

    # Print a header for the output
    print("-"*50)
    print("\t\tShoe most in stock")
    print("-"*50)

    # Iterate through the shoe_list to find the shoe(s) with the highest quantity in stock
    for shoe in shoe_list:
        if shoe.quantity == high_stock:
            # Print the name of the shoe that has the highest quantity in stock
            print(f"{shoe.product}: for sale")
            print()  # add a blank line for readability

#==========Main Menu=============

# Calling read shoe function
read_shoes_data()
while True:
    # Menu output and choices
    print("*"*50)
    print("\t\tMain Menu")
    print("*"*50)
    # Check the value of 'menu' variable and perform the corresponding task
    menu= input("""Enter one of the following menu options:

C- Capture new shoe to stock
L- View shoe low in stock
M- View maximum shoe in stock
S- Search for a shoe
VA- view all shoes in stock 
VI- View value of shoes
E- Exit \n""").lower().strip()
    
    # View all shoes
    if menu == "va":
        view_all()

    # Re-stock shoes
    elif menu == "l":
        re_stock()

    # Search for a specific shoe
    elif menu == "s":
        search_shoe()

    # View the value of each item
    elif menu == "vi":
        value_per_item()

    # View shoe with highest quantity
    elif menu== "m":
        highest_qty() 

    # Capture new shoes
    elif menu=="c":
        capture_shoes()

    # Exit the program
    elif menu=="e":
        print("Goodbye")
        break

    # Invalid entry
    else:
        print("Invalid entry")