total=0
count=int(input("How many expenses?"))
for i in range(count):
    expense=float(input("Enter expenses:"))
    total=total+expense

print("Total Spents:",total)