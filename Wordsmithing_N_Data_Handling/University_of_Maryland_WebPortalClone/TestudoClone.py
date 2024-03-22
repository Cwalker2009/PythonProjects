Students = {
  122400783: "Billy Marsh",#sets key in student dictionary to 122400783 and value to Billy Marsh
  122400785: "Robby Rotten",#sets key in student dictionary to 122400785 and value to Robby Rotten
  122400789: "Rosita Green"#sets key in student dictionary to 122400783 and value to Rosita Green
}

Balance = {
  122400783: 1600.67,#sets key in Balance dictionary to 122400783 and value to 1600.67 which serves as the student's balance
  122400785: 5.39,#sets key in Balance dictionary to 122400785 and value to 5.39 which serves as the student's balance
  122400789: 80.89#sets key in Balance dictionary to 122400789 and value to 80.89 which serves as the student's balance
}

Courses = {
  122400783: ["CMSC125", "ENES100", "UNIV100"],#sets key in Courses dictionary to 122400783 and value to list of courses student is enrolled in
  122400785: ["MUSC100", "CMSC351", "UNIV100"],#sets key in Courses dictionary to 122400785 and value to list of courses student is enrolled in
  122400789: ["ART200", "ENES100"]#sets key in Courses dictionary to 122400789 and value to list of courses student is enrolled in
}

def Billing(id, balance):#defines billing function the parameters are the students UID which is the key and balance is the dictionary to be called

  print("Welcome,", Students[id] + "!")#prints welcome message for student
  i = 0#sets i as counter
  while i == 0:#creates an infinite loop since i always = 0 and runs nested code
    bal = balance[id]#creates variable bal and sets it to the student's balance
    print("\noptions:\nSee Balance,\nAdd To Balance\nPay Balance\nReturn Home")#displays options for student to choose from
    option = input("Please enter an option here: ")#input command based on options diplayed
    option = option.lower()#makes every input in option lowercase to avoid errors
    if option == "see balance":
      #if the user enters "see balance" the code will output the students balance using data from balance dictionary
      print("you have a balance of $", bal)
    elif option == "add to balance":
      #else if the student inputs "add to balance" the code will ask how much they want to add, take that input and turn it into a float and then add that to total value in the dictionary that corresponds to the key and print it out for user to see the change made
      add = float(input("How much would you like to add: "))
      print("your new balance is " + "$", bal + add)
      bal = bal + add
      balance[id] = bal#sets balance in dictionary to be calculated bal
    elif option == "pay balance":
      #else if the student inputs "pay balance" the code will ask how much they want to pay, take that input and turn it into a float and then subtract that from the total balance value in the dictionary that corresponds to the key and print it out for user to see the change made
      sub = float(input("how much would you like to pay: "))
      bal = bal - sub
      print("your new balance is $", (bal))
      balance[id] = bal#sets balance in dictionary to be calculated bal
      if bal < 0:
        #Checks if the balance remaining after value is subtracted is zero and then prints out refund amount
        print("You will get a refund of $", (0 - bal))#since the value in balance will be negative I will subtract it from 0 because a negative minus a negative is a positive so that I can print out a positive value for refund amt to avoid confusion
    elif option == "return home":
      #If user inputs return home option the code will return the user back to the globally function options but will first print "Returning to homescreen"
      print("Returning to homescreen...\n")
      return
    else:
      #if option does not exist the code will print 'try again'
      print("try Again.")


def AddrChan():#Defines address function
  while True:#creates an infinite loop that runs neested code
    print("\nEnter new address or press Cancel")#displays user options for the address change function
    addr = input("Type here: ")#takes address input
    addr = addr.upper()#makes address string uppercase
    if addr == "CANCEL":
      #if the user enters "CANCEL" the code will take the user back to globally function options and notify them they are returning to home screen
      print("Returning to homescreen...\n")
      return 
    else:
      #If the user does not enter cancel whatever they inputed for addr will be their new address
      print("Your new address is: ", addr)
  


def addCourse(id,CourDict,balDict):#defines add course functions and takes the student ID which is the key as a parameter, and takes the course dictionary as another parameter and the balance dictionary as the final parameter 
  print("Welcome", Students[id],"to ADD COURSE"  )#displays welcome message that prints student's name
  while True:#infinite loop will always run nested code
    print("\nOptions: \nSee Current Courses \nAdd Course \nReturn Home")#displays options
    options = input("Type here: ")#asks user to make an input based on the displayed options
    options = options.lower()#makes user input lowercase
    if options == "see current courses":
      #if user enters "see current courses" will display all course values based on key
      for course in CourDict[id]:
        #loops through elements in the list for corresponding dictionary and displays thouse courses
        print(course)
    elif options == "add course":
      #if user enters "add course" option the code will ask for name of course as input(crse), then asks if user is an in or out of state student then takes an input of the amt of credits in course and then calculates cost based on whether they are instate or out of state then adds that to the value of the course dictionary that corresponds to the ID and then adds the amt to the balance dictionary for corresponding ID then  prints the course that was added and the new balance
      crse = input("What course would you like to add: ")
      crse = crse.upper()#makes course input uppercase
      print("If in state enter 'IN' if out of state 'OUT' ")
      state = input("type here: ")#asks for input in/out state
      state = state.lower()#makes input lowercase
      if state == "in":
        cost = 374#sets cost for instate
      elif state == "out":
        cost = 1529 #sets cost for out state
      credit = int(input("Please only enter numbers \nHow many credits is the course: "))#asks for credit input
      CourDict[id].append(crse)#adds course to course dictionary as a value for corresponding student id
      print(crse,"was added to your courses!")
      bal = balDict[id]#sets bal value to value in balance dictionary for corresponding student ID
      tot = (credit*cost)#calculates total bu multiplying num of credits times the cost for credit(determined by resident status)
      balDict[id] = bal+tot#adds balance to balance dictionary as a value for corresponding student id
      print("your balance is now $", balDict[id])
    elif options == "return home":
      print("Returning to homescreen...\n")#prints msg letting user know they are returning to globally function
      return#returns back to globally function options
  

def Unenroll(id,CourDict):#defines unenroll function and takes the student ID, course dictionary as parameters
  while True:#set infinite loop so that nested code is always ran
    print("Options:\nUnenroll\nCancel")#displays user options for this function
    option = input("Type here: ")#takes user input
    option = option.lower()#makes user input lowercase
    if option == "unenroll":
      #if user enters "unenroll" as option it will verify whether they really want to unenroll or cancel by taking another input
      verify = input("Enter 'y' if you sure you want to unenroll or 'n' to cancel: ")
      verify = verify.upper()#makes verify input uppercase
      if verify == "Y":
        #if they enter "y" the code will count that as user verifying that they want to unenroll and it will remove them from the course dictionary, balance dictionary and student dictionary based on the student's id
        CourDict.pop(id)
        print("You have been unenrolled from this institution")
        return
        #lets user know they have been unenrolled and returns them home
      elif verify == "N":
        #if user enters "n" shows they do not want to unenroll and does not unenroll the student but instead sends them back to options b/c infinite loop while letting them no they are not unenrolled
        print("Okay we will not unenroll you.")
    elif option == "cancel":
      #if user enters "cancel" the code will send the user back to globally function options and let them know they are returning to home screen
      print("Returning to homescreen...\n")
      return
        
          


def Quit(Dict):#defines quit function 
  print("Logging out...\n")#notifies user they are being logged out
  return globally(Dict)#returns user to start of globally function


def globally(Dict):
  i = 0#counter that sets counter to 0
  print("Howdy! What a beautiful day!")#displays welcome message for user
  while i == 0:#runs nested code while i is set to 0
    UserName = input("Name: ")#takes username as an input
    UID = (input("ID: "))#takes uid as an input
    try:
      int(UID)#checks if user UID is an int
    except:
      print("Please only enter valid ID numbers!")#if user uid is not an int prints please only enter valid id numbers
    UID = int(UID)#turns uid into int
    check = False#sets a bool check to false
    for k in Dict:
      #loops through keys in the student dictionary and checks if the UID matches any of the keys in the student dictionary then it checks if the key value equals the username and if it does it sets "check" bool to true
      if UID == k:
        if Dict[k] == UserName:
          check = True
    if check:
      #if the check bool is true the code will increment the counter to 1 which officially breaks the infinite while loop that asks the user to input their name and ID, and the code will print "log in success"
      i = i + 1
      print("Log In Success!")
    else:
      #if the key for the student dictionary which is the UID input and the UserName which is the key value for the student dictionary does not match the code will print try again
      print("Try Again.")

  while True:#infinite loop runs the nested code
    print("\nSelect an Option: \nBilling\nAddress Change\nAdd A Course\nUnenroll\nQuit")#displays user options
    option = input("Type Here: ")#asks user for input based on displayed option
    option = option.lower()#turns user input str into lowercase
    if option == "billing":
      #if user input is billing calls Billing function and set parameters to the student's UID input and the Balance dictionary
      Billing(UID, Balance)
    elif option == "address change":
      #if user input is address change calls AddrChan function 
      AddrChan()
    elif option == "add a course":
      #if user input is "add a course" calls "addCourse" function and set parameters to the student's UID input, The course dictionary, and the Balance dictionary
        if k not in Courses:  
          #if student id is not in course dictionary they are not a student, code prints cannot add a course
          print("You Are not Enrolled as a student therefore you cannot add a course ")
        else:
          addCourse(UID,Courses,Balance)
    elif option == "unenroll":
      #if user input is "unenroll", calls Unenroll function and sets parameters to the student's UID, and Course dictionary
      Unenroll(UID,Courses)
    elif option == "quit":
      #if user input is "quit" calls Quit function and set parameters to null Dict
      Quit(Dict)
    else:
      #if usser input does not match any of the displayed options prints "try again"
      print("Try Again.")


globally(Students)#since python runs line by line globally must be called last 
