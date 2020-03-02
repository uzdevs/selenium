import unittest
from searchtests import SearchTest
from homepagetests import HomeTestPage
from test_register import RegisterNewUser


#get all tests from SearchProductTest and HomepageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomeTestPage)
test_register = unittest.TestLoader().loadTestsFromTestCase(RegisterNewUser)
#create a test suite combing search_test and home_page_tests
smoke_tests = unittest.TestSuite([search_tests, home_page_tests, test_register])

#run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
