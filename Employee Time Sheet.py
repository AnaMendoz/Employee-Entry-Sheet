import datetime #Will display current time
print(datetime.datetime.now())

def get_employee(id): #Employee library by ID number
   if id == 1234:
       return "Jerry Yang, Employee:1234, Department:Design, Building:(A), Occupation:Manager, Priority:FULL Access"
   elif id == 2345:
       return "Filo David, Employee:2345, Department:Networking, Building:(B), Occupation:Supervisor, Priority:Security Building"
   elif id == 3456:
       return "Nola Juarez, Employee:3456, Department:N/A, Position:CEO"
   else:
       print("WANRNING 'Employee ID NOT FOUND' ")

def log(info, InOut): #This will create a file to log time for ID input
   currenttime = datetime.datetime.today()
   with open("logfile.txt", 'a') as file:
       file.write(str(currenttime) + " " + InOut + " " + info + "\n") #will write variable values on the file
       file.close()
   return currenttime

def log(info, inout):
   currentTime = datetime.datetime.now() #variable to use current time instead of string
   with open("logfile.txt", "a") as file:
       contents = str(currentTime) + " Clocked: " + inout + " " + info
       print(contents)
       file.write(contents + "\n")
       file.close()

   return currentTime

def getTime(id_number,outTime): #get the in and out time from the given ID
   with open("logfile.txt", "r") as file:
       #find the in time
       for line in file: #read file bottom up looking for the employee ID and In/Out
           #if line.find("Employee:"+info) and line.find("Clocked: in"): #If the ID number is within string, and the time is "in"
           if "Employee:"+id_number in line and "Clocked: in" in line:
               #get the user's in time
               lineList = line.split(" ")
               inTimeList = lineList[1].split(".")
               finalInTimeList = inTimeList[0].split(":")
               inTime = datetime.time(int(finalInTimeList[0]), int(finalInTimeList[1]), int(finalInTimeList[2]))  #inTime = datetime.time(14, 00, 00)

               #print(outTime)
               outList = str(outTime).split(" ")
               #print(outList)
               outTimeList = outList[1].split(".")
               #print(outTimeList)
               finalOutTimeList = outTimeList[0].split(":")
               #print(finalOutTimeList)
               outTime = datetime.time(int(finalOutTimeList[0]), int(finalOutTimeList[1]), int(finalOutTimeList[2]))  #inTime = datetime.time(14, 00, 00)

               #Do the calculation
               # Create datetime objects for each time (a and b)
               dateTimeA = datetime.datetime.combine(datetime.date.today(), inTime)
               dateTimeB = datetime.datetime.combine(datetime.date.today(), outTime)
               # Get the difference between datetimes (as timedelta)
               dateTimeDifference = dateTimeB - dateTimeA
               # Divide difference in seconds by number of seconds in hour (3600)
               dateTimeDifferenceInHours = dateTimeDifference.total_seconds() / 3600
               print(dateTimeDifferenceInHours)
               break

while True: #while loop to continue to ask new users' input
   print("A&A Company")
   print("Welcome! ", "Please, Enter Employee ID Number: ")
   id_number = input()

   print("Are you logging in or out?")
   inout = input()

   info = get_employee(int(id_number))
   print(info)

   currentTime = log(info, inout)

   if inout == "out" or inout == "Out":#either out or Out will be identified and read by Python
       getTime(id_number,currentTime)

   print("You're Clocked " + inout)#Will display whats in quotes plus the variable inout
