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
                        print(x, check_in_info[x])
                        user_input_lol = input("Which animal would you like to check out? ")
                        for x in check_in_info:
                            if user_input_lol in check_in_info:
                                del x[user_input_lol]
                       
                 
    

            elif input1 == "7":
                   print("Goodbye")
                   break

            elif input1 == "4":
                    if len(check_in_info) < 1:
                        for i in range(0, len(check_in_info)):
                            most_urgent = [0]
                            if check_in_info[i]["urgency"] >= most_urgent[0]:
                                      most_urgent.append(check_in_info[i]["urgency"])
                        for item in range(0, len(most_urgent)):
                            print("Name - " + check_in_info[item]["name"])
                            print("Kind - " + check_in_info[item]["kind"])
                            print("Urgency - " + check_in_info[item]["urgency"])
                            continue

            elif input1 == "5":
                    for i in range(0, len(check_in_info)):
                            least_urgent = [0]
                            if check_in_info[i]["urgency"] <= least_urgent[0]:
                                least_urgent.append(check_in_info[i]["urgency"])
                    for item in range(0, len(least_urgent)):
                        print("Name - " + check_in_info[item]["name"])
                        print("Kind - " + check_in_info[item]["kind"])
                        print("Urgency - " + check_in_info[item]["urgency"])
                        continue

             
            elif input1 == "3":
                if (len(check_in_info) > 0):
                    print("ALL ANIMALS CHECKED IN")
                    print_list(check_in_info)
                else:
                    print("No pets yet!")

           
            elif input1 == "6":
                    find_name = input("what is the name: ")
                    for item in check_in_info:
                        if find_name in item:
                            print(item)
                           

pawsome_pet_vet()

