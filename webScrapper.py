from urllib.request import urlopen
import requests

url = "https://money.cnn.com/quote/quote.html?symb=CHANGE"
stock = input("choose a stock to track: ")
url = url.replace("CHANGE", stock)
print(url)

page = requests.get(url)

priceIndex = page.text.find('"BatsUS">') + 9 # nine is a constant to get to the number
endPriceIndex = page.text[priceIndex:priceIndex+20].find("</")
stockPrice = page.text[priceIndex:priceIndex+endPriceIndex]

print(stock + "\n" + "Price is: " + stockPrice)