# -*- coding: utf-8 -*-
"""
Created on 07/06/2016

@author: juliaroebuck originally, edited by Aaron

#Unused or previous versions of code
def add_item():
    print("Add item")
    new_item = input("Please enter new item to add: ")
    my_list.append(new_item)
    my_storage = open("dvds.txt", "r+")
    list_length = len(my_list)
    my_storage.(new_item)
    my_storage.close()"""

def add_item(my_list, username):
    my_list = load_list(username)
    #print("Add item")
    new_item = input("Please enter new item to add: ")
    my_list.append(new_item)
    save_list(my_list, username)
    print(new_item+" was added.")

#function to delete existing item in user's list
def delete_item(my_list, username):
    item_deleted = False
    my_list = load_list(username)
    #print("Delete item")
    item_to_delete = input("Which item would you like to delete? ")
    #print(item_to_delete)

    filename = username+"dvds.txt"
    my_storage = open(filename, "w")

    #goes through every line in user's list, re-writing it to the file if it is not the item the user entered to be deleted.
    #.rstrip removes any trailing whitespace, such as \n
    for i in my_list:
        #print(i)
        if i.rstrip() != (item_to_delete.rstrip()):
            my_storage.write(i)
            #print(i + "Line written")
        else:
            item_deleted = True
    my_storage.close()
    if item_deleted == False:
        print(item_to_delete+" is not in your list of DVDs and therefore could not be deleted.")
    else:
        print(item_to_delete+" was deleted.")

#function to print out list of user's stored DVDs
def print_items(my_list):
    #loops through all items in list of DVDs and prints them out, adding a comma if it is not the last item
    if len(my_list) != 0:
        for i in range (len(my_list)):
            if i < len(my_list)-1:
                print((my_list[i].rstrip())+", ", end="")
            else:
                print(my_list[i].rstrip())
    else:
        print("There are currently no items in your collection.")
#function to add new item to the list

#function to load list of DVDs from the file into a variable
def load_list(username):
    #print("Load_list")
    filename = username+"dvds.txt"
    my_storage = open(filename,'r')
    my_list = my_storage.readlines()
    my_storage.close()
    #print(my_list)
    return my_list

#function to save list from variable back into the file containing the list of the user's DVDs
def save_list(my_list, username):
    #print("Save List")
    filename = username+"dvds.txt"
    my_storage = open(filename,'w')
    list_length = len(my_list)
    for i in range(list_length):
        my_storage.write(my_list[i].rstrip())
        my_storage.write("\n")
    my_storage.close()

#function to add new user
def add_user():
    #saves contents of current users to variable
    login_details = open("logindetails.txt",'r')
    login_list = login_details.readlines()
    login_details.close()
    #print(login_list)

    #variables to save new username and password
    username = input("Please enter your new username: ")
    password = input("Please enter your new password: ")

    #adds new username and password to the list
    login_list.append(username+"\n")
    login_list.append(password+"\n")

    login_details = open("logindetails.txt",'w')

    #saves contents of the variable to the file containg login details
    list_length = len(login_list)
    for i in range(list_length):
        login_details.write(login_list[i])
    #print(login_list)
    login_details.close()

    #creates a new file to save new user's DVDs into
    filename = username+"dvds.txt"
    file = open(filename, "w+")
    file.close()

    print("User "+username+" was added with the password "+password)

#function to let the user login
def login():
    #saves the contents of the file containing login details to a variable
    login_details = open("logindetails.txt",'r') #r - read w - write r+ append
    login_list = login_details.readlines()
    login_details.close()
    #print(login_list)

    #asks for username and password and saves them to a variable
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    #variable the stores a value that will determin what is printed to the user
    print_result = 0

    #loops through contents of login_list
    for i in range (len(login_list)):
        #print(login_list[i].rstrip())
        #if the username is in the list...
        if (username == ((login_list[i]).rstrip())):
            #check if the password is in the list
            if (password == ((login_list[i+1]).rstrip())):
                #if so, the user has logged in succesfully
                print("Login succesful")
                #print(username+password)
                #return True and the username of the current user
                return (True, username)
            else:
                #the username exists but password was incorrect. print_result should equal 1 to represent this
                print_result = 1
                #print(print_result)
        else:
            #the username does not exist. If print_result is not already equal to 1, set it to 0 to represent this.
            #if it is already set to 1 the username must exist!
            #print(username+password)
            if print_result != 1:
                print_result = 0
            #print(print_result)
    #depending on print_result's value, print the result of the login to the user
    if print_result == 0:
        print("Username does not exist")
    elif print_result == 1:
        print("Incorrect password")
    else:
        print("Error")
    #return false and the username of the current user
    return (False, username)

#starts login function and loops it until it returns True and the user has succesfully logged in
result = login()
while result[0] == False:
    result = login()

#print(result)
#print(result[0])
#print(result[1])

#loads contents of the current user's DVD collection to the variable
my_list = load_list(result[1])
run = True

#main part of the code that lets the user add to, delete or view their DVD collection. Uses all the above functions.
#parameters will be my_list for the list of DVDs to use, and result[1] for the current user
while run == True:
    user_input = input("What do you want to do? Add a new (U)sername and password, (A)dd an item, (D)elete an item, (P)rint everything, (Q)uit: \n")
    if (user_input == "Q"):
        run = False
    if (user_input == "A"):
        add_item(my_list, result[1])
    if (user_input == "D"):
        delete_item(my_list, result[1])
    if (user_input == "P"):
        my_list = load_list(result[1])
        print_items(my_list)
    if (user_input == "U"):
        add_user()