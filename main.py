rent = "Y"
metric_imperial = 0
busan_distance = 390
busan_time = 4
Gwangju_distance = 310
Gwangju_time = 3
Daegu_distance = 280
Daegu_time = 3
fuel_efficiency = 0
cars = ["Ford Model T", "Tesla Model Y", "BYD U9X"]
car_speeds = [60, 217, 417]
car_efficiency = [9,8,6]
car = 0

def unit_choice():
    global metric_imperial
    global busan_distance, Gwangju_distance, Daegu_distance, car_speeds, car_efficiency, fuel_efficiency
    metric_imperial = input("Would you like to use metric or imperial units? (m/i): ")
    if metric_imperial.lower() == "m":
        print("You have chosen metric units")
        print()
    elif metric_imperial.lower() == "i":
        print("You have chosen imperial units")
        print()
        busan_distance = busan_distance * 0.621371
        Gwangju_distance = Gwangju_distance * 0.621371
        Daegu_distance = Daegu_distance * 0.621371
       

def byd(rent):
   print("The BYD U9X is a modern car with a top speed of 417 km/h")
   rent = input("would you like to rent this car? (y/n):")
   if rent.lower() == "y":
        print("You have chosen the BYD U9X")
   else:
        print("You have chosen to not rent the BYD U9X")
        print("Would you like to rent the Tesla Model Y or the Ford Model T?")
       
def tesla(rent):
   print("The Tesla Model Y is a electric car with a top speed of 217km/h")
   rent = input("would you like to rent this car? (y/n):")
   if rent.lower() == "y":
        print("You have chosen the Tesla Model Y")
   else:
        print("You have chosen to not rent the Tesla Model Y")
        print()
        print("Would you like to rent the BYD U9X or the Ford Model T?")



def rent_car ():
  global cars
  print()
  print("Now moving on to the cars we have available for rent.......")
  print()
  print("1. " + cars[0])
  print("2. " + cars[1])
  print("3. " + cars[2])

  car = input("Enter the number of the car you want to rent: ")
  print()
  if car == "1":
     print("You have chosen the Ford Model T")
     print()
     print("The Ford Model T is a classic car with a top speed of 60km/h ")
     print()
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print("You plan to travel for " , question , " hours.")
     print()
     travel_time = distance / car_speeds[0]
     print("Based on the Ford Model T's max speed, it will take about", round(travel_time, 1), "hours to reach your destination.")
     print()
     print()
     print("A better option would be the " , cars[1] , " or " , cars[2] , " for more speed and comfort.")
     print()
     change = input("Would like to rent BYD U9X or the Tesla Model Y (Type in Tesla or BYD): ")
     if change.lower() == "byd":
        print("You have upgraded to the " + cars[2] )
        print()
        print()
        byd(rent)
        car = "3"
     elif change.lower() == "tesla":   
        print("You have upgraded to the " + cars[1])
        print()
        print()
        tesla(rent)
        car = "2"
     else:
        print("You decided to keep the " + cars[0])


               
  elif car == "2":
     print("You have chosen the Tesla Model Y")
     print()
     print("The Tesla Model Y is a electric car with a top speed of 217km/h ")
     print()
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print("You plan to travel for " , question ," hours.")
     print()
     travel_time = distance / car_speeds[1]
     print("Based on the Tesla Model Y's max speed, it will take about", round(travel_time, 1), "hours to reach your destination.")
     print()
     print()
     print("A better option would be the " , cars[2] , " for more speed .")
     change = input("Would like to rent BYD? (y/n): ")
     if change.lower() == "y":
         print("You have upgraded to the " + cars[2])
         byd(rent)
         cars = "3"
     else:
       print("You decided to keep the " + cars[1])
   


  elif car == "3":
     print("You have chosen the BYD U9X")
     print()
     print("The BYD U9X is a modern car with a top speed of 417 km/h ")
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print()
     print('Your plan to travel for ', question , ' hours.')
     print()
     travel_time = distance / car_speeds[2]
     print("Based on the BYD U9X's max speed, it will take about", round(travel_time, 1), "hours to reach your destination.")
     print()
     print("This is the best option for you ")
  return car
     
def fuelcost():
   print()
   print()
   fuel_price = int(input("What is the fuel price in won per liter: "))
   print("The fuel price is ", fuel_price, "won per liter")
 
   if chosen_car == "1":
      fuelefficency = car_efficiency[0]
      fuel_cost = (distance / fuelefficency)*fuel_price
      print()
      print("The fuel cost for the Ford Model T is ", fuel_cost)

   elif chosen_car == "2":
      fuelefficency = car_efficiency[1]
      fuel_cost = (distance / fuelefficency)*fuel_price
      print()
      print("The fuel cost for the Tesla Model Y is ", fuel_cost)

   else:
      fuelefficency = car_efficiency[2]
      fuel_cost = (distance / fuelefficency)*fuel_price
      print()
      print("The fuel cost for the BYD U9X is ", fuel_cost)
      print()
      print()

      
print("Hello Welcome to our rental car company HERTZ.")
print()
unit_choice()
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
   print("The distance from Seoul to Busan is approximately " + str(busan_distance) + " km and will take you around " + str(busan_time) + " hours to reach Busan")
   distance = busan_distance
elif destination == "2":
   print("The distance from Seoul to Gwangju is approximately " + str(Gwangju_distance) + " km and will take you around " + str(Gwangju_time) + " hours to reach Gwangju")
   distance = Gwangju_distance
elif destination == "3":
   print("The distance from Seoul to Daegu is approximately " + str(Daegu_distance) + " km and will take you around " + str(Daegu_time) + " hours to reach Daegu")
   distance = Daegu_distance
else:
   distance = 0

chosen_car = rent_car()
fuelcost()

print("Have a safe trip!")