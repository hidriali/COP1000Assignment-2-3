# Furniture.py.
#This program calculates profits and sales prices for a furniture company.
#input:
#assign values to to vairables: itemNmae, retailPrice, and wholsalePrice.
itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
#Write your assignment statements here for profit, salePrice, and saleProfit
profit = retailPrice - wholesalePrice
salePrice= retailPrice - (retailPrice * 0.25)
saleProfit= salePrice - wholesalePrice
#output:
#dispaly Item name: TV stand, retail price: $325, wholesale price:$200.
#Last, Calculate the values of profit, salePrice, and saleProfit; and disply them. 
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))
