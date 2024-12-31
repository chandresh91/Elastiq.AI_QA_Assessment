import pytest
from Pages.TableSearchPage import TableSearchPage
from Utility.DriverSetup import get_driver


@pytest.fixture(scope="class")
def setup(request):
    driver = get_driver()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestTableSearch:

    def test_search_new_york(self):
        page = TableSearchPage(self.driver)
        page.search_text("New York")

        # Get the visible row count
        visible_rows = page.get_visible_rows_count()

        # Check if there are exactly 5 rows
        assert visible_rows == 5, f"Expected 5 rows, but got {visible_rows} rows."

        # Check that each of the rows contains 'New York'
        col_texts = page.get_all_visible_col_text()
        for col in col_texts:
            assert "New York" in col


