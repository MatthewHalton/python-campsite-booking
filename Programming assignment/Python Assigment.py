# Imports
import datetime

# Store Accommodation Details - Card Fee, Weekday Discount, Per Day, VAT
myCottage = [4.40, 0.95, 200, 1.025]
myLogcabin = [2.00, 0.95, 90, 1.025]
myLargetent = [1.80, 0.95, 80, 1.025]
myMediumtent = [1.80, 0.95, 70, 1.025]
mySmalltent = [1.80, 0.10, 45, 1.025]

# Ask how many days they want to stay
print("Welcome to Camping Resort")
daysOption = int(input("How many days would you like to stay? 7/14\nOption: "))
tdelta = datetime.timedelta(days=daysOption)

# Take a date that their stay will start
year = int(input("What year is your stay taking place in? (2021): "))
month = int(input("What month do you want to stay? (4): "))
day = int(input("What day of the month do you want to stay? (15): "))
startDate = datetime.date(year, month, day)
endDate = startDate + tdelta
print(f"Start Date: {startDate}\nEnd Date: {endDate}")





# Calculate Price

               
if daysOption == 7:
    weekendPrice = myCottage[2] * 2
    print(f"Weekend Price: £{weekendPrice}")
        
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
        
    FinalTotal = (initialTotal + cottage[0]) * myCottage[3]
    print(f"Final Cost: £{FinalTotal}")
elif daysOption == 14:
    weekdayDiscount = (myCottage[2] * 10) * myCottage[1]
    print(f"Weekday Price: £{weekdayDiscount}")
    
    weekendPrice = myCottage[2] * 4
    print(f"Weekend Price: £{weekendPrice}")
    
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
    
    FinalTotal = (initialTotal + myCottage[0]) * myCottage[3]
    print(f"Final Cost: £{FinalTotal}")



    if daysOption == 7:
        weekdayDiscount = (myLogcabin[2] * 5) * myLogcabin[1]
        print(f"Weekday Price: £{weekdayDiscount}")


   
    weekendPrice = myLogcabin[2] * 2
    print(f"Weekend Price: £{weekendPrice}")
        
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
        
    FinalTotal = (initialTotal + myLogcabin[0]) * myLogcabin[3]
    print(f"Final Cost: £{FinalTotal}")
elif daysOption == 14:
    weekdayDiscount = (myLogcabin[2] * 10) * myLogcabin[1]
    print(f"Weekday Price: £{weekdayDiscount}")
    
    weekendPrice = myLogcabin[2] * 4
    print(f"Weekend Price: £{weekendPrice}")
    
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
    
    FinalTotal = (initialTotal + myLogcabin[0]) * myLogcabin[3]
    print(f"Final Cost: £{FinalTotal}")


    if daysOption == 7:
        weekdayDiscount = (myLogcabin[2] * 5) * myLogcabin[1]
        print(f"Weekday Price: £{weekdayDiscount}")
    weekendPrice = myLargetent[2] * 2
    print(f"Weekend Price: £{weekendPrice}")
        
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
        
    FinalTotal = (initialTotal + myLargetent[0]) * myLargetent[3]
    print(f"Final Cost: £{FinalTotal}")
elif daysOption == 14:
    weekdayDiscount = (myLargetent[2] * 10) * myLargetent[1]
    print(f"Weekday Price: £{weekdayDiscount}")
    
    weekendPrice = myLargetent[2] * 4
    print(f"Weekend Price: £{weekendPrice}")
    
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
    
    FinalTotal = (initialTotal + myLogcabin[0]) * myLogcabin[3]
    print(f"Final Cost: £{FinalTotal}")


  if daysOption == 7:
    weekdayDiscount = (myLargetent[2] * 5) * myLargetent[1]
    print(f"Weekday Price: £{weekdayDiscount}")    
weekendPrice = myLargetent[2] * 2
print(f"Weekend Price: £{weekendPrice}")



    if daysOption == 7:
      weekdayDiscount = (myMediumtent[2] * 5) * myMediumtent[1]
        print(f"Weekday Price: £{weekdayDiscount}")
        
    weekendPrice = myMediumtent[2] * 2
    print(f"Weekend Price: £{weekendPrice}")
        
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
        
    FinalTotal = (initialTotal + myMediumtent[0]) * myMediumtent[3]
    print(f"Final Cost: £{FinalTotal}")
elif daysOption == 14:
    weekdayDiscount = (myMediumtent[2] * 10) * myMediumtent[1]
    print(f"Weekday Price: £{weekdayDiscount}")
    
    weekendPrice = myMediumtent[2] * 4
    print(f"Weekend Price: £{weekendPrice}")
    
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
    
    FinalTotal = (initialTotal + myLogcabin[0]) * myLogcabin[3]
    print(f"Final Cost: £{FinalTotal}")

   if daysOption == 7:
      weekdayDiscount = (mySmalltent[2] * 5) * mySmalltent[1]
        print(f"Weekday Price: £{weekdayDiscount}") 

       
    weekendPrice = mySmalltent[2] * 2
    print(f"Weekend Price: £{weekendPrice}")
        
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
        
    FinalTotal = (initialTotal + myMediumtent[0]) * myMediumtent[3]
    print(f"Final Cost: £{FinalTotal}")
elif daysOption == 14:
    weekdayDiscount = (myMediumtent[2] * 10) * myMediumtent[1]
    print(f"Weekday Price: £{weekdayDiscount}")
    
    weekendPrice = myMediumtent[2] * 4
    print(f"Weekend Price: £{weekendPrice}")
    
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
    
    FinalTotal = (initialTotal + myLogcabin[0]) * myLogcabin[3]
    print(f"Final Cost: £{FinalTotal}")


# Allow the user to chose accomodation               
accomChoice = print("What accomodation would you like to stay in?")
UserChoice =input("1 - Cottage\n2 - Log Cabin\n3 - Large Tent\n4 - Medium Tent\n5 - Small Tent\nOption: ") 

if UserChoice == "1":
    OurCost = calculate_cost(myCottage, DaysOption)
elif UserChoice == "2":
    OurCost = calculate_cost(myLogcabin, Daysoption)
elif UserChoice == "3":
    OurCost = calculate_cost(myLargetent, Daysoption)
elif UserChoice == "4":
    OurCost = calculate_cost (myMediumtent, Daysoption)
elif Userchoice == "5":
    OurCost = calculate_cost (mySmalltent, Daysoption)
 
#Booking details


    print("Extra details required")
    Fname = input("Enter full name:)
    num = input("Enter contact number:))
    booking = [Fname, num, "£{:.2f}".format(FinalCost)]
    myFile = open("bookingsheet")
    myFile.write(f"{x} - ")
    myFile.close()
