


busan_distance = 390
busan_time = 4
Gwangju_distance = 310
Gwangju_time = 3
Daegu_distance = 280
Daegu_time = 3

cars = ["Ford Model T", "Tesla Model Y", "BYD U9X"]
car_speeds = [60, 217, 417]


def rent_car ():

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
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print("You plan to travel for " , question , " hours.")
     print()
     print("A better option would be the " , cars[1] , " or " , cars[2] , " for more speed and comfort.")
     print()
     change = input("Would like to rent BYD U9X (y/n): ")
     if change.lower() == "y":
       print("You have upgraded to the " + cars[2] )   

     
        

             
     
     

  elif car == "2":
     print("You have chosen the Tesla Model Y")
     print()
     print("The Tesla Model Y is a electric car with a top speed of 217km/h ")
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print("You plan to travel for " , question ," hours.")
     print()
     print("A better option would be the " , cars[2] , " for more speed .")
     change = input("Would like to rent another car? (y/n): ")
     if change.lower() == "yes":
         print("You have upgraded to the " + cars[2])
     else:
       print("You decided to keep the " + cars[1])



  elif car == "3":
     print("You have chosen the BYD U9X")
     print()
     print("The BYD U9X is a modern car with a top speed of 417 km/h ")
     question = input("Firstly, how long do you plan to travel to reach there (in hours):  ")
     print('You plan to travel for ', question , ' hours.')
     print()
     print("This is the best option for you ")
   
     
     

   
   

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
   print("The distance from Seoul to Busan is approximately " + str(busan_distance) + " km and will take you around " + str(busan_time) + " hours to reach Busan")
elif destination == "2":
   print("The distance from Seoul to Gwangju is approximately " + str(Gwangju_distance) + " km and will take you around " + str(Gwangju_time) + " hours to reach Gwangju")
elif destination == "3":
   print("The distance from Seoul to Daegu is approximately " + str(Daegu_distance) + " km and will take you around " + str(Daegu_time) + " hours to reach Daegu")
else:
   print("Invalid destination choice.")
   
chosen_car = rent_car()

