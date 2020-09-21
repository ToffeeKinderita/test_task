from contextlib import contextmanager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.constants import Environment, SqlLocators
from selenium.webdriver import Remote


class BasePage:
    """This class is the parent class for all the pages in the application."""

    def __init__(self, driver):
        self._driver: Remote = driver
        self._driver.implicitly_wait(5)

    def go_to_url(self):
        self._driver.get(Environment.BASE_URL)

    @contextmanager
    def wait_for_queryset_to_load(self):
        old_result = self._driver.find_element_by_css_selector(SqlLocators.DIV_QUERY_TABLE)
        yield
        WebDriverWait(self._driver, 5).until(
            expected_conditions.staleness_of(old_result))


class SQLExecutionPage(BasePage):

    def find_execution_window_send_query(self, query):
        element = self._driver.execute_script(
            f"window.editor.setValue('{query}');")
        return element

    def click_run_sql_btn(self):
        self._driver.find_element_by_css_selector(SqlLocators.RUN_SQL_BTN).click()

    def query(self, query):
        self.find_execution_window_send_query(query)
        with self.wait_for_queryset_to_load():
            self.click_run_sql_btn()

    def check_number_of_returned_sql_records(self):
        element = self._driver.find_elements_by_css_selector(SqlLocators.TABLE_RECORDS_LIST)
        total_number_of_table_records_without_header = len(element) - 1
        return total_number_of_table_records_without_header

    def check_record_is_present(self, value):
        try:
            self._driver.find_element_by_xpath(SqlLocators.XPATH_FIND_BY_TEXT.format(param=value))
            return True
        except NoSuchElementException:
            return False

    def get_address_of_defined_record(self, value):
        try:
            self.check_record_is_present(value)
            element = self._driver.find_element_by_xpath(SqlLocators.FIND_TEXT_GET_ADDRESS.format(param=value))
            address = element.text
            return address
        except NoSuchElementException:
            return f"No results found for {value}"
