from pages.drivers import Drivers
from pages.sqa_page import SqaPage
import time

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

sp.go()

sp.close_add.click()
sp.advanced_bar.click()
sp.boot_progress_bar.click()
start = sp.progress_percent0.text()
print(f'download start at:  {start}')
sp.download_button.move_to()
sp.download_button.click()
sp.download_button.click()
time.sleep(2)
finish = sp.progress_percent100.text()
print(f'download finish at: {finish}')
print('test passed')







