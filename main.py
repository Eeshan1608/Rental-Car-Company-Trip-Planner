# from typing import Sized


# print("Hello today we are gonna learn about Mental health")
# name = input("Enter your name: ")
# print("Hello " + name + "!")
# print("")
# print("Today we are gonna learn about Mental health")
# print("")
# print("")

# mental_health = input("What is Mental Health in your POV: ")
# print("Well there is no right or wrong answer to this question")
# print("")
# print("")
# print("Mental Health is basically the state of your mind and feelings you feel everyday")
# print("")
# print("")
# while True:
#   fun_fact = input("DO you want to know a sad fact yes or no: ").lower()

#   if fun_fact == "yes":  
#     print("Do you know that in South Korea every 40 min a person commits suicide and in UK every 90 mins a person commits suicide")
#     break
#   elif fun_fact == "no":
#     print("Okay")
#     break
#   else:
#     print("Please enter a valid answer") 

# print("")

# while  True:
#   feeling = input("How are you feeling today? good/okay/bad:  ").lower()

#   if feeling == "good": 
#      print("That's great to hear!")
#      break
#   elif feeling == "okay":
#      print("That's okay, it's not that bad.")
#      break
    
#   elif feeling == "bad":
#      print("Sorry to hear that.")
#      break
#   else:
#     print("Enter proper answer.") 


# print("")
# print("")
# print("")

# print("PEER PRESSURE AND ACADEMIC PRESSURE ARE ONE OF THE LEADING CAUSES OF MENTAL HEALTH ISSUES")

# while True:
#   peer_pressure = input("Do you agree? yes/no: ").lower()

#   if peer_pressure == "yes":
#     print("I agree with you")
#     break

#   elif peer_pressure == "no":
#     why = input("WHY do you think so?: ")
#     print("Okay")
#     break

#   else:
#     print("Enter proper answer.")

# print("")
# print("")

# print("")

# def breathe():
#   exercise = input("Do you want to learn an exercise that is proven to help reduce mental health issues? yes or no: ").lower()

#   if exercise == "yes":
#       print("Take a deep breath in through your nose and exhale through your mouth")
#       while True:
#           print("Inhale")
#           print("Exhale")
#           stop = input("Do you want to stop? yes/no: ").lower()
#           if stop == "yes":
#               print("Thank you for TALKING remember to take care of your mental health")
#               break
#           elif stop == "no":
#               continue

#   elif exercise == "no":
#       print("Okay, maybe next time!")

# breathe()




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