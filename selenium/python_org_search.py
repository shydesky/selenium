from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
url = 'https://www.youtube.com'
driver.get(url)
sss=driver.find_elements_by_class_name('yt-shelf-grid-item')
print len(sss)
driver.close()
