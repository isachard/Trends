from urllib.request import urlopen
from bs4 import BeautifulSoup

try :
	data = BeautifulSoup(urlopen('https://www.covers.com/Sports/mlb/PrintSheetHtml?isPrevious=False'),'html.parser')
except :
	"URL"


oddTable = data.findAll('tr',attrs={'class': "trBackGround"})
evenTable= data.findAll('tr',attrs={'class': ""})

trends =[]
def parsingTable(table):
	for i in table:
		lista =  i.text.split()[:]
		if len(lista) == 17 :
			trends.append(lista)


parsingTable(oddTable)
parsingTable(evenTable)

"""

def MoneylineTrends(self,name, trend):
		return moneyline.append(name + trend)

def getTotalTrends(name, trend):
	total.append(name + trend)"""