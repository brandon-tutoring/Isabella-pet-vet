import time 

def print_list(list_of_animals):
       counter = 0;
       for item in list_of_animals:
               print(counter, ") Name: ", item["name"], " Species: ", item["kind"])
               counter+=1

def pawsome_pet_vet():

   print("Welcome to pawsome pet vet!")
   check_in_info = []
   animals_we_take = ["dog", "cat"]


   while True:
           input1 = input("Would you like to: \n1)check in \n2)check out \n3)show all by name \n4)show all by most urgent \n5)show all by least urgent \n6)find by name \n7)quit?\n")

           if input1 == "1":
                  name_input = input("what is the name: ").strip()
                  kind_input = input("what is the species: ").strip().lower()
                  if kind_input not in animals_we_take:
                      print("sorry, we do not accept that animal")
                      continue
                  while True:
                      urgency_input = input("what is the urgency level: ")
                      if (urgency_input.isdigit()):
                          urgency_input = int(urgency_input)
                          check_in_info.append({"name": name_input, "kind": kind_input, "urgency": urgency_input})
                          break;
                      else:
                          print("That is not a valid number!  Try again")

           elif input1 == "2":
                  if len(check_in_info) == 0:
                      print("No animals yet!")
                      continue
                  print_list(check_in_info)
                  check_out = input("Which animal would you like to check out? ")
                  if not (check_out.isdigit()):
                      print("That is not a number")
                      continue
                    
                  check_out = int(check_out)

                  if check_out >= len(check_in_info):
                      print("That number is too big")
                      continue

                  check_in_info.pop(check_out)




           elif input1 == "3":
               if (len(check_in_info) > 0):
                   print("ALL ANIMALS CHECKED IN")
                   print_list(check_in_info)
               else:
                   print("No pets yet!")



           elif input1 == "4":
                   if len(check_in_info) == 0:
                       print("Sorry there are no pets checked in a this time")
                   elif len(check_in_info) == 1:
                       print_pet(check_in_info[0])
                   else:
                       most_urgent = [check_in_info[0]]
                       for i in range(1, len(check_in_info)):
                           if check_in_info[i]["urgency"] < most_urgent[0]["urgency"]:
                               continue
                           elif check_in_info[i]["urgency"] == most_urgent[0]["urgency"]:
                               most_urgent.append(check_in_info[i])
                           elif check_in_info[i]["urgency"] > most_urgent[0]["urgency"]:
                               most_urgent = check_in_info[i]
                               for animal in most_urgent:
                                   print_pet(animal)


           elif input1 == "5":
                  if len(check_in_info) > 0:
                      for i in range(0, len(check_in_info)):
                          least_urgent = [0]
                          if check_in_info[i]["urgency"] >= least_urgent[0]:
                              least_urgent.append(check_in_info[i]["urgency"])
                              print("Name - " + check_in_info[i]["name"])
                              print("Kind - " + check_in_info[i]["kind"])
                              print(check_in_info[i]["urgency"])
                  else:
                      print("Sorry there are no pets checked in at this time")



           


           elif input1 == "6":
                   if len(check_in_info) > 0:
                       find_name = input("what is the name: ")
                       for i in range(0, len(check_in_info)):
                           if find_name in check_in_info[i]["name"]:
                               print("Name - " + check_in_info[i]["name"])
                               print("Kind - " + check_in_info[i]["kind"])
                               print (check_in_info[i]["urgency"])

                       else:
                           print("that animal is not checked in")
                   else:
                        print("No animals yet!")



           elif input1 == "7":
                  print("Goodbye")
                  break


pawsome_pet_vet()
