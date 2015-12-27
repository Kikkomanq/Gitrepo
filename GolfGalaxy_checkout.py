# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class GolgGalaxyPython(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://m.golfgalaxy.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_golg_galaxy_python(self):
        driver = self.driver
        driver.get("http://m.golfgalaxy.com/")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("(//a[contains(text(),'Bags')])[22]").click()
        driver.find_element_by_css_selector("#panel4 > ul.accordion.second-tier > li > a").click()
        driver.find_element_by_link_text("Cart Bags (42)").click()
        # driver.find_element_by_css_selector("p.title").click()
        driver.find_element_by_link_text("Titleist Lightweight Cart Bag").click()
        driver.find_element_by_link_text("Add To Cart").click()
        driver.find_element_by_css_selector("div.go_to_cart > #GotoCartButton2 > div.button_text").click()
        driver.find_element_by_link_text("Secure Checkout").click()
        driver.find_element_by_css_selector("div.button_text").click()
        driver.find_element_by_id("shippingAddressForm1_firstName").clear()
        driver.find_element_by_id("shippingAddressForm1_firstName").send_keys("John")
        driver.find_element_by_id("shippingAddressForm1_lastName").clear()
        driver.find_element_by_id("shippingAddressForm1_lastName").send_keys("New")
        driver.find_element_by_id("shippingAddressForm1_address1").clear()
        driver.find_element_by_id("shippingAddressForm1_address1").send_keys("160 5th Ave")
        driver.find_element_by_id("shippingAddressForm1_city").clear()
        driver.find_element_by_id("shippingAddressForm1_city").send_keys("New York")
        Select(driver.find_element_by_id("shippingAddressForm1_state")).select_by_visible_text("New York")
        driver.find_element_by_id("shippingAddressForm1_zipCode").clear()
        driver.find_element_by_id("shippingAddressForm1_zipCode").send_keys("10010")
        driver.find_element_by_id("shippingAddressForm1_phone1").clear()
        driver.find_element_by_id("shippingAddressForm1_phone1").send_keys("(445)554-5544")
        driver.find_element_by_css_selector("#shippingAddressForm1_nextButton_addSPC > div.button_text").click()
        driver.find_element_by_css_selector("#shippingMethodForm_nextButton > div.button_text").click()
        driver.find_element_by_id("sharedShipBillAddress").click()
        driver.find_element_by_id("sharedAddress_email1").clear()
        driver.find_element_by_id("sharedAddress_email1").send_keys("bbbelgradetesting@gmail.com")
        driver.find_element_by_id("account1_1").clear()
        driver.find_element_by_id("account1_1").send_keys("4111-1111-1111-1111")
        Select(driver.find_element_by_id("expire_month_1")).select_by_visible_text("03 - March")
        Select(driver.find_element_by_id("expire_year_1")).select_by_visible_text("2021")
        driver.find_element_by_id("cc_cvc_1").clear()
        driver.find_element_by_id("cc_cvc_1").send_keys("123")
        driver.find_element_by_css_selector("#paymentSharedBillingForm_nextButton > div.button_text").click()
        driver.find_element_by_css_selector("#paymentBillingForm_OrderConfirmation2 > div.button_text").click()
        driver.find_element_by_css_selector("a.button_secondary > div.button_text").click()
        # ERROR: Caught exception [ERROR: Unsupported command [captureEntirePageScreenshot | //home//milan//Lightshot//test.png | ]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
