# import datetime
# print(datetime)

# import datetime
# print(datetime.datetime.now())
#
# employee_list = ["'1234', '2345'"]
#
# input_string = input("Please, Enter Employee ID Number: ")
# employee_list = input_string("")
# print(employee_list)
#
# def fun():
#     print("1234,Joan, building C")
#     print("Jose, building A")
# fun()
# # #
# import datetime
# print(datetime.datetime.now())
# #
# # start = time.clock()
# # stop = (time.clock() - start)
#
# print("A&A Company")
# print("Welcome! ", "Please, Enter Employee ID Number: ")
#
# id_number = input()
# print("Jerry Yang, Employee:1234, Department:Design, Building:(A), Occupation:Manager, Priority:FULL Access")
# print("ID Found")
#
# print("Welcome! ", "Please, Enter Employee ID Number: ")
#
# id_number1 = input()
# print("Filo David, Employee:2345, Department:Networking, Building:(B), Occupation:Supervisor, Priority:Security Building Only")
# print("ID Found")


# if id_number == id_number:
#     # print(id_number)
#     # print(id_number1)
# print("ID Found")
# else:
#     print("ID Not Found, Please Speak to your Administrator! ")
# #
# if id == id_number1:
#     print(id_number1)
# else:
#     print("ID Not Found, Please Speak to your Administrator! ")

# def employee_number(Jerry Yang 3456 Design(A) Manager FULL):
# # print(ID)
#
# ID = employee_number(input())
# print(ID)

# import datetime
# print(datetime.datetime.today())
#
# def get_employee(id):
#     if id == 1234:
#        # print("im running")
#         return "Jerry Yang, Employee:1234, Department:Design, Building:(A), Occupation:Manager, Priority:FULL Access"
#     elif id == 2345:
#         return "Filo David, Employee:2345, Department:Networking, Building:(B), Occupation:Supervisor, Priority:Security Building"
#     elif id == 3456:
#         return "Nola Juarez, Employee:3456, Department:ALL, Position:CEO"
#     else:
#         print("WARNING 'Employee ID Not Found' ")
#
# def log(info, InOut):
#     currenttime = datetime.datetime.today()
#     with open("logfile.txt", 'a') as file:
#         file.write(str(currenttime) + " " + InOut + " " + info + "\n")
#         file.close()
#     return currenttime
#
# def get_time(info, OutTime):
#     f = open("logfile.txt", "r")
#     for line in f:
#         if "Employee:"+id_number in line and "InOut" in line:
#             #Will get employee 'in' time
#             lineList = line.split(" ")
#             inTimeList = lineList[1].split(".")
#             FinalinTimeList = inTimeList[0].split(":")
#             inTime = datetime.time(int(FinalinTimeList[0])), int(FinalinTimeList[2]) #intime = datetime.time(12, 00, 00)
#
#             OutofList = str(OutTime).split(" ")#print(outTime)
#             OutTimeList = OutofList[1].split(".")#print(outofList)
#             FinalOutTimeList = OutTimeList[0].split(":")#print(finalouttimeList)
#             OutTime = datetime.time(int(FinalOutTimeList[0]), int(FinalOutTimeList[1]), int(FinalOutTimeList[2]))#intime = datetime.time(12, 00, 00)
#
#             #Execute Calculation (Time worked)
#             #Create datetime objects for each time (A and B)
#             DateTimeA = datetime.datetime.combine(datetime.date.today(), inTime)
#             DateTimeB = datetime.datetime.combine(datetime.date.today(), OutTime)
#             DateTimeADiff = DateTimeB - DateTimeA #Will get difference between datetimes (as timedelta)
#             DateTimeDifferenceHours = DateTimeADiff.total_seconds() / 3600
#             print(DateTimeDifferenceHours)
#             break

    #     print(line)
    # f.close()
    #
    # start = datetime.today().time()
    # datetimeDiff = end - start
    # end = currenttime
    #
    # print(start)
    # print(end)
    # print(datetime.combine(datetime.min, end) - (datetime.date, start))


#This will create datetime objects for each time (InOutA and InOutB)
# InOutA = datetime.datetime.combine(datetime.date.today(), InTime)
# InOutB = datetime.datetime.combine(datetime.date.today(), OutTime)

# #This will get difference between datetimes
# datetimeDiff = InOutA - InOutB
#
# #This will divide differece in seconds by number of seconds in a hour (3600)
# #I have to find the total seconds worked in order to devide by seconds in a hour
# datetimeDiffHours = datetimeDiff.info()/3600

# while True:
#     print("A&A Company")
#     print("Welcome! ", "Please, Enter Employee ID Number: ")
#
#     id_number = input()
#     print("Do You Wish to Clock In or Out?")
#     InOut = input()
#     info = get_employee(int(id_number))
#     print(info)
#
#     CurrentTime = log(info, InOut)
#
#     if InOut == "Out" or InOut == "out":
#         get_time(info, CurrentTime)
#
#     print("You Are Successfully Logged! Have a Nice Day!! ^_^")
#
# # for line in file:
# #     if "Employee ID Number" and  "InOut":
#
# if "Employee:" + "ID Number" in line  and "InOut" in line:
#     lineList = line.split(" ") Date_Time_Employee_Name
#     List([Date], [Time], [Emploee], [Name])
#     print(List[2])
#
#     lineList[1]
#     time = lineList[1].split(".")
#     finaltime = in time.split(".")
#     finaltime = ([0], [1], [2])
#     intime =  datetime.time(int(finaltime[0], int([1], [2], [3])))
