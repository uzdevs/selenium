import unittest
import HtmlTestRunner
# import HTMLTestRunner
import os
from test_register import RegisterNewUser
from homepagetests import HomeTestPage
from searchtests import SearchTest
from collections import Mapping
from collections import MutableMapping

# get the dicrectory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
test_register_new_user = unittest.TestLoader().loadTestsFromTestCase(RegisterNewUser)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomeTestPage)
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)

# create a test combining search_test and homepagetests
smoke_tests = unittest.TestSuite([test_register_new_user, home_page_test, search_test])

# open the report file
outfile = open(dir + 'NewRegisterReport.html', 'w')

# configure HtmlTestRunner
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile,
                                       report_title='Test report',
                                       descriptions='Tests',
                                       output='C:\\DEV\\selenium')

# run the suite using HTMLTestRunner
runner.run(smoke_tests)
