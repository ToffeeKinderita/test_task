class Environment:
    BASE_URL = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"


class TestData:
    LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGER_NAME_OF_THE_EXECUTED_TEST = 'Test name is: '
    TEST_DATA_FOR_INSERT_SQL = 'TEST'
    TEST_DATA_FOR_UPDATE_SQL = "UPD"
    CONTACTNAME_FOR_SEARCH = 'Giovanni Rovelli'
    ADDRESS_BY_CONTACTNAME = 'Via Ludovico il Moro 22'
    COUNTRY = 'London'
    NUM_OF_RECORDS_FOR_LONDON = 6


class AssertionErrorsText:
    INCORRECT_NUMBER_OF_RECORDS_RETURNED = 'Incorrect number of returned records'
    RECORD_IS_ABSENT = 'The record is absent: ContactName {contactname}'
    RECORD_IS_STILL_PRESENT = 'The record is still present: ContactName {contactname}'
    INCORRECT_ADDRESS_OR_USER_NOT_FOUND = 'The address is incorrect of the user was not found'


class SqlLocators:
    DIV_QUERY_TABLE = 'div#divResultSQL>div'
    RUN_SQL_BTN = '.w3-green.w3-btn'
    TABLE_RECORDS_LIST = 'div#divResultSQL tbody tr'
    EACH_RECORD_VALUE = 'div#divResultSQL tbody tr>td:nth-child(3)'
    FIND_TEXT_GET_ADDRESS = "//text()[. = '{param}']/../../td[4]"
    XPATH_FIND_BY_TEXT = "//text()[. = '{param}']/.."


class SqlQueries:
    SQL_ALL_CUSTOMERS = 'SELECT * FROM Customers;'
    SQL_ONLY_ONE_COUNTRY_CUSTOMERS = 'SELECT * FROM Customers where city = "{country}";'
    SQL_FIND_RECORD_BY_CONTACTNAME = 'select * from Customers where ContactName = "{contactname}";'
    SQL_ADD_NEW_RECORD = 'Insert into Customers ("CustomerName", "ContactName", "Address", "City", "PostalCode", "Country") values ("{customername}","{contactname}","{address}","{city}","{postalcode}","{country}")'
    SQL_UPDATE_THE_RECORD_WHERE_CONTACTNAME = 'Update Customers set CustomerName = "{customername}", ContactName = "{contactname}", Address = "{address}", City = "{city}", PostalCode = "{postalcode}", Country = "{country}" where contactName = "{where}";'
    SQL_DELETE_BY_CONTACTNAME = 'delete from Customers where ContactName = "{contactname}";'
