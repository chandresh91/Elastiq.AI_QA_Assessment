from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class TableSearchPage(BasePage):
    SEARCH_BOX = (By.CSS_SELECTOR, "input[type='search']")
    TABLE_COLUMN = (By.XPATH, "//tr[@role='row']//td[3]")
    TABLE_ROWS = (By.XPATH,"//tr[@role='row']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    def search_text(self, query):
        self.enter_text(self.SEARCH_BOX, query)

    def get_visible_rows_count(self):
        rows = self.find_elements(self.TABLE_ROWS)
        return len([row for row in rows if row.is_displayed()])

    def get_all_visible_col_text(self):
        cols = self.find_elements(self.TABLE_COLUMN)
        return [cols.text for col in cols if col.is_displayed()]
