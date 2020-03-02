from selenium import webdriver
import time
import unittest

class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_register_new_user(self):
        driver = self.driver

        # click on log in link to open Login page
        driver.find_element_by_link_text("ACCOUNT").click()
        driver.find_element_by_link_text("My Account").click()

        # Get the Create account button
        create_account_button = driver.find_element_by_link_text("CREATE AN ACCOUNT")

        # Check create an account button is displayed and enabled
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())

        # click on Create account button. this will display new account
        create_account_button.click()

        # check title
        self.assertEqual("Create New Customer Account", driver.title)

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath("//button[@title = 'Register']")

        # check max length of the first name and last name textbox
        self.assertEqual('255', first_name.get_attribute('maxlength'))
        self.assertEqual('255', last_name.get_attribute('maxlength'))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and
                        email_address.is_enabled() and news_letter_subscription.is_enabled()
                        and password.is_enabled() and confirm_password.is_enabled()
                        and submit_button.is_enabled())

        # check sign up for the newsletter is unchecked
        self.assertFalse(news_letter_subscription.is_selected())

        user_name = 'user_' + time.strftime('%Y%m%d%H%M%S', time.gmtime())

        # fill out all the fields
        first_name.send_keys('Test')
        last_name.send_keys(user_name)
        news_letter_subscription.click()
        email_address.send_keys((user_name + '@example.com'))
        password.send_keys('tester')
        confirm_password.send_keys('tester')

        # click submit button to submit the form
        submit_button.click()

        # check new user is registered
        self.assertEqual('Hello, Test ' + user_name + '!',
                         driver.find_element_by_css_selector('p.hello > strong').text)
        driver.find_element_by_link_text('ACCOUNT').click()
        self.assertTrue(driver.find_element_by_link_text('Log Out').is_displayed())

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.TestCase(verbosity=2)



