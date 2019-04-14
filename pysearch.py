import selenium
from selenium import webdriver
# Need this module to get keyboard input
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# So far headed in the right direction
# what I need to do is have my variable ready, right?

# I'm going to declare a value for search
search = "Red Rocket"

# Now I have to go to googles search page
browser.get("https://www.google.com")

# now we have to find the search box
search_form = browser.find_element_by_name('q')

# Now we gotta put the search into the format
search_form.send_keys(search)

# There is no search button so we have to click enter
search_form.send_keys(Keys.RETURN)


