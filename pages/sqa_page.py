from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class SqaPage(BasePage):

    url = 'https://www.seleniumeasy.com/test/'

    # nav examples
    @property
    def home_bar(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="home_bar"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def basic_bar(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="basic_example"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def intermediate_bar(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="inter_example"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def advanced_bar(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="advanced_example"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def completed_bar(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="done_example"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def close_add(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="at-cv-lightbox-close"]')
        return BaseElement(driver=self.driver, locator=locator)

    # input form
    @property
    def input_forms(self):
        locator = Locator(By.XPATH, '//a[text()="Input Forms"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def input_forms_submit(self):
        locator = Locator(By.XPATH, '(//a[text()="Input Form Submit"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def first_name(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="first_name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_name(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="last_name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="email"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def phone(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="phone"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def address(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="address"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def city(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="city"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def state(self):
        locator = Locator(By.CSS_SELECTOR, 'select[name="state"]')
        return BaseElement(driver=self.driver, locator=locator)

    # @property
    # def state(self):
    #     locator = Locator(By.XPATH, '//option[text()="Please select your state"]')
    #     return BaseElement(driver=self.driver, locator=locator)

    @property
    def zip(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="zip"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def website_name(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="website"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hosting_yes(self):
        locator = Locator(By.XPATH, '(//input[@name="hosting"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def project_description(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[name="comment"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def send(self):
        locator = Locator(By.CSS_SELECTOR, 'button[class="btn btn-default"]')
        return BaseElement(driver=self.driver, locator=locator)

    # ajax form
    @property
    def ajax_form_submit(self):
        locator = Locator(By.XPATH, '(//a[text()="Ajax Form Submit"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def name_ajax(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="title"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def comment_ajax(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[id="description"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submit_ajax(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="btn-submit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def success_ajax(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="submit-control"]')
        return BaseElement(driver=self.driver, locator=locator)

    # date pickers
    @property
    def date_pickers(self):
        locator = Locator(By.XPATH, '//a[text()="Date pickers"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def boot_date_pickers(self):
        locator = Locator(By.XPATH, '(//a[text()="Bootstrap Date Picker"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_date1(self):
        locator = Locator(By.XPATH, '(//span[@class="input-group-addon"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def today_button(self):
        locator = Locator(By.XPATH, '(//th[@class="today"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_date(self):
        locator = Locator(By.XPATH, '(//input[@class="form-control"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    # alerts
    @property
    def alerts_modals(self):
        locator = Locator(By.XPATH, '(//a[@class="dropdown-toggle"])[5]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bootstrap_alerts(self):
        locator = Locator(By.XPATH, '(//a[text()="Bootstrap Alerts"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def start_practising(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="btn_basic_example"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def autoclose_scs_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="autoclosable-btn-success"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def autoclose_scs_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="alert alert-success alert-autocloseable-success"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def normal_scs_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="normal-btn-success"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def normal_scs_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="alert alert-success alert-normal-success"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def normal_close_msg(self):
        locator = Locator(By.XPATH, '(//button[@class="close"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def file_download(self):
        locator = Locator(By.XPATH, '(//a[text()="File Download"])')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def enert_data(self):
        locator = Locator(By.CSS_SELECTOR, 'textarea[id="textbox"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def generate_file(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="create"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def download(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="link-to-download"]')
        return BaseElement(driver=self.driver, locator=locator)

    # drag and drop
    @property
    def drag_and_drop(self):
        locator = Locator(By.XPATH, '(//a[text()="Drag and Drop"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag1(self):
        locator = Locator(By.XPATH, '//span[text()="Draggable 1"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag2(self):
        locator = Locator(By.XPATH, '//span[text()="Draggable 2"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag3(self):
        locator = Locator(By.XPATH, '//span[text()="Draggable 3"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag4(self):
        locator = Locator(By.XPATH, '//span[text()="Draggable 4"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drop_here(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="mydropzone"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drop_list(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="droppedlist"]')
        return BaseElement(driver=self.driver, locator=locator)

    # progress bar
    @property
    def boot_progress_bar(self):
        locator = Locator(By.XPATH, '//a[text()="Bootstrap Download Progress bar"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def progress_percent0(self):
        locator = Locator(By.XPATH, '//div[text()="0%"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def progress_percent100(self):
        locator = Locator(By.XPATH, '//div[text()="100%"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def download_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="cricle-btn"]')
        return BaseElement(driver=self.driver, locator=locator)

    # tables
    @property
    def table_data(self):
        locator = Locator(By.XPATH, '(//a[text()="Table Data Download"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def table_search(self):
        locator = Locator(By.XPATH, '(//a[text()="Table Sort & Search"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sort_salary(self):
        locator = Locator(By.XPATH, '//th[text()="Salary"]')
        return BaseElement(driver=self.driver, locator=locator)




