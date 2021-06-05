class BasePage():

    def __init__(self, driver):
        print("Metoda inicjalizacyjna z BasePage")
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        print("Weryfikacja z BasePage")

class title_is(object):
    """An expectation for checking the title of a page.
    title is the expected title, which must be an exact match
    returns True if the title matches, false otherwise."""
    def __init__(self, title):
        self.title = title

    def __call__(self, driver):
        return self.title == driver.title