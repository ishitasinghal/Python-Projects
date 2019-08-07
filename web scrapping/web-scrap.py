# from bs4 import BeautifulSoup
# import requests
#
# website_address = "http://quotes.toscrape.com"
# result = requests.get(website_address)
# print(result)
# #Request-200 means ran successfully
#
#
#
#
# soup = BeautifulSoup(result.text, "html.parser")
# #print(soup)
#
# quotes_list = soup.findAll("div",{"class":"quote"})
# #print(quotes_list)


#####do not touch upar vala code#####


from bs4 import BeautifulSoup
import requests

website_address = "http://quotes.toscrape.com"
result = requests.get(website_address)
#print(result)

soup = BeautifulSoup(result.text, "html.parser")
#print(soup)

# single_quotation = soup.find("div",{"class":"quote"})
# #print(single_quotation)
#
# quotation = single_quotation.find("span",{"class":"text"})
# print(quotation.text)
#
# author = single_quotation.find("small",{"class":"author"})
# print(author.text)
#
# tags = single_quotation.findAll("a",{"class":"tag"})
# #we can not print .text with findAll, for that we need a for loop.
#
# for tag in tags:
#     print(tag.text, end=', ')

########another one###############

# quotes_list = soup.findAll("div",{"class": "quote"})
# print(len(quotes_list))

#for url in range(10):



#
# for quote in quotes_list:
#     quotation = quote.find("span",{"class":"text"})
#     print(quotation.text)


