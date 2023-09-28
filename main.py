"""
Author = Alex Fenlon
Number = R00220236
Project Name = The Long Island Camping and Caravanning Resort
This code is a booking form for the long island camping and caravanning resort, it takes an input of a family name, phone number, accommodation type, people in a group, whether or not they have a pool pass and the number of kids they have for the kids club and stores that information in a file with the family name and bookings number. It then shows how many orders of each accommodation, pool passes, kids for kids club, most popular accommodation, expected income, average per booking and the number of slots remaining.
"""
def family_name():
  while True:
    surname = input("Enter your family name: ")
    if 0 < len(surname) < 15:
      break
    else:
      print("ERROR - Name is null or greater than 15 characters\n\n")
      pass
  return surname
#this function takes user input and cbecks if its emply or greater than 15 characters
def phone_number():
  phone = ""
  while True:
    try:
      phone = str(input("Enter your phone number: "))
      if len(phone) >= 12:
        print("Please emter a number between 1 and 12 digits")
      else:
        if int(phone) >= 0 and int(phone) < 100000000000:
          break
        else:
          print("Please emter a number between 1 and 12 digits")
      pass
    except:
      print("Please enter a number")
  return phone
#this function takes a user input and checks if it between 0 and 12 characters long to use as a phone number
def accommodation_type():
  accommodation = 0
  print("Choose your accommodation type: \n")
  print("1. Deluxe Caravan      (€2000.0)")
  print("2. Standard Caravan    (€1600.0)")
  print("3. Camp Site            (€200.0)")
  while True:
    try:
      accommodation = int(input("Option? (1-3): "))
    except:
      print("Please enter a valid number")
    if 0 < accommodation <=3:
      break
    else:
      print("ERROR")
      pass
  return accommodation
#this function chooses the accommodation type using user input menu and makes sure between 0 and 4
def group_num():
  group = 0
  while True:
    try:
      group = int(input("\nHow many people in your group? "))
      if group > 0:
        break
    except:
      print("Please enter a number")
      pass
  return group
#this function asks user fir nunber of people in a group and returns it
def pool_pass():
  while True:
    pool = input("Do you require a family pool pass (Y/N)? €150 total. : ")
    pool = pool.upper()
    if pool == "Y" or pool == "N":
      break
    else:
      pass
  return pool
#this function asks if the user needs a familt pass and returns the answer
def child_club(group):
  kids_club = ""
  while True:
    try:
      kids_club = int(input("How many kids will join the kids club? €100 each : "))
      pass
    except:
      print("Please enter a number")
    if 0 <= int(kids_club) < group:
      break
    else:
      print("More people in the group required for this many kids")
      pass
  return kids_club
#this function asks how many kids the user has and checks if tbe number of kids is less than the group and returns the answer
def read_file():
  acc_list = []
  price_list = []
  book_list = []
  count = 0
  with open('Bookings_2022.txt', 'r') as bookings:
   for line in bookings:
     div = line.split(',')
     acc_list.append(div[0])
     price_list.append(int(div[1]))
     book_list.append(int(div[2]))
  for i in range(len(acc_list)):
    count = count + book_list[i]
  return acc_list,price_list, book_list,count
#this fumction reads the bookings text file and divides the parts and puts them into lists and returns them
def read_extra():
 list_name = []
 quantity = []
 with open('Extras.txt', 'r') as extra:
    for line in extra:
       div = line.split(',')
       list_name.append(div[0])
       quantity.append(int(div[1]))
 return list_name,quantity
#this fumction reads the extra text file and divides the parts and puts them into lists and returns them
def booking_num(count):
  if count < 10:
    booking_numbers = (f"0{count}")
  else:
    booking_numbers = count
  return booking_numbers
#this function creates the bookings numbers by using count
def booking_and_extra_cost(accommodation,kids_club,pool,acc_list,price_list, book_list,list_name,quantity):
  acc_cost = 0
  kids_cost = 0
  pool_cost = 0
  if accommodation == 1:
    acc_cost = price_list[0]
    book_list[0] = book_list[0] + 1
  elif accommodation == 2:
    acc_cost = price_list[1]
    book_list[1] = book_list[1] + 1
  elif accommodation == 3:
    acc_cost = price_list[2]
    book_list[2] = book_list[2] + 1
  quantity[0] = quantity[0] + int(kids_club)
  kids_cost = int(kids_club) * 100
  if pool == "Y":
    quantity[1] = quantity[1] + 1
    pool_cost = 150
  else:
    pool_cost = 0
  total_cost = acc_cost + kids_cost + pool_cost
  return acc_cost, kids_cost, pool_cost, total_cost
#this function calculates the costs for everything and the total
def booking_details(accommodation,kids_club,pool,surname,booking_numbers, acc_cost, total_cost, group,phone):
  acc_type = ""
  if accommodation == 1:
    acc_type = "Deluxe Caravan"
  if accommodation == 2:
    acc_type = "Standard Caravan"
  if accommodation == 3:
    acc_type = "Camp"
  print("BOOKING DETAILS \n================")
  print(f"Family Name:            {surname}")
  print(f"Phone Number:           {phone}")
  print(f"Booking ID:             {booking_numbers}")
  print(f"Accommodation Type:     {acc_type}")
  print(f"No of People:           {group}")
  print(f"Pool Pass?:             {pool}")
  print(f"No for Kids Club:       {kids_club}")
  print(f"Accommodation Cost:     {acc_cost}")
  print(f"Total Cost:             {total_cost}")
  with open(f"{surname}_{booking_numbers}.txt", "w") as client_file:
    print("BOOKING DETAILS \n================", file=client_file)
    print(f"Family Name:            {surname}", file=client_file)
    print(f"Phone Number:           {phone}", file=client_file)
    print(f"Booking ID:             {booking_numbers}", file=client_file)
    print(f"Accommodation Type:     {acc_type}", file=client_file)
    print(f"No of People:           {group}", file=client_file)
    print(f"Pool Pass?:             {pool}", file=client_file)
    print(f"No for Kids Club:       {kids_club}", file=client_file)
    print(f"Accommodation Cost:     {acc_cost}", file=client_file)
    print(f"Total Cost:             {total_cost}", file=client_file)
    client_file.close()
#this fumctiom takes all the information and outputs it to the user and added to a file with the name of the family and booking number.
def update(list_name,quantity,acc_list, price_list, book_list):
  with open('Extras.txt', 'w') as extra:
    for i in range(len(list_name)):
      extra.write(f"{list_name[i]},{quantity[i]}\n")
  with open('Bookings_2022.txt', 'w') as bookings:
    for i in range(len(acc_list)):
      bookings.write(f"{acc_list[i]},{price_list[i]},{book_list[i]}\n")
#this function writes back to the extras text file
def review_bookings(acc_list, price_list,book_list,quantity, booking_numbers,count):
  print("LONG ISLAND HOLIDAYS – Review Bookings")
  print("======================================")
  print(f"Deluxe Caravan:            ¦ {book_list[0]}")
  print(f"Standart Caravan:          ¦ {book_list[1]}")
  print(f"Camp Site                  ¦ {book_list[2]}")
  print(f"Total Pool Passes:         ¦ {quantity[1]}")
  print(f"No. for Kids Club:         ¦ {quantity[0]}")
  projected_income = (price_list[0] * book_list[0]) + (price_list[1] * book_list[1]) +(price_list[2] * book_list[2]) + (quantity[1] * 150)+ (quantity[0] * 100)
  print(f"Projected Profits:          ¦{projected_income}")
  remain_site = 30 - count
  print(f"No. of remaing sites:      ¦ {remain_site}")
  print(f"Average income per bookings¦ {projected_income / count}")
  if count >= 5:
    popular = max(book_list)
    if popular == book_list[0]:
      print(f"Most Popular Accommodation  ¦{acc_list[0]}")
    elif popular == book_list[1]:
      print(f"Most Popular Accommodation  ¦{acc_list[1]}")
    elif popular == book_list[2]:
      print(f"Most Popular Accommodation  ¦{acc_list[2]}")
#This function creates a review of the bookings and displays all information to the user.
def main():
  menu_option = 0
  acc_list, price_list, book_list, count = read_file()
  while True:
    print("\nLONG ISLAND HOLIDAYS \n=======================")
    print("1. Make a Booking")
    print("2. Review Bookings")
    print("3. Exit\n")
    try:
      menu_option = int(input("Option? (1 - 3): "))
      pass
    except:
      "Error"
    while True:
      if menu_option == 1:
        if count == 30:
          print("No more bookings allowed")
          break
        print("\nLONG ISLAND HOLIDAYS - Making a Booking\n=======================================")
        surname = family_name()
        phone = phone_number()
        accommodation = accommodation_type()
        group = group_num()
        pool = pool_pass()
        kids_club = child_club(group)
        count += 1
        booking_numbers = booking_num(count)
        list_name, quantity = read_extra()
        acc_cost,kids_cost,pool_cost,total_cost = booking_and_extra_cost(accommodation,kids_club,pool,acc_list,price_list, book_list,list_name,quantity)
        booking_details(accommodation,kids_club,pool,surname,booking_numbers, acc_cost, total_cost, group,phone)
        update(list_name,quantity,acc_list, price_list, book_list)
        break
      if menu_option == 2:
        if count == 0:
          print("Bookings required")
          break
        else:
          pass
        review_bookings(acc_list, price_list,book_list,quantity, booking_numbers,count)
      if menu_option == 3:
        exit(0)
      else:
        break
main()