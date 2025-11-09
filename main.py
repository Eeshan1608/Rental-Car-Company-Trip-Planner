




hours = 0
hours_2 = 0
hours_3 = 0


def rent_car ():

  print("Now moving on to the cars we have available for rent")
  print()
  print(" 1. Ford Model T")
  print(" 2. Tesla Model Y")
  print(" 3. Ferrari 12 Cillindri")  

  car = input("Enter the number of the car you want to rent: ")
  print()
  if car == "1":

    return()
   

print("Hello Welcome to our rental car company HERTZ.")
print()
print()
print("Where would you like to go from Seoul today: ")
print()
print("1. Busan")
print("2. Gwangju")
print("3. Daegu")

destination = input("Enter the number of your destination: ")
print()
if destination == "1": 
   print("The distance from Seoul to Busan is approximately 390km and will take you around 4 hours to reach Busan")

elif destination == "2":
   print("The distance from Seoul to Gwangju is approximately 310km and will take you around 3 hours to reach Gwangju")

elif destination == "3":
   print("The distance from Seoul to Daegu is approximately 280km and will take you around 3 hours to reach Daegu")

chosen_car = rent_car()