from pages.drivers import Drivers
from pages.sqa_page import SqaPage

browser = Drivers('--start-maximized').chrome()
sp = SqaPage(driver=browser)

# test setup
fn = 'Barry'
ln = 'Brown'
eml = 'test_01_@gmail.com'
ph = '(845)884-4715'
adr = 'Test Address'
cit = 'Test city'
zp = '14785'
web = 'www.test.com'
pd = 'Test Project'

# test start
sp.go()
sp.input_forms.click()
sp.input_forms_submit.click()
sp.first_name.input_text(fn)
sp.last_name.input_text(ln)
sp.email.input_text(eml)
sp.phone.input_text(ph)
sp.address.input_text(adr)
sp.city.input_text(cit)
sp.state.input_text('Alaska')
sp.zip.input_text(zp)
sp.website_name.input_text(web)
sp.hosting_yes.click()
sp.project_description.input_text(pd)
sp.send.click()
browser.quit()
print('Test successful')


















