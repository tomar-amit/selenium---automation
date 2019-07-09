#import time
#import the webdriver form the selenium module
from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe')  #give the path of chromedriver in argument 

#maximize the window, if you required
browser.maximize_window()

#search the URL
browser.get('https://www.youtube.com/')

#find the seacrh box
search = browser.find_element_by_name('search_query')

#enter text/query to search... ex - love me like you do
search.send_keys('love me like you do')

#hit the search button
search.submit()

#find the top one search result, and click it to play
browser.find_element_by_id('video-title').click()

#time.sleep(300)
#browser.close()



