from selenium import webdriver
from bs4 import BeautifulSoup
import requests

PATH = 'C:\chromedriver_win32\chromedriver.exe'
url = 'https://www.daraz.pk/laptops/?spm=a2a0e.home.cate_1.5.35e34937sTvRiR'


driver  = webdriver.Chrome(PATH)


driver.get(url)

# Put the page source into a variable and create a BS object from it
soup_file=driver.page_source
soup = BeautifulSoup(soup_file, "html.parser")

# Load and print the title and the text of the <div>
# print(soup.title.get_text())
# print(soup.find(id='text').get_text())

print("-------\n\n\n")
price = soup.find_all("span", "c13VH6")

for p in price:
    print(p.text.strip())

print("-------\n\n\n")

driver.quit()

'''response=requests.get(url)
# print(response.text)


bs=BeautifulSoup(response.content,"html.parser")
# formatted_text=bs.prettify()
# print(formatted_text)

a = bs.find("span", "c13VH6")
print(a)'''