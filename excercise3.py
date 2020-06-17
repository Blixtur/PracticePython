import sys

def creating_lists():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]
    mylist = []
    menu(a, mylist)

# Using the parameteres from creating_lists() function, ask the user for their choice of action.
def menu(a, mylist):
    print (a)
    # Asking for user input
    menu_opt = int(input("Would you like to sort the above list?: \n 1: Show list\n 2: Sort list \n 3: Exit \n"))
    if menu_opt == 1:
        print("The full list looks like this: ", a)
        menu(a, mylist)
    elif menu_opt == 2:
        #Asking for user input regarding the sorting options
        sorting = int(input("Enter number to sort with: "))
        sort_opt = int(input("Would you like to sort the list higher or lower? \n 1: Higher \n 2: Lower \n"))
        if sort_opt == 1:
            # Using the higher_sorting functions with the parameters a, mylist, sorting and sort_opt
            higher_sorter(a, mylist, sorting, sort_opt)
        elif sort_opt == 2:
            # Using the lower functions with the parameters a, mylist, sorting and sort_opt
            lower_sorter(a, mylist, sorting, sort_opt)
    # Exiting the program through sys.exit()
    elif menu_opt == 3:
        print("Exiting program")
        sys.exit()
# Using the previously declared parameters to run through the list: a. If i > sorting then that integer gets appended to "mylist". Mylist then gets printed
def higher_sorter(a, mylist, sorting, sort_opt):
    for i in a:
        if i > sorting:
            mylist.append(i)
    print("The list with numbers higher than ", sorting, " looks like this: ", mylist)
    mylist = a
    sys.exit()

# Using the previously declared parameters to run through the list: a. If i < sorting then that integer gets appended to "mylist". Mylist then gets printed
def lower_sorter(a, mylist, sorting, sort_opt):
    for i in a:
        if i < sorting:
            mylist.append(i)
    print("The list with numbers below ", sorting, " looks like this: ", mylist)
    mylist = a
    sys.exit()

#Running the starting function
creating_lists()
sys.exit()