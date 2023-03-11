# Write your solution here
gift=int(input("Value of gift:"))
tax=0
if gift < 5001:
    print("No tax!")
elif gift < 25001:
    tax=100+(gift-5000)*0.08
elif gift < 55001:
    tax=1700+(gift-25000)*0.1
elif gift < 200001:
    tax=4700+(gift-55000)*0.12
elif gift < 1000001:
    tax=22100+(gift-200000)*0.15
elif gift > 1000000:
    tax=142100+(gift-1000000)*0.17
if tax!=0:
    print(f"Amount of tax: {tax} euros")