
clientList = []


print("Welcome to the User Database\n","--------------------")

while(1):# only breaks once choice 4 is chosen
  print("1. Add User")
  print("2. Remove User")
  print("3. Display Users")
  print("4. Exit")
  print("---------------------")
  choice = input("please one of the following options: ")
  
  

  if choice == "1": # user adding option

     while(1):
       print("Current List:", clientList) 
       print("\n")

       name = input("Enter the new user's name:  ")
       print("\n")
       count2 = 0
       for i in range(len(clientList)):
          if clientList[i] == name:
           print("this name is already listed, please try another, \n")
           count2 = 2
           break
       if count2 == 0:
            clientList.append(name)
            print("User Added")
            print("Updated List: ")
            print(clientList,"\n")
            break
        #breaks the while loop that checks if client answered correct


  elif choice == "2" and len(clientList) == 0:
    print("you can't remove when the list is empty, try another choice\n")

  elif choice == "2":
      x = 1
      print(clientList)
      while(1):
        name = input("Enter the name of the user to be removed: ")
        print("\n")
        for i in range(len(clientList)):
          
            if clientList[i] == name:
              (clientList.pop(i))
              print("Updated List: ")
              print(clientList, "\n")
              x = 0
              break

        if x == 1:
            print("this name is not in the data base, please enter another user, ")
        else :
          break

  elif choice == "3":
    print("current list:")
    print(clientList,"\n")
        
  elif choice == "4":
    print("have a nice day")
    break

  else:
    print("You have entered an invalid choice. Please pick again.\n")



      





     











  