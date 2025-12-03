

rent = "Y"
metric_imperial = 0
busan_distance = 390
busan_time = 4
Gwangju_distance = 310
Gwangju_time = 3
Daegu_distance = 280
Daegu_time = 3
fuel_efficiency = 0
cars = ["Ford Model T", "Chevy Cobalt SS", "Buggati Chiron"]
car_speeds = [60, 155, 357]
car_efficiency = [13,22,11]
car = 0

def speed_label():
    if metric_imperial == "m":
        return "km/h"
    else:
        return "mph"

def convert_speed(speed):
    if metric_imperial == "m":
        return speed
    else:
        return round(speed * 0.621371, 2)

def unit_choice():
    global metric_imperial
    global busan_distance, Gwangju_distance, Daegu_distance, car_speeds, car_efficiency, fuel_efficiency
    metric_imperial = input("Would you like to use metric or imperial units? (m/i): ")
    if metric_imperial.lower() == "m":
        print()
        print("You have chosen metric units")
        print()
    elif metric_imperial.lower() == "i":
        print()
        print("You have chosen imperial units")
        print()
        busan_distance = busan_distance * 0.621371
        Gwangju_distance = Gwangju_distance * 0.621371
        Daegu_distance = Daegu_distance * 0.621371

def unit_label():
    if metric_imperial == "m":
        return " km"
    else:
        return " miles"
      

def Buggati(rent):
   print("The Bugatti Chiron has a top speed of 417 km/h")
   rent = input("Would you like to rent this car? (y/n):")
   if rent.lower() == "y":
        print("You have chosen the Bugatti Chiron")
   else:
        print("You have chosen to not rent the Bugatti Chiron")
        print("Would you like to rent the Chevy Cobalt SS or the Ford Model T?")

def chevy(rent):
   print("The Chevy Cobalt SS has a top speed of 217 km/h")
   rent = input("Would you like to rent this car? (y/n):")
   if rent.lower() == "y":
        print("You have chosen the Chevy Cobalt SS")
   else:
        print("You have chosen to not rent the Chevy Cobalt SS")
        print()
        print("Would you like to rent the Bugatti Chiron or the Ford Model T?")


def rent_car ():
  global cars
  print()
  print("Now moving on to the cars we have available for rent.......")
  print()
  print("1. " + cars[0])
  print("2. " + cars[1])
  print("3. " + cars[2])
  print()
  car = input("Enter the number of the car you want to rent: ")
  print()
  if car == "1":
     print()
     print("The Ford Model T is a classic car with a top speed of", convert_speed(60), speed_label(),)
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
     change = input("Would like to rent Buggati Chiron or the Chevy Cobalt SS (Type in Chevy or Bug): ")
     if change.lower() == "bug":
        print("You have upgraded to the " + cars[2] )
        print()
        print()
        Buggati(rent)
        car = "3"
     elif change.lower() == "chevy":   
        print("You have upgraded to the " + cars[1])
        print()
        print()
        chevy(rent)
        car = "2"
     else:
        print("You decided to keep the " + cars[0])


               
  elif car == "2":
     print()
     print("The Chevy Cobalt SS has a top speed of", convert_speed(217), speed_label())
     print()
     question = input("Firstly, how long do you plan to travel to reach there:  ")
     print("You plan to travel for " , question ," hours.")
     print()
     travel_time = distance / car_speeds[1]
     print("Based on the Chevy Cobalt SS max speed, it will take about", round(travel_time, 1), "hours to reach your destination.")
     print()
     print()
     print("A better option would be the " , cars[2] , " for more speed .")
     print()
     print()
     change = input("Would like to rent Buggati Chiron? (y/n): ")
     if change.lower() == "y":
         print()
         print("You have upgraded to the " + cars[2])
         Buggati(rent)
         cars = "3"
     else:
        print()
        print("You decided to keep the " + cars[1])
   


  elif car == "3":
     print()
     print("The Bugatti Chiron has a top speed of", convert_speed(357), speed_label())
     print()
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print()
     print('Your plan to travel for ', question , ' hours.')
     print()
     travel_time = distance / car_speeds[2]
     print("Based on the Buggati Chiron's max speed, it will take about", round(travel_time, 1), "hours to reach your destination.")
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
      print("The fuel cost for the Chevy Cobalt SS is ", fuel_cost)

   else:
      fuelefficency = car_efficiency[2]
      fuel_cost = (distance / fuelefficency)*fuel_price
      print()
      print("The fuel cost for the Buggati Chiron is ", fuel_cost)
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
   print("The distance from Seoul to Busan is approximately " + str(round(busan_distance)) + "" + unit_label() + " and will take you around " + str(busan_time) + " hours to reach Busan")
   distance = busan_distance
elif destination == "2":
   print("The distance from Seoul to Gwangju is approximately " + str(round(Gwangju_distance)) + "" + unit_label() + "and will take you around " + str(Gwangju_time) + " hours to reach Gwangju")
   distance = Gwangju_distance
elif destination == "3":
   print("The distance from Seoul to Daegu is approximately " + str(round(Daegu_distance)) + "" + unit_label() + "" +  " and will take you around " + str(Daegu_time) + " hours to reach Daegu")
   distance = Daegu_distance
else:
   distance = 0

chosen_car = rent_car()
fuelcost()

print("Have a safe trip :)")







