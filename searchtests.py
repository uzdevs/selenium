import unittest

import self as self
from selenium import webdriver
from selenium.webdriver.support.select import Select


class SearchTest(unittest.TestCase):
    def setUp(self):
        # create new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("shirts")
        self.search_field.submit()

        # get all anchor elements which have product names
        # displayed currently on result page using
        # find_element_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")

        self.assertEqual(2, len(products))

    def test_search_by_name(self):
        # get search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()

        # product name displayed
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))

        # print("Found " + str(len(products)) + " products:")
        # for product in products:
        #     print(product.text)

    def test_search_text_field_max_length(self):
        # get search text field
        search_field = self.driver.find_element_by_id("search")

        # check maxlength attribute is set to 128
        self.assertEqual("128", search_field.get_attribute('maxlength'))

    def test_search_button_enabled(self):
        # get search button
        search_button = self.driver.find_element_by_class_name("button")

        # check search button is enabled
        self.assertTrue(search_button.is_enabled())

    def test_count_of_promo_banners_images(self):
        # get promo banner list
        banner_list = self.driver.find_element_by_class_name("promos")

        # get images from the banner_list
        banners = banner_list.find_elements_by_tag_name("img")

        # check there are 20 tags displayed on the page
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        # get vip promo image
        vip_promo = self.driver.find_element_by_xpath("//img[@alt='Shop Private Sales - Members Only']")

        # check vip promo logo is displayed on home page
        self.assertTrue(vip_promo.is_displayed())

        # click on vip promo images to open the page
        vip_promo.click()

        # check page title
        self.assertEqual("VIP", self.driver.title)

    def test_my_account_link_is_displayed(self):
        # get account link
        account_link = self.driver.find_element_by_link_text("ACCOUNT")

        # check my account link is displayed/visible in the home page
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        # get the all the links with account text in it
        account_links = self.driver.find_elements_by_partial_link_text("ACCOUNT")

        # check account and my account link is displayed/visible in the home page footer
        self.assertTrue(2, len(account_links))

    def test_shopping_cart_empty_message(self):
        # check shopping cart of My shopping Cart block on Home Page
        shopping_cart_icon = \
            self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        shopping_cart_icon.click()

        shopping_cart_status = \
            self.driver.find_element_by_css_selector("p.empty").text
        self.assertEqual("You have no items in your shopping cart.", shopping_cart_status)

        close_button = self.driver.find_element_by_css_selector("div.minicart-wrapper a.close")
        close_button.click()

    def test_language_option(self):
        # list of expected values in Language dropdown
        exp_options = ['English', 'French', 'German']

        # empty list for capturing actual options displayed in the dropdown
        act_options = []

        # get the Your language dropdown as instance of Select class
        select_language = \
            Select(self.driver.find_element_by_id('select-language'))

        # check number of options in dropdown
        self.assertEqual(3, len(select_language.options))

        # get options in a list
        for option in select_language.options:
            act_options.append(option.text)

        # check expected options list with actual options list
        self.assertListEqual(exp_options, act_options)

        # check default selected options is English
        self.assertEqual("English", select_language.first_selected_option.text)

        # select an option using select_by_visible text
        select_language.select_by_visible_text("German")

        # check store is now German
        self.assertTrue("store=german" in self.driver.current_url)

        # changing language will refresh the page ,
        # we need to get find language dropdown once again
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)

    def test_store_cookie(self):
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_visible_text("French")
        self.assertEqual("french", self.driver.get_cookie("store")["value"])

        # changing language will refresh the page,
        # we need to get find language dropdown once again
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)

    def test_css_for_home_page(self):
        self.assertTrue("demo-logo.png" in
                        self.driver.find_element_by_css_selector("div.notice-inner")
                        .value_of_css_property("background-image"))

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
