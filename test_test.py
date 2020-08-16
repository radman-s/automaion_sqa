from pages.drivers import Drivers
from pages.sqa_page import SqaPage

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)
sp.go()













