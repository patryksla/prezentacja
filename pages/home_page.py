from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import HomePageLocators


class HomePage(BasePage):

    def click_close_newsletter_btn(self):
        wait = WebDriverWait(self.driver, 60)
        newsletter_element = wait.until(EC.element_to_be_clickable(HomePageLocators.CLOSE_NEWSLETTER_BTN))
        newsletter_element.click()

    def click_zaloguj_btn(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable(HomePageLocators.ZALOGUJ_BTN))
        element.click()
