from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def wait_close(self):
        element = WebDriverWait(self.driver,20).until(EC.invisibility_of_element_located(locator=self.locator))
        self.web_element = element

    def arrow_down(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ARROW_DOWN).perform()
        return None

    def enter(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ENTER).perform()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def select_drop(self, val):
        element = Select(self.web_element)
        element.select_by_value(val)
        return None

    def text(self):
        text = self.web_element.text
        return text

    def move_to(self):
        element = ActionChains(self.driver)
        element.move_to_element(self.web_element).perform()
        return None

    def drag_to(self, target):
        element = ActionChains(self.driver)
        element.click_and_hold(self.web_element).move_to_element(self.web_element).release(target).perform()
        return None

    def drag_drop(self, target):
        element = ActionChains(self.driver)
        element.click_and_hold(self.web_element).move_to_element(target).release(target).perform()
        return None

    def drag_offset(self, offset, yoffset):
        element = ActionChains(self.driver)
        element.click_and_hold(self.web_element).move_to_element(offset, yoffset).release().perform()










