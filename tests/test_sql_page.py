import pytest

from pages.sql_page import SQLExecutionPage
from utils.constants import SqlQueries, TestData, AssertionErrorsText
from utils.utils import generate_unique_str


class TestSQLPage:

    @pytest.fixture(scope="session")
    def page(self, browser):
        sql_page = SQLExecutionPage(browser)
        sql_page.go_to_url()
        yield sql_page

    @pytest.fixture(scope="function")
    def add_new_record_to_db_before_test(self, page):
        contact_name = generate_unique_str(7)
        page.query(
            SqlQueries.SQL_ADD_NEW_RECORD.format(customername=TestData.TEST_DATA_FOR_INSERT_SQL,
                                                 contactname=contact_name, address=TestData.TEST_DATA_FOR_INSERT_SQL,
                                                 city=TestData.TEST_DATA_FOR_INSERT_SQL,
                                                 postalcode=TestData.TEST_DATA_FOR_INSERT_SQL,
                                                 country=TestData.TEST_DATA_FOR_INSERT_SQL))
        yield contact_name

    def test_select_all_customers(self, page):
        page.query(SqlQueries.SQL_ALL_CUSTOMERS)
        address = page.get_address_of_defined_record(TestData.CONTACTNAME_FOR_SEARCH)
        assert address == TestData.ADDRESS_BY_CONTACTNAME, AssertionErrorsText.INCORRECT_ADDRESS_OR_USER_NOT_FOUND

    def test_number_of_records_by_query(self, page):
        page.query(SqlQueries.SQL_ONLY_ONE_COUNTRY_CUSTOMERS.format(country=TestData.COUNTRY))
        assert page.check_number_of_returned_sql_records() == TestData.NUM_OF_RECORDS_FOR_LONDON, \
            AssertionErrorsText.INCORRECT_NUMBER_OF_RECORDS_RETURNED

    def test_add_new_record(self, page, add_new_record_to_db_before_test):
        page.query(SqlQueries.SQL_FIND_RECORD_BY_CONTACTNAME.format(contactname=add_new_record_to_db_before_test))
        assert page.check_record_is_present(
            add_new_record_to_db_before_test) is True, \
            AssertionErrorsText.RECORD_IS_ABSENT.format(contactname=add_new_record_to_db_before_test)

    def test_update_of_sql_record(self, page, add_new_record_to_db_before_test):
        page.query(
            SqlQueries.SQL_UPDATE_THE_RECORD_WHERE_CONTACTNAME.format(
                customername=TestData.TEST_DATA_FOR_UPDATE_SQL,
                contactname=TestData.TEST_DATA_FOR_UPDATE_SQL,
                address=TestData.TEST_DATA_FOR_UPDATE_SQL, city=TestData.TEST_DATA_FOR_UPDATE_SQL,
                postalcode=TestData.TEST_DATA_FOR_UPDATE_SQL,
                country=TestData.TEST_DATA_FOR_UPDATE_SQL,
                where=add_new_record_to_db_before_test))
        page.query(
            SqlQueries.SQL_FIND_RECORD_BY_CONTACTNAME.format(contactname=TestData.TEST_DATA_FOR_UPDATE_SQL))
        assert page.check_record_is_present(
            TestData.TEST_DATA_FOR_UPDATE_SQL) is True, \
            AssertionErrorsText.RECORD_IS_ABSENT.format(contactname=TestData.TEST_DATA_FOR_UPDATE_SQL)

    def test_delete_record_by_contactname(self, page, add_new_record_to_db_before_test):
        page.query(SqlQueries.SQL_DELETE_BY_CONTACTNAME.format(contactname=add_new_record_to_db_before_test))
        page.query(
            SqlQueries.SQL_FIND_RECORD_BY_CONTACTNAME.format(contactname=add_new_record_to_db_before_test))
        assert page.check_record_is_present(
            add_new_record_to_db_before_test) is False, \
            AssertionErrorsText.RECORD_IS_STILL_PRESENT.format(contactname=add_new_record_to_db_before_test)
