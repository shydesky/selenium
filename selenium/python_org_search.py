from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("http://www.shydesky.top")
pap=driver.find_element_by_id('primary-nav')
print pap
sss=driver.find_elements_by_class_name('entry-excerpt')
import pdb;pdb.set_trace()
driver.close()
