from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from pynput.keyboard import Key, Controller
import random
keyboard = Controller()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
driver = webdriver.Chrome(executable_path='CHROMEDRIVERPATH')
driver.get("https://monkeytype.com") 
time.sleep(4)
#letters = []
#letters = driver.find_elements_by_tag_name("letter")
#for letter in letters:
#    content.append(letter.get_attribute('content'))
raw = driver.page_source
soup = BeautifulSoup(raw, "html.parser")
content = soup.find_all(class_ = "word")
for i in range(5):
    print("Get ready... {}".format(5 - i))
    time.sleep(1)

count = 0
for word in content:
    newsoup = BeautifulSoup(str(word), "html.parser")
    final = (newsoup.find_all("letter"))
    for i in final:
        if count < len(word):
            scuff = random.randint(0, 100)
            if scuff == 50:
                keyboard.type(random.choice(alphabet))
            else:
                keyboard.type(str(i.text))
                time.sleep(random.uniform(0.08, 0.1))
            count += 1
        if count == len(word):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            count = 0
