mealCost=float(input().strip())
taxPercent=float(input().strip())
tipPercent=float(input().strip())

totalCost = int (round(mealCost * (1.0 + (taxPercent+tipPercent) / 100)))
print('The total meal cost is ',totalCost,' dollars')