from pages.drivers import Drivers
from pages.sqa_page import SqaPage
from pathlib import Path
import os
import time

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

data = 'test data'

# test start
sp.go()
sp.close_add.click()
sp.alerts_modals.click()
sp.file_download.click()
sp.enert_data.input_text(data)
time.sleep(1)
sp.enert_data.enter()
sp.generate_file.click()
sp.download.click()
time.sleep(1)

# validate correct file was downloaded
txt = Path("C:\\Users\\radss\\Downloads\\easyinfo.txt").read_text()
assert data.strip() == txt.strip()

print(f'upload:    {data}')
print(f'dwownload: {txt}')
print()
print('test passed')
time.sleep(1)
# remove file from downloads after compared
os.remove("C:\\Users\\radss\\Downloads\\easyinfo.txt")

browser.quit()






