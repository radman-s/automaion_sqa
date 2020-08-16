from pages.drivers import Drivers
from pages.sqa_page import SqaPage

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

# test start
sp.go()
check_mark = '✔'
# go to the bootstrap alerts page
sp.close_add.click()
sp.start_practising.click()
sp.bootstrap_alerts.click()

# autoclosable success message
exepected_auto_scs = "I'm an autocloseable success message. I will hide in 5 seconds."

sp.autoclose_scs_button.click()
auto_scs = sp.autoclose_scs_msg.text()
assert auto_scs == exepected_auto_scs
print(auto_scs)
sp.autoclose_scs_msg.wait_close()
print(f'message closed {check_mark}')
print()

# normal success message
exepected_normal_scs = "×\n\
I'm a normal success message. To close use the appropriate button."

sp.normal_scs_button.click()
normal_scs = sp.normal_scs_msg.text()
assert normal_scs == exepected_normal_scs
print(normal_scs[1:])
sp.normal_close_msg.click()
print(f'message closed {check_mark}')















