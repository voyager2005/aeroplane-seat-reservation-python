from colors import bcolors
import sys
from random import seed
from random import random

# declaring global variables
name = "username"
phone_number = 0000000000
travel_date = "dd mm yyyy"
current_location = "unknown"
destination = "unknown"

# declaring variables to print the seating pattern
occupied_seats = [True, False,                             # row 1
                  False, True,                             # row 2
                  True, True, False, True,                 # row 3
                  True, False, False, False,               # row 4
                  False, False, True, True,                # row 5
                  True, True, True, False, False, False,   # row 6
                  False, True, True, True, True, False,    # row 7
                  True, False, False, False, False, True,  # row 8
                  True, True, False, False, False, False,  # row 9
                  False, False, False, True, True, True,   # row 10
                  True, True, True, True, True, True]      # row 11
all_seats = ["1A", "1F", "2A", "2F", "3A", "3B", "3E", "3F", "4A", "4B", "4E", "4F", "5A", "5B", "5E", "5F",
             "6A", "6B", "6C", "6D", "6E", "6F", "7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C", "8D", "8E", "8F",
             "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E", "10F",
             "11A", "11B", "11C", "11D", "11E", "11F"]

# declaring global variables to accept the seat from the user
number_of_seats_booked = 0
users_seat = ["nothing here"] * 28
all_seats_index = 0


# displaying the welcome pattern at the beginning
def display_welcome():
    # displaying welcome
    print(" *       *   * * * *   *         * * *    * * * *    *     *   * * * * ")
    print(" *       *   *         *        *        *       *   * * * *   *       ")
    print(" *   *   *   * * * *   *       *        *         *  *  *  *   * * * * ")
    print(" * *   * *   *         *        *        *       *   *     *   *       ")
    print(" *       *   * * * *   * * * *   * * *    * * * *    *     *   * * * * ")
    print(f"{bcolors.BOLD}{bcolors.HEADER}{bcolors.UNDERLINE}Welcome to https://github.com/voyager2005 Travels, "
          f"We would like to take some information: {bcolors.ENDC}{bcolors.ENDC}{bcolors.ENDC}")

# accepting the users name
def accept_name():
    global name

    name = input("Your name please: ")  # accepting the users name
    name.strip()  # removing unwanted spaces before and after the name
    name = name + " "  # adding a space after the name

    # declaration
    word = ""
    new_name = ""

    # capitalizing name
    for i in range(0, len(name)):
        ch = name[i]
        word = word + ch

        if ch == ' ':
            word = word.capitalize()
            new_name = new_name + word
            word = ""

    name = new_name


# accepting other details from the user like his phone number, current location and destination
def other_details():
    global phone_number
    global current_location
    global destination
    global travel_date

    # accepting the phone number of the user
    phone_number = input("Enter your phone number: ")
    while len(phone_number) != 10:
        print("Please make sure that the phone number that you have entered is 10 digits long")
        print("The phone number you entered was " + str(len(phone_number)) + " digits long ")
        phone_number = input("Please enter the phone number: ")

    # accepting the date of travel
    travel_date = input("Travel Date(dd mm yyyy): ")

    # accepting the current location
    current_location = input("From: ")

    # accepting the destination
    destination = input("To: ")

    # converting current_location and destination into upper case
    current_location = current_location.upper()
    destination = destination.upper()


def display_aeroplane_seat():
    # global variables
    global occupied_seats
    global all_seats

    # displaying Business Class
    print("             " + f"{bcolors.BOLD}Business Class{bcolors.ENDC}" + "           ")

    for i in range(0, 4):
        # displaying 1A and 2A with colour code
        if occupied_seats[i] and (i == 0 or i == 2):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + "                             ", end="")
        elif not occupied_seats[i] and (i == 0 or i == 2):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + "                             ", end="")

        # displaying 1F and 2F with colour code
        if occupied_seats[i] and (i == 1 or i == 3):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 1 or i == 3):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying First Class
    print("              " + f"{bcolors.BOLD}First Class{bcolors.ENDC}" + "              ")

    for i in range(4, 16):
        # displaying 3A, 4A and 5A with colour code
        if occupied_seats[i] and (i == 4 or i == 8 or i == 12):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 4 or i == 8 or i == 12):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 3B, 4B and 5B with colour coding
        if occupied_seats[i] and (i == 5 or i == 9 or i == 13):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="                   ")
        elif not occupied_seats[i] and (i == 5 or i == 9 or i == 13):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="                   ")

        # displaying 3E, 4E and 5E with colour coding
        if occupied_seats[i] and (i == 6 or i == 10 or i == 14):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 6 or i == 10 or i == 14):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 3F, 4F and 5F with colour coding
        if occupied_seats[i] and (i == 7 or i == 11 or i == 15):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 7 or i == 11 or i == 15):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying Economy Class
    print("             " + f"{bcolors.BOLD}Economy Class{bcolors.ENDC}" + "            ")

    for i in range(16, 52):
        # displaying 6A, 7A, 8A and 9A with colour code
        if occupied_seats[i] and (i == 16 or i == 22 or i == 28 or i == 34):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 16 or i == 22 or i == 28 or i == 34):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats[i] and (i == 17 or i == 23 or i == 29 or i == 35):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 17 or i == 23 or i == 29 or i == 35):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats[i] and (i == 18 or i == 24 or i == 30 or i == 36):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="         ")
        elif not occupied_seats[i] and (i == 18 or i == 24 or i == 30 or i == 36):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="         ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats[i] and (i == 19 or i == 25 or i == 31 or i == 37):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 19 or i == 25 or i == 31 or i == 37):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats[i] and (i == 20 or i == 26 or i == 32 or i == 38):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 20 or i == 26 or i == 32 or i == 38):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats[i] and (i == 21 or i == 27 or i == 33 or i == 39):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 21 or i == 27 or i == 33 or i == 39):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    for i in range(40, 52):
        # displaying 10A and 11A with colour code
        if occupied_seats[i] and (i == 40 or i == 46):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 40 or i == 46):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats[i] and (i == 41 or i == 47):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[i] and (i == 41 or i == 47):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="  ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats[i] and (i == 42 or i == 48):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="      ")
        elif not occupied_seats[i] and (i == 42 or i == 48):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="      ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats[i] and (i == 43 or i == 49):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[i] and (i == 43 or i == 49):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="  ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats[i] and (i == 44 or i == 50):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[i] and (i == 44 or i == 50):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="  ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats[i] and (i == 45 or i == 51):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 45 or i == 51):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    accept_users_seat()


# accepting the users seat number
def accept_users_seat():
    global number_of_seats_booked
    global users_seat
    global all_seats_index
    global occupied_seats

    terminator = 1
    while terminator <= 24:
        # accepting users seat
        users_seat[number_of_seats_booked] = input(f"{bcolors.BOLD}Please enter the seat "
                                                   f"that you want to book: {bcolors.ENDC}")

        # finding index of all seats
        for j in range(0, len(all_seats)):
            if all_seats[j] == users_seat[number_of_seats_booked]:
                all_seats_index = j

        if occupied_seats[all_seats_index]:
            print(f"{bcolors.WARNING}{bcolors.BOLD}That seat has already been booked/reserved"
                  f"{bcolors.ENDC}{bcolors.ENDC}")
            continue
        elif not occupied_seats[all_seats_index]:
            occupied_seats[all_seats_index] = True
            number_of_seats_booked += 1
            print(f"{bcolors.OKCYAN}Your seat {users_seat[number_of_seats_booked-1]} has been booked{bcolors.ENDC}")

        # asking if the user wants to book another seat
        while True:
            choice = input("Do you want to reserve another seat? ")
            choice = choice.upper()
            if choice == "YES":
                print("\n"*40)
                display_aeroplane_seat()
            elif choice == "NO":
                display_boarding_pass()
            else:
                print(f"{bcolors.WARNING}Please enter either {bcolors.BOLD}yes or no{bcolors.ENDC}{bcolors.ENDC}")


# displaying boarding pass
def display_boarding_pass():
    global users_seat
    global number_of_seats_booked

    print("\n"*40)
    print(f"{bcolors.BOLD}{bcolors.UNDERLINE}{bcolors.HEADER}Boarding Pass for all the seats that you booked:"
          f"{bcolors.ENDC}{bcolors.ENDC}{bcolors.ENDC}")

    seed(10)

    for i in range(0, number_of_seats_booked):
        value = random() * 10
        #  I know you want to change the travels name? ↓↓↓
        print("   https://github.com/voyager2005 Travels       ")
        print("            BOARDING PASS                      ")
        print(name + "\t" + "Flight: OKL012" + "\t" + users_seat[i])
        print(f"Gate: {int(value)}" + "     " + "date: " + travel_date + "\t" + "cost: 15000")
        print()

    sys.exit()


# calling the methods
while True:
    display_welcome()
    accept_name()
    other_details()
    display_aeroplane_seat()
