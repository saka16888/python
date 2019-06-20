# mealCost=float(input().strip())
# taxPercent=float(input().strip())
# tipPercent=float(input().strip())

mealCost=23.50
taxPercent=9.25
tipPercent=15

totalCost = int (round(mealCost * (1.0 + (taxPercent+tipPercent) / 100)))
print('The total meal cost is ',totalCost,' dollars')