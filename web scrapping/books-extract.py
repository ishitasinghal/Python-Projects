from bs4 import BeautifulSoup
import requests

#for all addresses
addresses = ["http://books.toscrape.com", "http://books.toscrape.com/catalogue/page-2.html"]
for address in addresses:
#website_address = "http://books.toscrape.com"
    data = requests.get(address)
    #print(data)


    soup = BeautifulSoup(data.text, "html.parser")
    #print(soup)

    books = soup.findAll("article", {"class":"product_pod"})
    #print(len(books))

    rating_dict = {
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }

    for book in books:
        rating = book.findAll("p")[0].get("class")[1]
        #print(rating)
        rating = rating_dict.get(rating, "Not found" )
        print(rating)

