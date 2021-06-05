from selenium.webdriver.common.by import By

class HomePageLocators():
    CLOSE_NEWSLETTER_BTN = (By.XPATH, '//div [@class="popup-window-close-button"][@popup-window-id="3"]')
    ZALOGUJ_BTN = (By.XPATH, '//*[@id="layoutPortletElement_359"]/header/div/div[3]/ul/li[2]/a/span')

class LoginPageLocators():
    REGISTER_BTN = (By.XPATH, '//*[@class="sign-in-form-table"]/tbody/tr[7]/td[2]/a[2]')

class RegistrationPageLocators():
    NAME_INPUT = (By.CSS_SELECTOR, '#Name_51')
    SURNAME_INPUT = (By.NAME, 'Surname_51')
    NATIONALITY_INPUT = (By.ID, 'Country_51')
    NATIONALITY_CHOOSE = (By.XPATH, '//*[@id="Country_51"]/option[2]')
    VOIVODESHIP_INPUT = (By.XPATH, '//*[@id="Region_51"]')
    VOIVODESHIP_CHOOSE = (By.XPATH, '//*[@id="Region_51"]/option[2]')
    STREET_INPUT = (By.XPATH, '//*[@id="Street_51"]')
    BUILDING_NUMBER_INPUT = (By.XPATH, '//*[@id="Building_51"]')
    POSTAL_CODE_INPUT = (By.XPATH, '//*[@id="Postal_51"]')
    CITY_INPUT = (By.XPATH, '//*[@id="City_51"]')
    PHONE_NUMBER_INPUT = (By.XPATH, '//*[@id="Phone_51"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="Email_51"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="Password_51"]')
    PASSWORD_CONFIRMATION_INPUT = (By.XPATH, '//*[@id="PasswordConfirmation_51"]')
    ACCEPT_AGREEMENT1 = (By.XPATH, '//*[@id="createAccountForm_instance_51"]/table/tbody/tr[47]/td[2]/div/div[1]/div/div')
    ACCEPT_RODO = (By.XPATH, '//*[@id="createAccountForm_instance_51"]/table/tbody/tr[49]/td[2]/div/div[1]/div/div')
    CREATE_ACCOUNT = (By.XPATH, '//*[@id="createAccountForm_instance_51"]/table/tbody/tr[50]/td[2]/input')
    ERROR_MESSAGES_DIV = (By.XPATH, '//*[@id="createAccountForm_instance_51"]/table/tbody/tr[38]/td/div')


