# Imports
import datetime

# Store Accommodation Details - Card Fee, Weekday Discount, Per Day, VAT
myCottage = [4.40, 0.95, 200, 1.025]

# Ask how many days they want to stay
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
    weekdayDiscount = (myCottage[2] * 5) * myCottage[1]
    print(f"Weekday Price: £{weekdayDiscount}")

    weekendPrice = myCottage[2] * 2
    print(f"Weekend Price: £{weekendPrice}")
        
    initialTotal = weekdayDiscount + weekendPrice
    print(f"Price before VAT and Card: £{initialTotal}")
        
    FinalTotal = (initialTotal + myCottage[0]) * myCottage[3]
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






