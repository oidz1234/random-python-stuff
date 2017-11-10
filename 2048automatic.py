from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')


i = 0
while i < 1000:

    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
    i = i + 1

    if i == 1000:
        i = 0
        browser.refresh()

   
