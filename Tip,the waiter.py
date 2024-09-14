def tipCalc (b,tipPerc):
    total = bill*0.01*tipPerc
    return total     

bill = int(input("Enter your Bill:"))
tipPercentage = int(input("Enter your Tip Percentage:"))

res = tipCalc(bill,tipPercentage)
print(f"Bill : {bill}")
print(f"tip : {tipPercentage}%")
print(f"Total : {bill+res}")



def cube(n):

return n**3

num = 55

cb = cube(num)

print(f"Cube of {num} = {cb}")            