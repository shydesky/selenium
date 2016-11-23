from selenium import webdriver
from selenium.webdriver.common.keys import Keys

service_args = [
'--proxy=https://neweb.gq:81',
'--proxy-type=http',
'--ssl-protocol=any',
'--ignore-ssl-errors=true'
]
driver = webdriver.PhantomJS(service_args=service_args)
url = 'https://www.youtube.com'
driver.get(url)
sss=driver.find_elements_by_class_name('yt-shelf-grid-item')
print len(sss)
driver.close()



