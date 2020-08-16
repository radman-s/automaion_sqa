from pages.drivers import Drivers
from pages.sqa_page import SqaPage
from pages import current_time

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

# test setup
expected_processing = 'Ajax Request is Processing!'
expected_validation = 'Form submited Successfully!'

# test start
sp.go()
sp.close_add.click()
sp.input_forms.click()
sp.ajax_form_submit.click()
sp.name_ajax.input_text('Mario')
sp.comment_ajax.input_text('No comment')
sp.submit_ajax.click()
processing = sp.success_ajax.text()
assert processing == expected_processing
print(f'{processing}')
current_time.sleep(2)
validation = sp.success_ajax.text()
assert validation == expected_validation
print(f'Test passed: {validation}')

browser.quit()



