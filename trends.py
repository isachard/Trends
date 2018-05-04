import url as table

def getMoneylineTrends(t):
	for i in t:
		moneyline.append(i[1] +" " + i[15])

def getTotalTrends(t):
	for i in t:
		total.append(i[1] +" " + i[16])



moneyline = []
total = []


getMoneylineTrends(table.trends)
getTotalTrends(table.trends)

print(moneyline)
print(total)