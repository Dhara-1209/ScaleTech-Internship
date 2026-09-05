from selenium import webdriver
from pathlib import Path

driver = webdriver.Chrome()

html_file = Path("productshop.html").resolve()
driver.get(html_file.as_uri())

print(driver.title)

show_products = driver.find_element("id", "show-products")
show_products.click()

products = driver.find_elements("css selector", ".product")

for product in products:
    print(product.text)

driver.quit()