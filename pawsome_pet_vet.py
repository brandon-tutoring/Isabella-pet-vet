def print_list(list_of_animals):
       counter = 1;
       for item in list_of_animals:
               print(counter, ") Name: ", item["name"], " Species: ", item["kind"])
               counter+=1

def pawsome_pet_vet():

   import time 
   print("Welcome to pawsome pet vet!")
   time.sleep(2)
   check_in_info = []


   while True:
           input1 = input("Would you like to: \n1)check in \n2)check out \n3)show all by name \n4)show all by most urgent \n5)show all by least urgent \n6)find by name \n7)quit?\n")

           if input1 == "1":
                  name_input = input("what is the name: ")
                  kind_input = input("what is the species: ")
                  while True:
                      urgency_input = input("what is the urgency level: ")
                      if (urgency_input.isdigit()):
                          urgency_input = int(urgency_input)
                          check_in_info.append({"name": name_input, "kind": kind_input, "urgency": urgency_input})
                          break;
                      else:
                          print("That is not a valid number!  Try again")
                          print(check_in_info)

           elif input1 == "2":
                  for x in range(0, len(check_in_info)):
                       print_list(check_in_info)
                       user_input_lol = input("Which animal would you like to check out? ")
                       check_in_info["name"].delete(user_input_lol)





           elif input1 == "7":
                  print("Goodbye")
                  break

           elif input1 == "5":
                  if len(check_in_info) > 0:
                      for i in range(0, len(check_in_info)):
                          most_urgent = [0]
                          if check_in_info[i]["urgency"] >= most_urgent[0]:
                              most_urgent.append(check_in_info[i]["urgency"])
                              print("Name - " + check_in_info[i]["name"])
                              print("Kind - " + check_in_info[i]["kind"])
                              print(check_in_info[i]["urgency"])
                  else:
                      print("Sorry there are no pets checked in a this time")



           elif input1 == "4":
                  if len(check_in_info) > 0:
                      for i in range(0, len(check_in_info)):
                          least_urgent = [100000]
                          if check_in_info[i]["urgency"] <= least_urgent[0]:
                              least_urgent.append(check_in_info[i]["urgency"])
                              print("Name - " + check_in_info[i-1]["name"])
                              print("Kind - " + check_in_info[i-1]["kind"])
                              print(check_in_info[i-1]["urgency"])
                  else:
                      print("Sorry there are no pets checked in a this time")




           elif input1 == "3":
               if (len(check_in_info) > 0):
                   print("ALL ANIMALS CHECKED IN")
                   print_list(check_in_info)
               else:
                   print("No pets yet!")


           elif input1 == "6":
                   find_name = input("what is the name: ")
                   for i in range(0, len(check_in_info)):
                           if find_name in check_in_info[i]["name"]:
                               print("Name - " + check_in_info[i]["name"])
                               print("Kind - " + check_in_info[i]["kind"])
                               print (check_in_info[i]["urgency"])

                           else:
                               print("that animal is not checked in")


pawsome_pet_vet()
