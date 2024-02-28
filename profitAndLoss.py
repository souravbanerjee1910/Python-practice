sellingPrice = int(input("enter selling price :-"))
costPrice = int(input("enter cost price :-"))

isProfit=sellingPrice-costPrice

if(sellingPrice>costPrice):
    print("Congo You have made profit of rupees :- ",isProfit)
elif(sellingPrice==costPrice):
    print("You have No profit ")
else:print("you have made loss of rupees :-",isProfit)
    