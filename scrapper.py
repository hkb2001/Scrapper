from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pandas

from random import randint
from time import sleep

options = Options()
options.headless = True     # to hide the browser

driverPath = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=driverPath)

url = 'https://www.daraz.pk/smartphones/?page=1&spm=a2a0e.home.cate_1.1.6e1f4937nlJB4e'
driver.get(url)

main = driver.find_element_by_class_name("ant-pagination ")
pages = main.find_elements_by_class_name("ant-pagination-item")
lastPage = pages[-1]
lastPage = int(lastPage.text)

names = []
prices = []

currentPageNumber = 1
while currentPageNumber <= lastPage:

    time = randint(2, 10)
    sleep(time)

    pageSource = driver.page_source

    mainDiv = driver.find_element_by_class_name("box--ujueT")
    itemDetails = mainDiv.find_elements_by_class_name("info--ifj7U")

    for itemDetail in itemDetails:
        name = str(itemDetail.find_element_by_class_name("title--wFj93").text)
        names.append(name)

        price = str(itemDetail.find_element_by_class_name("price--NVB62").text)
        prices.append(price)

    currentPageNumber += 1
    url = 'https://www.daraz.pk/smartphones/?page=' + str(currentPageNumber) + '&spm=a2a0e.home.cate_1.1.6e1f4937nlJB4e'
    driver.get(url)


data = pandas.DataFrame({"Price": prices, "Mobile Names": names})
data.to_csv("mobileData.csv", index=False)

driver.quit()
