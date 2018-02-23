############################################################
#Name : Sathi.Ranganathan
#Porject : SSH autnentication manager
#date : Feburay,23.2018
############################################################
import unittest
import json
import time
import urllib2
from selenium import webdriver
import os
import unittest
from selenium.webdriver.support.select import Select
import time


class PArkingLottest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://adam.goucher.ca/parkcalc/")

    def test_STP_select(self):
        print ("------Select Short-Term Parking test------")
        select = Select(self.driver.find_element_by_id('Lot'))
        select.select_by_visible_text('Short-Term Parking')
        self.assertIn("Short-Term Parking", select.first_selected_option.text)

    def test_EP_select(self):
        print ("------Select Economy Parking test------")
        select = Select(self.driver.find_element_by_id('Lot'))
        select.select_by_visible_text('Economy Parking')
        self.assertIn("Economy Parking", select.first_selected_option.text)

    def test_LTSP_select(self):
        print ("------Select Long-Term Surface Parking test------")
        select = Select(self.driver.find_element_by_id('Lot'))
        select.select_by_visible_text('Long-Term Surface Parking')
        self.assertIn("Long-Term Surface Parking", select.first_selected_option.text)

    def test_VP_select(self):
        print ("------Select Valaut Parking test------")
        select = Select(self.driver.find_element_by_id('Lot'))
        select.select_by_visible_text('Valet Parking')
        self.assertIn("Valet Parking", select.first_selected_option.text)

    def test_time_hour(self):
        print ("------Entering hour test------")
        elem = self.driver.find_element_by_name("EntryTime").clear()
        elem2 = self.driver.find_element_by_name("EntryTime")
        elem2.send_keys("01:00")
        self.assertIn("01:00", elem2.get_attribute('value'))
        elem2 = self.driver.find_element_by_name("EntryTime").clear()
        elem3 = self.driver.find_element_by_name("EntryTime")
        elem3.send_keys("12:00")
        self.assertIn("12:00", elem3.get_attribute('value'))

    def test_wrong_time_test(self):
        print ("------Entering wrong hour test------")
        elem = self.driver.find_element_by_name("EntryTime").clear()
        elem2 = self.driver.find_element_by_name("EntryTime")
        elem2.send_keys("-100:00")
        self.assertIn("-100:00", elem2.get_attribute('value'))

    def test_date_set(self):
        print ("------Entering date test------")
        elem = self.driver.find_element_by_name("EntryDate").clear()
        elem2 = self.driver.find_element_by_name("EntryDate")
        elem2.send_keys("01/31/2018")
        self.assertIn("01/31/2018", elem2.get_attribute('value'))
        elem2 = self.driver.find_element_by_name("EntryDate").clear()
        elem3 = self.driver.find_element_by_name("EntryDate")
        elem3.send_keys("12/31/2018")
        self.assertIn("12/31/2018", elem3.get_attribute('value'))

    def test_wrong_date_set(self):
        print ("------Entering wrong date test------")
        elem = self.driver.find_element_by_name("EntryDate").clear()
        elem2 = self.driver.find_element_by_name("EntryDate")
        elem2.send_keys("-01/-31/2018")
        self.assertIn("-01/-31/2018", elem2.get_attribute('value'))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
