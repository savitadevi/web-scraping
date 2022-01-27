from bs4 import BeautifulSoup
import requests,json
import pprint
link="https://www.boohoo.com/glitter-plisse-skater-midi-skirt/FZZ34112.html"
url= requests.get(link)
# print(url)
soup=BeautifulSoup(url.text,"html.parser")
# print(soup)
dress_name=soup.find(class_="product-name is-mobile js-product-name").text
print(dress_name)
price=soup.find("span",class_="price-sales").text
print(price)
color=soup.find("span", class_="selected-value").text
print(color)
size=soup.find(class_="swatches size clearfix").text
# size=soup.find(class_="attribute-title").text
print(size)
dict={}
dict["dress_name"]=dress_name
dict["price"]=price
dict["color"]=color
dict["size"]=size
print(dict)
with open("skirts.json","w")as a:
   json.dump(dict,a,indent=4)
