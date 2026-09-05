from bs4 import BeautifulSoup
with open("product.html", "r", encoding="utf-8") as file:
    html = file.read()
soup=BeautifulSoup(html,"html.parser")
print("Title:",soup.title.text)
Products = soup.find_all("div", class_="product")
for product in Products:
    name = product.find("h2").text
    price = product.find("p", class_="price").text
    url = product.find("a").get("href")

    print(name, "|", price, "|", url)
