from urllib.request import urlopen
import requests


ActualUrl = "https://money.cnn.com/quote/quote.html?symb=CHANGE"

def findPrice(stock):
    url = ActualUrl #created for the changed that will happen to Url later.

    url = url.replace("CHANGE", stock)

    page = requests.get(url)

    priceIndex = page.text.find('"BatsUS">') + 9 # nine is a constant to get to the number
    endPriceIndex = page.text[priceIndex:priceIndex+20].find("</")
    stockPrice = page.text[priceIndex:priceIndex+endPriceIndex]

    return stockPrice


def main():
    stock = input("choose a stock to track: ")
    print(findPrice(stock))

if __name__=="__main__":
    main()