# from bs4 import BeautifulSoup
# import requests,json
# import pprint
# link="https://www.flipkart.com/realme-c21y-cross-black-32-gb/p/itm2a2e4f7554a21?pid=MOBG5ZGKG2HRSQB8&lid=LSTMOBG5ZGKG2HRSQB84SHCIC&marketplace=FLIPKART&q=realme+mobile&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_6_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_5_na_na_na&fm=SEARCH&iid=da2622a5-e986-4ee8-9471-d44ac0aea003.MOBG5ZGKG2HRSQB8.SEARCH&ppt=sp&ppn=sp&ssid=yr44mkcsfw3rbq4g1635224569556&qH=1fa38e164777fe68"
# url=requests.get(link)
# soup=BeautifulSoup(url.text,"html.parser")
# print(soup)
# mobile_name=soup.find("span", class_="B_NuCI").text
# print(mobile_name[:12])
# rating=soup.find(class_="_2d4LTz").text
# print(rating)
# price=soup.find( class_="_1BErVs _3hyeE5").text
# print(price[5:])
# color=soup.find( class_="_22QfJJ").text
# print(color[22:])

dic={"a":2,"b":4}
dic1={"c":3,"b":3}
dic2={"d":1,"e":4}
sum=0
for i in dic:
    sum=sum+1
    print()