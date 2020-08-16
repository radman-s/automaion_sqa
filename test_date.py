from pages.drivers import Drivers
from pages.sqa_page import SqaPage
from pages.current_time import Date
import time

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

today = Date().time_format()

# test start
sp.go()
sp.close_add.click()
time.sleep(2)
sp.date_pickers.click()
sp.boot_date_pickers.click()
sp.select_date1.move_to()
sp.select_date1.click()
sp.today_button.click()
time.sleep(2)
sp.get_date.move_to()
date_input = sp.get_date.text()
print(f'from app: {date_input}')
print(f'actual time {today}')
browser.quit()
print('test passed')

# code in progress
# need to sort assedtion (string from file not returning)