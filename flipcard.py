 
from typing import Sized
from bs4 import BeautifulSoup
import requests,json
import pprint
dress_link="https://www.flipkart.com/kedar-fab-anarkali-gown/p/itma13a90ccb1937?pid=GWNFMHMGGFSH7CRY&lid=LSTGWNFMHMGGFSH7CRYEOZPJV&marketplace=FLIPKART&cmpid=content_gown_12884797849_u_8965229628_gmc_pla&tgi=sem,1,G,11214002,u,,,517829293436,,,,c,,,,,,,&ef_id=Cj0KCQjwiNSLBhCPARIsAKNS4_c6vObwU8BJmWoJcjhWIaDzN3N3zYVFUHljB94XWXgBvYalSk-r7OgaAmOdEALw_wcB:G:s&s_kwcid=AL!739!3!517829293436!!!u!293946777986!&gclid=Cj0KCQjwiNSLBhCPARIsAKNS4_c6vObwU8BJmWoJcjhWIaDzN3N3zYVFUHljB94XWXgBvYalSk-r7OgaAmOdEALw_wcB"
url=requests.get(dress_link)

beauti=BeautifulSoup(url.text,"html.parser")
rating=beauti.find("div",class_="_3LWZlK _3uSWvT").text

price=beauti.find("div", class_="_30jeq3 _16Jk6d").text
price1=price[1:]
# print(price1)

name=beauti.find("span",class_="B_NuCI").text
# print(name,"pppp")
brand=name[37:-9]
bran=name[:16]
# print(bran)




Size=beauti.find("span", class_="UYlt8X").text

color1=beauti.find("div",class_="_3Oikkn _3_ezix _2KarXJ _31hAvz").text

d={}
d["rating"]=rating
d["price"]=price1
d["Brand"]=bran
d["Name"]=brand
d["color"]=color1
d["Size"]=Size
# print(d)
with open("flipcard.json","w")as file:
    json.dump(d,file,indent=4)



