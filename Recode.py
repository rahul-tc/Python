#Wap to display a person name age address
Name = input("Enter the name : ")
Age = int(input("Enter the age: "))
Address = input("Enter the address: ")
print(Name)
print(Age)
print(Address)

########################################################
ABT = CALCULATE(AVERAGE(RidersTable[Confirmation Time]),RidersTable[Confirmed]="Yes")
ANCT = CALCULATE(AVERAGE(RidersTable[Confirmation Time]),RidersTable[Confirmed]="no")
Avg Confirmation Time = AVERAGE(RidersTable[Confirmation Time])
Confirmed Ride% = DIVIDE(CALCULATE(COUNTROWS(RidersTable),RidersTable[Confirmed]="Yes"),[Total Rides])
Confirmed Rides = CALCULATE(COUNTROWS(RidersTable),RidersTable[Confirmed]="Yes")
Overall ABT = CALCULATE(AVERAGE(RidersTable[Confirmation Time]),ALL(RidersTable[ZScore Category]), RidersTable[Confirmed]="Yes")
Overall ANCT = CALCULATE(AVERAGE(RidersTable[Confirmation Time]),ALL(RidersTable[ZScore Category]),ABS( RidersTable[Confirmed]="no"))
Total Rides = DISTINCTCOUNT(RidersTable[Ride ID])
UnConfirmed Ride% = DIVIDE(CALCULATE(COUNTROWS(RidersTable),RidersTable[Confirmed]="No"),[Total Rides])
Unconfirmed Rides = CALCULATE(COUNTROWS(RidersTable),RidersTable[Confirmed]="No")
