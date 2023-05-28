# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? : $"))
# tip = int(input("What percent of tip you would like to give? 10, 12, 15? : "))
# people = int(input("Between how many people do the bill should be divided : "))

# tip_amount = (bill * tip) / 100
# total_bill = bill + tip_amount
# bill_per_person = round(total_bill/people, 2)

# print(f"Total bill is {total_bill}, with each should contribute about ${bill_per_person}")

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill : $"))
tip = int(input("What percent of tip you like to give? 10, 12 or 15 : "))
people = int(input("How many pople to split the bill between : "))

tip_amount = (bill*tip)/100
total_bill = bill + tip_amount
bill_per_person = round(total_bill/people, 2)

print(f"Total bill is ${total_bill}, with each should contribute about ${bill_per_person}")