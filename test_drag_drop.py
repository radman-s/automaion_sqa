from pages.drivers import Drivers
from pages.sqa_page import SqaPage

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

sp.go()

sp.close_add.click()
sp.advanced_bar.click()
sp.drag_and_drop.click()
# drop_zone = browser.find_element_by_css_selector('div[id="mydropzone"]')
sp.drag1.drag_offset(50,0)
# sp.drag1.drag_to(sp.drop_here)
# sp.drag2.drag_to(sp.drop_here)
# sp.drag3.drag_to(sp.drop_here)
# sp.drag4.drag_to(sp.drop_here)


