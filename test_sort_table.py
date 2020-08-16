from pages.sqa_page import SqaPage
from pages.drivers import Drivers
from pages.base_tree import Root
from pages.listings_data_table import Listings
import time

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)


sp.go()

sp.close_add.click()
sp.advanced_bar.click()
sp.table_search.click()
time.sleep(2)

# lxml setup
html = browser.page_source
listing = Root(html, locator='.//table/tbody/tr')

one = listing.get_listings(Listings)[1]
two = listing.get_listings(Listings)[2]
three = listing.get_listings(Listings)[3]

line_one = list(one.all)
line_two = two.all
line_three = three.all
print(line_one)
print(line_two)
print(line_three)

sp.sort_salary.click()
sp.sort_salary.click()

# code in progress

