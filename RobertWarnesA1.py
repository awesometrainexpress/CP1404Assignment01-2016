"""
CP1404 Assignment 1
Items for Hire
Robert Warnes
Due 07/04/2016
Github URL - https://github.com/robertwarnes/CP1404-Assignment-01-2016

Pseudocode

function main()

    display intro message
    display menu
    display open message

    open "items.csv" as in_file for writing

    names = blank list
    descriptions = blank list
    prices = blank list
    states = blank list

    for each line in items

        name = line[0]
        description = line[0]
        price = line[0]
        state = line[0]

        add name to names
        add description to descriptions
        add price to prices
        add state to states

    display loading message
    get query
    while query is not 'q'
        if query is 'l'
            function listing_items(names, descriptions, prices, states)
        if query is 'h'
            function hiring_an_item(names, descriptions, prices, states)
        if query is 'r'
            function returning_an_item(names, descriptions, prices, states)
        if query is 'a'
            function adding_an_item(names, descriptions, prices, states)
        else:
            display error message
        display menu
        get query

    display save message
    display farewell message
    close in_file

function listing_items(names, descriptions, prices, states):

    display list message
    display items list

function hiring_an_item(names, descriptions, prices, states):

    display items list
    get item number

returning_an_item(names, descriptions, prices, states):

    display items list
    get item number

adding_an_item(names, descriptions, prices, states):

    get item name
    get item description
    get item price
    add name to names
    add description to descriptions
    add price to prices
    add state to states

"""

def main():

    import csv

    ERROR_MESSAGE = "Invalid menu Choice"
    FILENAME = "items.csv"
    FAREWELL_MESSAGE = "Have a nice day :)"
    INVALID_MESSAGE = "Invalid number"
    LIST_MESSAGE = "All items on file (* indicates item is currently out)"
    MENU_MESSAGE = """Menu:
    (L)ist all items
    (H)ire an item
    (R)eturn an item
    (A)dd new item to stock
    (Q)uit"""
    INTRO_MESSAGE = "Items for Hire - by Robert Warnes"
    RETURN_MESSAGE = "Enter the number of an item to return"

    in_file = open(FILENAME)
    items = csv.reader(in_file, delimiter = ',')

    names = []
    descriptions = []
    prices = []
    states = []

    for line in items:

        name = line[0]
        description = line[1]
        price = float(line[2])
        state = line[3]

        names.append(name)
        descriptions.append(description)
        prices.append(price)
        states.append(state)

    print(INTRO_MESSAGE)
    print("{} Items loaded from {}".format(len(names), FILENAME))
    print(MENU_MESSAGE)
    query = input (">>> ").lower()
    while query != "q":
        if query == "l":
            listing_items(names, descriptions, prices, states, LIST_MESSAGE)
        elif query == "h":
            hiring_an_item(names, descriptions, prices, states, INVALID_MESSAGE)
        elif query == "r":
            returning_an_item(names, descriptions, prices, states, INVALID_MESSAGE)
        elif query == "a":
            adding_an_item(names, descriptions, prices, states)
        else:
            print(ERROR_MESSAGE)
        print(MENU_MESSAGE)
        query = input (">>> ").lower()
    print("{} items saved to {}".format(len(names), FILENAME))
    print(FAREWELL_MESSAGE)

    in_file.close()

def listing_items(names, descriptions, prices, states, LIST_MESSAGE):

    print(LIST_MESSAGE)
    for i in range(len(names)):
        print("{} - {} ({}) = ${:,.2f} - {}".format(i, names[i], descriptions[i], prices[i], states[i]))

def returning_an_item(names, descriptions, prices, states, INVALID_MESSAGE): #return an item that is being hired

    if "out" in states: #check if any items haven't been returned
        for i in range(len(names)):
            print("{} - {} ({}) = ${:,.2f} - {}".format(i, names[i], descriptions[i], prices[i], states[i]))
        finished = False
        while not finished:
            try:
                print("Enter the number of an item to return")
                i = int(input(">>> "))
                if "out" in states[i]:
                    print("{} returned".format(names[i]))
                    states[i] = "in"
                else:
                    print("That item is not on hire")

                finished = True

            except IndexError:
                print(INVALID_MESSAGE)

            except ValueError:
                print("Invalid input; enter a number")

    else:
        print("No items are currently on hire")

def hiring_an_item(names, descriptions, prices, states, INVALID_MESSAGE): #hire an item that is currently available

    for i in range(len(names)):
        print("{} - {} ({}) = ${:,.2f} - {}".format(i, names[i], descriptions[i], prices[i], states[i]))

    finished = False
    while not finished:
        try:
            print("Enter the number of an item to hire")
            i = int(input(">>> "))
            if "in" in states[i] :
                print("{} hired for ${:,.2f}".format(names[i], prices[i]))
                states[i] = "out"
            else:
                print("That item is not available for hire")

            finished = True

        except IndexError:
                print(INVALID_MESSAGE)

        except ValueError:
                print("Invalid input; enter a number")

def adding_an_item(names, descriptions, prices, states): #get information to add item to the list

    name = input("Item name:")
    while name == "":
        print("Name can not be empty")
        name = input("Item name:")
    description = input("Description:")
    while description == "":
        print("Description can not be empty")
        description = input("Description:")
    finished = False
    while not finished:
        try:
            price = float(input("Price per day:"))
            while price == "":
                print("Price can not be empty")
                price = float(input("Price per day:"))
            finished = True
        except ValueError:
            print("enter a valid number")

    state = "in" #item is automatically in by default
    print("{} ({}), ${:,.2f} now available for hire".format(name, description, price))
    names.append(name)
    descriptions.append(description)
    prices.append(price)
    states.append(state)

main()